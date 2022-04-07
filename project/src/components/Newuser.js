import React,{useState} from 'react';
import { Button, TextField } from '@mui/material';
import { useNavigate } from 'react-router-dom'


function Newuser() {
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
        console.log("Sending")

        // const formData = new FormData();
        // formData.append('username', 'abc123');

        // fetch('adduser', {
        // method: 'PUT',
        // body: formData
        // })
        // .then(response => response.json())
        // .then(result => {
        // console.log('Success:', result);
        // })
        // .catch(error => {
        // console.error('Error:', error);
        // });


        const sent = {
            method: "POST",
            headers: {'Content-Type': 'application/json',
                    'Accept': 'application/json'},
            body: JSON.stringify(
                {username: "EXAMPLE USER",
                password: "EXAMPLE PASWRD"
            })
        }
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
                navigate('/projects')
            }
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
            <h3> {error} </h3>
            


            
        </div>
    );
}

export default Newuser;