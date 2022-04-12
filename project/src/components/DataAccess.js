import React from 'react';
import { Button, TextField } from '@mui/material';
import {Grid, Link} from '@mui/material'

function DataAccess() {
    return (
        <div>
            <h1>DataAccess</h1>
            <Grid container rowSpacing={1} columnSpacing={1} background='primary'>
                <Grid item xs={4}>
                    <h1> Title of dataset (Link embedded)</h1>
                </Grid>
                <Grid item xs={2}>
                    <h1> Author </h1>
                </Grid>
                <Grid xs={4}>
                    <h1> Meta Data</h1>
                </Grid>
                <Grid item xs={2}>
                    <h1> Zip download</h1>
                </Grid>

                <Grid item xs={4}>
                    <a href="https://physionet.org/content/pmd/1.0.0/" target="_blank">A Pressure Map for In-bed Postures</a>
                </Grid>

                <Grid item xs={2}>
                    <h2>M. Baran Pouyan</h2>
                </Grid>

                <Grid item xs={4}>
                    <h2> Meta Data</h2>
                </Grid>

                <Grid item xs={2}>
                <a href="https://physionet.org/static/published-projects/pmd/a-pressure-map-dataset-for-in-bed-posture-classification-1.0.0.zip"
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