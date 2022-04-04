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
        const tosend = { usernm };
        const response = fetch("/logcheck", {
     
            // Adding method type
            method: "POST",
             
            // Adding body or contents to send
            body: JSON.stringify({
                title: "foo",
                body: "bar",
                userId: 1
            }),
             
            // Adding headers to the request
            headers: {
                "Content-type": "application/json; charset=UTF-8"
            }
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