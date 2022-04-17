import React,{useState} from 'react';
import { Button, TextField } from '@mui/material';
import { useNavigate } from 'react-router-dom'

function Signin({setGlobalUser, globalUser}) {
    const navigate = useNavigate()
    const [errorMsg, setError] = useState("")
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
        console.log(usernm)
        console.log(pswd)
        const sent = {
            method: "POST",
            headers: {'Content-Type': 'application/json',
                    'Accept': 'application/json'},
            body: JSON.stringify(
                {username: usernm,
                password: pswd
            })
        }

        if(usernm.length < 3)
        {
            setError("username must be greater than 2 characters")

        }
        else if (pswd.length < 3)
        {
            setError("password length must be greater than 2 characters")
        }
        else{
            console.log("sending")
        
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
                
                //setUser("")
                setGlobalUser(usernm)
                setPswd("")
                setError("")          
                navigate('/projects')
            }
          })
        
        }
 
        

        //navigate('/projects')
    }


    return (
        <div>
            <h1>
                Username
            </h1>
            <TextField value = {usernm} id="outlined-basic" label="Username" variant="outlined" onChange={updateUser} />
            <h1>
                Password
            </h1>       
            <TextField value = {pswd} id="outlined-basic" label="Password" variant="outlined" onChange= {updatePswd} />
            <div>
                <Button variant="contained" onClick={send} >Sign-In</Button>
            </div>
            <div>
                <h1> </h1>
                <h3> {errorMsg} </h3>
                <Button variant="contained" onClick={()=>navigate('/newuser')}>Create an Account</Button>
            </div>
            
        </div>
    );
}

export default Signin;
