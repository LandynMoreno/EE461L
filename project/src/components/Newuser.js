import React from 'react';
import { Button, TextField } from '@mui/material';

function Newuser() {
    return (
        <div>
            <h1>New User? make here :)</h1>
            <h1>
                Username
            </h1>
            <TextField id="outlined-basic" label="Username" variant="outlined" />
            <h1>
                Password
            </h1>
            <TextField id="outlined-basic" label="Password" variant="outlined" />
            <Button variant="contained">Login</Button>
            


            
        </div>
    );
}

export default Newuser;