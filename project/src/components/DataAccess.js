import React, {useState, useEffect} from 'react';
import { Button,  } from '@mui/material';
import {Grid, } from '@mui/material'
import {useNavigate} from "react-router-dom";

//import LoginIcon from '@mui/icons-material/Login';

const metaData = [
    "Experiment I: Pressure data from 13 participants in 8 standard postures and 9 additional states, Experiment II: pressure data from 8 participants in 29 different states of 3 standard postures",
    "Ten young healthy adults (males, age of 27.6±3.7 years, one left-handed participant) were recruited for this study conducted in 2018 at University of Oklahoma, Translational Geroscience Laboratory",
    "Walking stride interval time series included are from 15 subjects: 5 healthy young adults (23 - 29 years old), 5 healthy old adults (71 - 77 years old), and 5 older adults (60 - 77 years old) with Parkinson's disease",
    "The study population consisted of 36 individuals. The 'young' population consisted of 20 individuals [Mean age = 21.0 (SD = 1.36 years)] and the 'old' population consisted of 16 individuals [Mean age = 50.0 (SD = 10.4 years)].",
    "Twenty-five subjects (21M, 4F) were selected (age: 50 ± 10 years, range 28-68 years; BMI: 31.6 ± 4.0 kg/m², range 25.1-42.5 kg/m²; AHI: 24.1 ± 20.3, range 1.7-90.9)."
]



function DataAccess({globalUser, setGlobalUser}) {
    const navigate = useNavigate()

    const [meta1, setmeta1] = useState("")
const [meta2, setmeta2] = useState("")
const [meta3, setmeta3] = useState("")
const [meta4, setmeta4] = useState("")
const [meta5, setmeta5] = useState("")

useEffect(() => {
    loadMeta();
  }, []);

const loadMeta = () => {


        const sent = {
            method: "POST",
            headers: {'Content-Type': 'application/json',
                    'Accept': 'application/json'},
            body: JSON.stringify(
                {link1: "https://physionet.org/content/pmd/1.0.0/",
                link2: "https://physionet.org/content/sleep-dep-hemo-cog/1.0.0/",
                link3: "https://physionet.org/content/gaitdb/1.0.0/" ,
                link4: "https://physionet.org/content/osv/1.0.0/",
                link5: "https://physionet.org/content/ucddb/1.0.0/"

            })
        }
        fetch("/apiaccess",sent )
            .then(response => response.json())
             .then(data =>{
                //console.log(data.message);
                if (data.message.trim() !== 'approved')
                    {
                        console.log(data.message)
                    }
                else
                {
                    // set the project ID here
                    setmeta1(data.meta1)
                    setmeta2(data.meta2)
                    setmeta3(data.meta3)
                    setmeta4(data.meta4)
                    setmeta5(data.meta5)
                }
            })


}



    return (
        <div>
            <div className = 'navigationBar'>
                <Button variant="contained" onClick={()=>navigate('/projects')} style = {{display: 'flex', position: 'fixed', bottom: 550, left: 25}}>Projects</Button>
                {/* <Button variant="contained" onClick={()=>navigate('/ResourceManagement')} style = {{display: 'flex', position: 'fixed', bottom: 550, left: 200}}>Resource Management</Button> */}
                <h3 style = {{display: 'flex', position: 'fixed', bottom: 535, right: 200}}>{globalUser}</h3>
                <Button variant="contained" onClick={()=> {navigate('/'); setGlobalUser('Not Signed-In');}} style = {{display: 'flex', position: 'fixed', bottom: 550, right: 50}}>Sign Out</Button>
            </div>
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
                    <h2> {meta1} </h2>
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
                    <h2> {meta2}</h2>
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
                    <h2>Jeffrey Hausdorff</h2>
                </Grid>

                <Grid item lg={4}>
                    <h2> {meta3}</h2>
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
                    <h2>Amar S. Bhogal</h2>
                </Grid>

                <Grid item lg={4}>
                    <h2> {meta4}</h2>
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
                    <h2>Conor Heneghan</h2>
                </Grid>

                <Grid item lg={4}>
                    <h2> {meta5} </h2>
                </Grid>

                <Grid item lg={2}>
                <a href="https://physionet.org/static/published-projects/ucddb/st-vincents-university-hospital-university-college-dublin-sleep-apnea-database-1.0.0.zip"
                    download
                    >
                        Click to download zip
                    </a>
                </Grid>

            </Grid>

            <div className = 'navigationButton'>
                <Button
                    variant="contained"
                    style = {{display: 'flex', position: 'fixed', bottom: 925}}
                    //startIcon={<LoginIcon/>}
                    onClick={()=>navigate('/')}>
                    Sign-In
                </Button>
            </div>
            
        </div>
    );
}

export default DataAccess;
