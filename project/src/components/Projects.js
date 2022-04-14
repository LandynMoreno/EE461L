import React from 'react';
import { Button, TextField } from '@mui/material';
import { useNavigate } from 'react-router-dom'

function Projects() {
    const navigate = useNavigate()


    return (
        <div>
            <h1>
                Projects Page
            </h1>
            <p>Create New Project</p>
            <TextField id="outlined-basic" label="Project Name" variant="outlined" />
            <TextField id="outlined-basic" label="Project Description" variant="outlined" />
            <TextField id="outlined-basic" label="ProjectID" variant="outlined" />
            <Button variant="contained" onClick={()=>navigate('/ResourceManagement')}>Create</Button>

            <p>Use existing Project</p>
            <TextField id="outlined-basic" label="ProjectID" variant="outlined" />
            <Button variant="contained" onClick={()=>navigate('/ResourceManagement')}>Access Project</Button>

            
        </div>
    );
}

export default Projects;