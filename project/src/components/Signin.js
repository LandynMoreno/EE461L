import React,{useState, useEffect} from 'react';
import { Button, TextField } from '@mui/material';
import { useNavigate } from 'react-router-dom'

function Signin() {
    const navigate = useNavigate()
    const [errorMsg, setError] = useState("initial error message")
    const [usernm, setUser] = useState("")
    const [pswd, setPswd] = useState("")

    const updateUser = (newUser) => {
        setUser(newUser.target.value)
        //console.log(usernm)
        
    }

    const updatePswd = (newPswd) => {
        setPswd(newPswd.target.value)
      
    }

    const send = () => {
        console.log("Sending")
        const sent = {
            method: "POST",
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({username: "TESTER"})
        }
        fetch("/logcheck",sent )
        .then(response => response.json())
        .then(data =>{
            //setError(data.approval);
            console.log(data.message);
          })
        
 
        

        //navigate('/projects')
    }


    return (
        <div>
            <h1>
                Username
            </h1>
            <TextField value = {usernm} d="outlined-basic" label="Username" variant="outlined" onChange={updateUser} />
            <h1>
                Password
            </h1>       
            <TextField value = {pswd} id="outlined-basic" label="Password" variant="outlined" onChange= {updatePswd} />
            <Button variant="contained" onClick={send} >Submit</Button>
            <Button variant="contained" onClick={()=>navigate('/newuser')}>New User????</Button>
            <h3> {errorMsg} </h3>


            
        </div>
    );
}

export default Signin;