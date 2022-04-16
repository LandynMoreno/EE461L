import React,{useState} from 'react';
import { Button, TextField } from '@mui/material';
import { useNavigate } from 'react-router-dom'
//import LoginIcon from '@mui/icons-material/Login';


function Newuser({setGlobalUser, globalUser}) {
    const navigate = useNavigate()

    const [usernm, setUser] = useState("")
    const [pswd, setPswd] = useState("")
    const[error, setError] = useState("")

    const updateUser = (newUser) => {
        setUser(newUser.target.value)
        //console.log(usernm)
        
    }

    const updatePswd = (newPswd) => {
        setPswd(newPswd.target.value)
      
    }

    const send = () => {
        

        const sent = {        
            method: "POST",
            headers: {'Content-Type': 'application/json',
                    'Accept': 'application/json'},
            body: JSON.stringify(
                {username: usernm,
                password: pswd

            })
        }

        // const formData = new FormData();
        // formData.append('username', 'abc123');
        if(usernm.length < 3)
        {
            setError("username must be greater than 2 characters")

        }
        else if (pswd.length < 3)
        {
            setError("password length must be greater than 2 characters")
        }
        else{
            console.log("Sending");

        fetch("/adduser",sent )
        .then(response => response.json())
        .then(data =>{
            console.log(data.message);
            if (data.message.trim() !== 'approved')
                {
                    setError(data.message)
                }
            else
            {
                setGlobalUser(usernm)
                console.log(globalUser)
                setUser("")
                setPswd("")
                setError("")
                navigate('/projects')
            }
          })
               
        }

      
    }



    return (
        <div>
            <h1>New User? Make an account here :)</h1>
            <h1>
                Username
            </h1>
            <TextField value = {usernm} d="outlined-basic" label="Username" variant="outlined" onChange={updateUser} />
            <h1>
                Password
            </h1>       
            <TextField value = {pswd} id="outlined-basic" label="Password" variant="outlined" onChange= {updatePswd} />

            <div>
                <Button variant="contained" onClick={send}>Create Account</Button>
            </div>

            <div className = 'navigationButton'>
                <Button
                    variant="contained"
                    style = {{display: 'flex', position: 'fixed', bottom: 925}}
                    //startIcon={<LoginIcon/>}
                    onClick={()=>navigate('/')}>
                    Sign-In
                </Button>
            </div>

            <h3> {error} </h3>
            


            
        </div>
    );
}

export default Newuser;