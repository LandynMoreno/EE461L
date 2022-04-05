import React,{useState, useEffect} from 'react';
import { Button, TextField } from '@mui/material';
import { useNavigate } from 'react-router-dom'


function Newuser() {
    const navigate = useNavigate()

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
            body: JSON.stringify(
                {username: usernm,
                password: pswd
            })
        }
        fetch("/adduser",sent )
        .then(response => response.json())
        .then(data =>{
            console.log(data.message);
          })
               

        //navigate('/projects')
    }



    return (
        <div>
            <h1>New User? make here :)</h1>
            <h1>
                Username
            </h1>
            <TextField value = {usernm} d="outlined-basic" label="Username" variant="outlined" onChange={updateUser} />
            <h1>
                Password
            </h1>       
            <TextField value = {pswd} id="outlined-basic" label="Password" variant="outlined" onChange= {updatePswd} />
            <Button variant="contained" onClick={send} >Login</Button>
            


            
        </div>
    );
}

export default Newuser;