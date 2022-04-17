import React, {useState, useEffect} from 'react';
import { Button, TextField } from '@mui/material';
import { useNavigate } from 'react-router-dom'


function ResourceManagement({globalUser, setGlobalUser, currentProjId, setCurrentProjId}) {
    const navigate = useNavigate()

    const [errorMsg, setError] = useState("")
    const [userhw1, setUserhw1] = useState("")
    const [userhw2, setUserhw2] = useState("")

    const [capacity1, setCapacity1] = useState("")
    const [availability1, setAvailability1] = useState("")
    const [quantity1, setQuantity1] = useState("")

    const [capacity2, setCapacity2] = useState("")
    const [availability2, setAvailability2] = useState("")
    const [quantity2, setQuantity2] = useState("")

    const [projName, setProjName] = useState("")
    const [projDescrip, setProjDescrip] = useState("")


    const updateCapacity1 = (newCapacity) => {
        setCapacity1(newCapacity.target.value)
    }
    const updateCapacity2 = (newCapacity) => {
        setCapacity2(newCapacity.target.value)
    }

    const updateAvailability1 = (newAvailability) => {
        setAvailability1(newAvailability.target.value)
    }
     const updateAvailability2 = (newAvailability) => {
        setAvailability2(newAvailability.target.value)
    }

    const updateQuantity1 = (newQuantity) => {
        setQuantity1(newQuantity.target.value)
    }
    const updateQuantity2 = (newQuantity) => {
        setQuantity2(newQuantity.target.value)
    }

    useEffect(() => {
        loadData();
      }, []);
    useEffect(() =>{
    loadData();
    },[quantity1])

    useEffect(() =>{
        loadData();
        },[quantity2])

   



    const loadData = () => {
        //setCapacity1("asdasd")
        const sent = {
            method: "POST",
            headers: {'Content-Type': 'application/json',
                    'Accept': 'application/json'},
            body: JSON.stringify(
                {id: currentProjId,
                username: globalUser

            })
        }
        fetch("/bigloader",sent )
            .then(response => response.json())
             .then(data =>{
                //console.log(data.message);
                if (data.message.trim() !== 'approved')
                    {
                        setError(data.message)
                    }
                else
                {
                    // set the project ID here
                    setAvailability1(data.avail1)
                    setCapacity1(data.capac1)
                    setAvailability2(data.avail2)
                    setCapacity2(data.capac2)
                    setUserhw1(data.hw1value)
                    //console.log(data.hw1value)
                    setUserhw2(data.hw2value)
                    setProjName(data.name)
                    setProjDescrip(data.description)
                }
            })



    }


    const send = (setType, chVal, inOut) => {
        //console.log(chVal)
        if (!(Number.isInteger(chVal)) && parseInt(chVal) <= 0 && (chVal.length >0)){
            setError("Quantity for HardwareSet must be integer greater than 0")
        }
         else
         {
            const sent = 
            {        
                method: "POST",
                headers: {'Content-Type': 'application/json',
                        'Accept': 'application/json'},
                body: JSON.stringify(
                    {id: currentProjId,
                    qty: parseInt(chVal),
                    hwsetname: setType,
                    username: globalUser,
                    check: inOut
                    
                })
            }
            fetch("/inorout", sent)
                .then(response => response.json())
                .then(data => {
                    //console.log(data.message);
                    if (data.message.trim() !== 'approved') {
                        setError(data.message)
                    } else {
                        setError("")
                        setQuantity1("")
                        setQuantity2("")
                        
                    }
                })



             //loadData()

        }

        

        

    }

    return (
        <div>
            <div className = 'navigationBar'>
                <Button variant="contained" onClick={()=>navigate('/dataaccess')} style = {{display: 'flex', position: 'fixed', bottom: 550, left: 25}}>Data Access</Button>
                <Button variant="contained" onClick={()=>navigate('/projects')} style = {{display: 'flex', position: 'fixed', bottom: 550, left: 200}}>Projects</Button>
                <h3 style = {{display: 'flex', position: 'fixed', bottom: 535, right: 200}}>{globalUser}</h3>
                <Button variant="contained" onClick={()=> {navigate('/'); setGlobalUser('Not Signed-In');}} style = {{display: 'flex', position: 'fixed', bottom: 550, right: 50}}>Sign Out</Button>
            </div>
            <h1>Resource Management</h1>

            <h3> Currently Working on Project: </h3>
            <h3> ID: {currentProjId} Name: {projName} Descrip: {projDescrip}</h3>

            <h3> ------------------------------------------- </h3>

            
             <div className = 'container' style = {{display : "block"}}>
                <h3 id = "HWSet1">HWSet1</h3>
                <TextField value = {capacity1} id="outlined-basic" label="Capacity" variant="outlined" onChange = {updateCapacity1}/>
                <TextField value = {availability1} id="outlined-basic" label="Available" variant="outlined" onChange = {updateAvailability1}/>
                {/* <TextField value = {quantity1} id="outlined-basic" label="Quantity" variant="outlined" onChange = {updateQuantity1}/> */}
            </div> 

            
            <div className = 'container' style = {{display : "block"}}>
                <h3 id = "HWSet2">HWSet2</h3>
                <TextField value = {capacity2} id="outlined-basic" label="Capacity" variant="outlined" onChange = {updateCapacity2}/>
                <TextField value = {availability2} id="outlined-basic" label="Available" variant="outlined" onChange = {updateAvailability2}/>
                {/* <TextField value = {quantity2} id="outlined-basic" label="Quantity" variant="outlined" onChange = {updateQuantity2}/> */}
            </div> 

            <div className = 'container' style = {{display : "block"}}>
                <h3 id = "HWSet1C">HWSet1 check in/out</h3>
                 <TextField value = {quantity1} id="outlined-basic" label="Quantity" variant="outlined" onChange = {updateQuantity1} />
                 <Button variant="contained"
                        onClick={() => send("hwset1", quantity1, "checkin")}>
                        Checkin
                </Button>
                <Button variant="contained"
                        onClick={() => send("hwset1", quantity1, "checkout")}>
                        CheckOut
                </Button>
            </div>

            <div className = 'container' style = {{display : "block"}}>
                <h3 id = "HWSet2C">HWSet2 check in/out</h3>
                 <TextField value = {quantity2} id="outlined-basic" label="Quantity" variant="outlined" onChange = {updateQuantity2} />
                 <Button variant="contained"
                        onClick={() => send("hwset2", quantity2, "checkin")}>
                        Checkin
                </Button>
                <Button variant="contained"
                        onClick={() => send("hwset2", quantity2, "checkout")}>
                        CheckOut
                </Button>
            </div> 

            <div className = 'container' style = {{display : "block"}}>
                <h3 id = "HWSetUser">{globalUser} Current hardware set values</h3>
                <h3> Hardware Set 1: {userhw1}</h3> {/* add the values here*/}
                <h3> Hardware set 2: {userhw2}</h3> 
                 
            </div>

            <div>
                <h3>
                    {errorMsg}
                </h3>
            </div>
        </div>
    );
}

export default ResourceManagement;
