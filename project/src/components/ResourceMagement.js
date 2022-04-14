import React, {useState} from 'react';
import { Button, TextField } from '@mui/material';
import { useNavigate } from 'react-router-dom'


function ResourceManagement() {
    const navigate = useNavigate()

    const [errorMsg, setError] = useState("")

    const [capacity1, setCapacity1] = useState("")
    const [availability1, setAvailability1] = useState("")
    const [quantity1, setQuantity1] = useState("")

    const [capacity2, setCapacity2] = useState("")
    const [availability2, setAvailability2] = useState("")
    const [quantity2, setQuantity2] = useState("")

    const updateCapacity1 = (newCapacity) => {
        setCapacity1(newCapacity.target.value)
    }
    const updateCapacity2 = (newCapacity) => {
        setCapacity2(newCapacity.target.value)
    }

    const updateAvailability1 = (newAvailability) => {
        setAvailability1(newAvailability.target.value)
    }
     const updateAvailability2 = (newAvailability) => {
        setAvailability2(newAvailability.target.value)
    }

    const updateQuantity1 = (newQuantity) => {
        setQuantity1(newQuantity.target.value)
    }
    const updateQuantity2 = (newQuantity) => {
        setQuantity2(newQuantity.target.value)
    }

    const send = () => {
        const sent = {
            method: "POST",
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            },
            body: JSON.stringify(
                {
                    capacity1: capacity1, availability1: availability1, quantity1: quantity1,
                    capacity2: capacity2, availability2: availability2, quantity2: quantity2,
                })
        }

        if (parseInt(quantity1) <= 0) {
            setError("Quantity for HardwareSet1 must be greater than 0")

        } else if (parseInt(quantity2) <= 0) {
            setError("Quantity for HardwareSet2 must be greater than 0")
        } else {

            fetch("/logcheck", sent)
                .then(response => response.json())
                .then(data => {
                    console.log(data.message);
                    if (data.message.trim() !== 'approved') {
                        setError(data.message)
                    } else {
                        setCapacity1("")
                        setAvailability1("")
                        setQuantity1("")
                        setCapacity2("")
                        setAvailability2("")
                        setQuantity2("")
                        setError("")
                        navigate('/ResourceManagement')
                    }
                })

        }
    }

    return (
        <div>
            <h1>Resource Management</h1>

            <div className = 'container' style = {{display : "flex"}}>
                <h3 id = "HWSet1">HWSet1</h3>
                <TextField value = {capacity1} id="outlined-basic" label="Capacity" variant="outlined" onChange = {updateCapacity1}/>
                <TextField value = {availability1} id="outlined-basic" label="Available" variant="outlined" onChange = {updateAvailability1}/>
                <TextField value = {quantity1} id="outlined-basic" label="Quantity" variant="outlined" onChange = {updateQuantity1}/>
            </div>
            
            <div className = 'container' style = {{display : "flex"}}>
                <h3 id = "HWSet1">HWSet2</h3>
                <TextField value = {capacity2} id="outlined-basic" label="Capacity" variant="outlined" onChange = {updateCapacity2}/>
                <TextField value = {availability2} id="outlined-basic" label="Available" variant="outlined" onChange = {updateAvailability2}/>
                <TextField value = {quantity2} id="outlined-basic" label="Quantity" variant="outlined" onChange = {updateQuantity2}/>
            </div>
            
            <div className = 'managementButtons' style={{ display: 'flex', position: "fixed", bottom: 725}}>
                <Button variant="contained"
                        style = {{left: 277}}
                        onClick={send}>
                        Checkin
                </Button>
              
                <Button
                    variant="contained"
                    style = {{left: 288}}
                    onClick={send}>
                    Checkout
                </Button>
            </div>

            <div>
                <h3>
                    {errorMsg}
                </h3>
            </div>

            <div className = 'navigationButtons'>
                <Button variant="contained" onClick={()=>navigate('/projects')} style = {{display: 'flex', position: 'fixed', bottom: 500}}>Return To Projects</Button>
                <Button variant="contained" onClick={()=>navigate('/')} style = {{display: 'flex', position: 'fixed', bottom: 450}}>Sign Out</Button>
            </div>
            
        </div>
    );
}

export default ResourceManagement;