import React from 'react';
import { Button, TextField } from '@mui/material';
import { useNavigate } from 'react-router-dom'

function Signin() {
    const navigate = useNavigate()


    return (
        <div>
            <h1>
                Username
            </h1>
            <TextField id="outlined-basic" label="Username" variant="outlined" />
            <h1>
                Password
            </h1>
            <TextField id="outlined-basic" label="Password" variant="outlined" />
            <Button variant="contained">Submit</Button>
            <Button variant="contained" onClick={()=>navigate('/newuser')}>New User????</Button>


            
        </div>
    );
}

export default Signin;