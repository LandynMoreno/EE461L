import React from 'react';
import { Button, TextField } from '@mui/material';
import {Grid, Link} from '@mui/material'

function DataAccess() {
    return (
        <div>
            <h1>DataAccess</h1>
            <Grid container rowSpacing={1} columnSpacing={1} background='primary'>
                <Grid item xs={2}>
                    <a href="https://www.linkedin.com/in/mike-hildner/" target="_blank">My linkedin link</a>
                    {/* <Link href='#' color='primary' underline='always'>
                        {"Your link"}
                    </Link> */}
                </Grid>
                <Grid item xs={5}>
                    <h2>metaData</h2>
                </Grid>
                <Grid item xs={5}>
                <a href="https://physionet.org/static/published-projects/aftdb/af-termination-challenge-database-1.0.0.zip"
                    download
                    >
                        Click to download zip
                    </a>
                </Grid>
                <Grid item xs={2}>
                    <a href="https://www.linkedin.com/in/mike-hildner/" target="_blank">My linkedin link</a>
                    {/* <Link href='#' color='primary' underline='always'>
                        {"Your link"}
                    </Link> */}
                </Grid>
                <Grid item xs={5}>
                    <h2>metaData</h2>
                </Grid>
                <Grid item xs={5}>
                    <a href="https://physionet.org/static/published-projects/adfecgdb/abdominal-and-direct-fetal-ecg-database-1.0.0.zip"
                    download
                    >
                        Click to download zip
                    </a>
                </Grid>
            </Grid>

            {/* <h1>New User? make here :)</h1>
            <h1>
                Username
            </h1>
            <TextField id="outlined-basic" label="Username" variant="outlined" />
            <h1>
                Password
            </h1>
            <TextField id="outlined-basic" label="Password" variant="outlined" />
            <Button variant="contained">Login</Button> */}
            
            
        </div>
    );
}

export default DataAccess;