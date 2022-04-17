import React, {useState} from 'react';
import { Button, TextField } from '@mui/material';
import { useNavigate } from 'react-router-dom'

function Projects({globalUser, setGlobalUser, currentProjId, setCurrentProjId }) {
    const navigate = useNavigate()

    const [projName, setName] = useState("")
    const [projId, setId] = useState("")
    const [projDescrip, setDescrip] = useState("")
    const[searchId, setSearchId] = useState("")
    const[error, setError] = useState("")

    const updateName = (newName) => {
        setName(newName.target.value)  }
    const updateId= (newId) => {
        setId(newId.target.value)  }
    const updateDescrip = (newDescrip) => {
        setDescrip(newDescrip.target.value)  }
    const updateSearchid = (newSearch) => {
        setSearchId(newSearch.target.value)  }

    const sendNewProj = () => {
        const sent = {        
            method: "POST",
            headers: {'Content-Type': 'application/json',
                    'Accept': 'application/json'},
            body: JSON.stringify(
                {name: projName,
                description: projDescrip,
                id: projId,
                username: globalUser
            })
        }
        if(projName.length < 1 )
        {
            setError("Name must be non-zero length")

        }
        else if (projDescrip.length < 1)
        {
            setError("description must be non-zero length")
        }
        else if(projId.length < 1 )
        {
            setError("ID must be non-zero length")
        }
        else{
            console.log("sending")
            fetch("/projecting",sent )
            .then(response => response.json())
             .then(data =>{
                console.log(data.message);
                if (data.message.trim() === 'project already exists')
                    {
                        setError(data.message)
                    }
                else
                {
                    // set the project ID here
                    setCurrentProjId(projId)

                    //setGlobalUser(usernm)
                    //console.log(globalUser)
                    setId("")
                    setDescrip("")
                    setError("")
                    setName("")
                    navigate('/resourceManagement')
                }
            })
            
        }



    }
    const checkProject = () =>{

        const sent = {        
            method: "POST",
            headers: {'Content-Type': 'application/json',
                    'Accept': 'application/json'},
            body: JSON.stringify(
                {
                     id: searchId,
                     username: globalUser
            })
        }
        if(searchId.length < 1)
        {
            setError("ID must be a non-zero length")
        }
        else{
            console.log("Sendings")
            // add the send here to /checkproj
           fetch("/checkProj",sent )
            .then(response => response.json())
             .then(data =>{
                console.log(data.message);
                if (data.message.trim() === 'approved')
                    {
                    // set the project ID here
                    setCurrentProjId(searchId)

                    
                    setSearchId("")
                    setError("")
                    
                    navigate('/resourceManagement')
                    }
                else
                {
                    setError(data.message)
                }
            })

        
        }


    }

    

    return (
        <div>
        
            <div className = 'navigationBar'>
                <Button variant="contained" onClick={()=>navigate('/dataaccess')} style = {{display: 'flex', position: 'fixed', bottom: 550, left: 25}}>Data Access</Button>
                {/* <Button variant="contained" onClick={()=>navigate('/ResourceManagement')} style = {{display: 'flex', position: 'fixed', bottom: 550, left: 200}}>Resource Management</Button> */}
                <h3 style = {{display: 'flex', position: 'fixed', bottom: 535, right: 200}}>{globalUser}</h3>
                <Button variant="contained" onClick={()=> {navigate('/'); setGlobalUser('Not Signed-In');}} style = {{display: 'flex', position: 'fixed', bottom: 550, right: 50}}>Sign Out</Button>
            </div>

            <h1>
                Projects Page
            </h1>
            <h3> {globalUser}</h3>
            <p>Create New Project</p>
            <TextField value = {projName} id="outlined-basic" label="Project Name" variant="outlined" onChange={updateName}/>
            <TextField value ={projDescrip} id="outlined-basic" label="Project Description" variant="outlined" onChange={updateDescrip}/>
            <TextField value = {projId} id="outlined-basic" label="ProjectID" variant="outlined" onChange = {updateId}/>
            <Button variant="contained" onClick={sendNewProj}>Create</Button>

            <p>Use existing Project</p>
            <TextField value = {searchId} id="outlined-basic" label="ProjectID" variant="outlined" onChange={updateSearchid}/>
            <Button variant="contained" onClick={checkProject}>Access Project</Button>
            <h3> {error} </h3>
            
        </div>
    );
}

export default Projects;
