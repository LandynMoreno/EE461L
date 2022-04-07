import React,{useState} from 'react';
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
            headers: {'Content-Type': 'application/json',
                    'Accept': 'application/json'},
            body: JSON.stringify(
                {username: "EXAMPLE USER",
                password: "EXAMPLE PASWRD"
            })
        }
        fetch("/logcheck",sent )
        .then(response => response.json())
        .then(data =>{
            console.log(data.message);
            if (data.message.trim() !== 'approved')
                {
                    setError(data.message)
                }
            else
            {
                navigate('/projects')
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
            <Button variant="contained" onClick={()=>navigate('/dataaccess')}>Data Access</Button>


            
        </div>
    );
}

export default Signin;