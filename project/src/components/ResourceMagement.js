import React from 'react';
import { Button, TextField } from '@mui/material';
import { useNavigate } from 'react-router-dom'


function ResourceManagement({globalUser}) {
    const navigate = useNavigate()

    return (
        <div>
            <h1>Resource Management</h1>

            <div className = 'container' style = {{display : "flex"}}>
                <h3 id = "HWSet1">HWSet1</h3>
                <TextField id="outlined-basic" label="Capacity" variant="outlined"/>
                <TextField id="outlined-basic" label="Available" variant="outlined" />
            </div>
            
            <div className = 'container' style = {{display : "flex"}}>
                <h3 id = "HWSet1">HWSet2</h3>
                <TextField id="outlined-basic" label="Capacity" variant="outlined"/>
                <TextField id="outlined-basic" label="Available" variant="outlined" />
            </div>
            
            <div className = 'buttons' style={{ display: 'flex', position: "fixed", bottom: 725}}>
                <Button variant="contained" style = {{left: 277}}>Checkin</Button>
              
                <Button variant="contained" style = {{left: 288}}>Checkout</Button>
            </div>
            
        </div>
    );
}

export default ResourceManagement;