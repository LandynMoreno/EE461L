import React from 'react';
import { Button, TextField } from '@mui/material';
import {Grid, Link} from '@mui/material'

function DataAccess() {
    return (
        <div>
            <h1>DataAccess</h1>
            <Grid container rowSpacing={1} columnSpacing={1} background='primary'>
                <Grid item lg={4}>
                    <h1> Title of dataset (Link embedded)</h1>
                </Grid>
                <Grid item lg={2}>
                    <h1> Author </h1>
                </Grid>
                <Grid item lg={4}>
                    <h1> Meta Data</h1>
                </Grid>
                <Grid item lg={2}>
                    <h1> Zip download</h1>
                </Grid>

                <Grid item lg={4}>
                    <a href="https://physionet.org/content/pmd/1.0.0/" target="_blank">A Pressure Map for In-bed Postures</a>
                </Grid>

                <Grid item lg={2}>
                    <h2>M. Baran Pouyan</h2>
                </Grid>

                <Grid item lg={4}>
                    <h4> * 679 Experimental Datasets</h4>
                    <h4> * 29 Air Mat Experiemtns</h4>
                </Grid>

                <Grid item lg={2}>
                <a href="https://physionet.org/static/published-projects/pmd/a-pressure-map-dataset-for-in-bed-posture-classification-1.0.0.zip"
                    download
                    >
                        Click to download zip
                    </a>
                </Grid>

                <Grid item lg={4}>
                    <a href="https://physionet.org/content/sleep-dep-hemo-cog/1.0.0/" target="_blank">Effect of 24-Hour Sleep Deprivation on Cognitive Performance</a>
                </Grid>

                <Grid item lg={2}>
                    <h2>P. Mukli</h2>
                </Grid>

                <Grid item lg={4}>
                    <h2> Meta Data</h2>
                </Grid>

                <Grid item lg={2}>
                <a href="https://physionet.org/static/published-projects/sleep-dep-hemo-cog/effect-of-24-hour-sleep-deprivation-on-cerebral-hemodynamics-and-cognitive-performance-1.0.0.zip"
                    download
                    >
                        Click to download zip
                    </a>
                </Grid>

                <Grid item lg={4}>
                    <a href="https://physionet.org/content/gaitdb/1.0.0/" target="_blank">Gait in Aging and Disease Database</a>
                </Grid>

                <Grid item lg={2}>
                    <h2>A. Goldberger</h2>
                </Grid>

                <Grid item lg={4}>
                    <h2> Meta Data</h2>
                </Grid>

                <Grid item lg={2}>
                <a href="https://physionet.org/static/published-projects/gaitdb/gait-in-aging-and-disease-database-1.0.0.zip"
                    download
                    >
                        Click to download zip
                    </a>
                </Grid>


                <Grid item lg={4}>
                    <a href="https://physionet.org/content/osv/1.0.0/" target="_blank">Pattern Analysis of Oxygen Saturation Variability</a>
                </Grid>

                <Grid item lg={2}>
                    <h2>L. Amaral</h2>
                </Grid>

                <Grid item lg={4}>
                    <h2> Meta Data</h2>
                </Grid>

                <Grid item lg={2}>
                <a href="https://physionet.org/static/published-projects/osv/pattern-analysis-of-oxygen-saturation-variability-1.0.0.zip"
                    download
                    >
                        Click to download zip
                    </a>
                </Grid>

                <Grid item lg={4}>
                    <a href="https://physionet.org/content/ucddb/1.0.0/" target="_blank">
                        St. Vincent's University Hospital / University College Dublin Sleep Apnea Database
                    </a>
                </Grid>

                <Grid item lg={2}>
                    <h2>L. Glass</h2>
                </Grid>

                <Grid item lg={4}>
                    <h2> Meta Data</h2>
                </Grid>

                <Grid item lg={2}>
                <a href="https://physionet.org/static/published-projects/ucddb/st-vincents-university-hospital-university-college-dublin-sleep-apnea-database-1.0.0.zip"
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