import React, { useEffect, useState } from 'react';
import { useLocation, useNavigate, } from 'react-router-dom';
import { Button, Card, TextField, CardContent, CardActions, FormControl, Select,
    InputLabel, MenuItem } from '@mui/material';
import { ROOT_URL } from '../Constants';
import BasicDatePicker from './BasicDatePicker';

export default function Schedule() {
    const [amount, setAmount] = useState("");
    const [caption, setCaption] = useState("");
    const [startDate, setStartDate] = useState(new Date());
    const [endDate, setEndDate] = useState(new Date());
    const [frequency, setFrequency] = useState("");
    const [freqUnit, setFreqUnit] = useState("");
    const location = useLocation();
    // let navigate = useNavigate();
    // useEffect(() => {
    //     if (location.state === null) {
    //         console.log('ere');
    //         navigate("..", { replace: true });
    //         return;
    //     }
    // })
    const { username, display_name, profile_picture_url, id } = location.state;

    const date2UnixTime = date => {
        return parseInt((date.getTime() / 1000).toFixed(0));
    };

    const handleScheduleRequest = e => {
        // const userId = localStorage.getItem('userId');
        const userId = 1;
        if (!userId) {
            console.log("No userID");
            return;
        }
        let req_body = {
            "user_id": userId,
            "target_user_venmo_id": id,
            "text": caption,
            "start_date": date2UnixTime(startDate),
            "end_date": date2UnixTime(endDate),
            "frequency": frequency,
            "frequency_unit": freqUnit,
            "amount": amount
        };
        console.log(req_body);
        // fetch(ROOT_URL + "/login", {
        //         method: "POST",
        //         headers: {
        //             'Content-Type': 'application/json',
        //         },
        //         body: JSON.stringify(req_body)
        //         }
        //     ).then(response => {
        //         // if (response.status === NEED_OTP) {
        //         //     console.log(response.json());
        //         //     //redirect to the OTP page
        //         // } else {
        //         //     console.log("login successful");
        //         // }
        //     });
    }
    return (
        <Card variant="outlined" sx={{ width: 600, p:1 }} >
            <CardContent>
                <h2>{ display_name }</h2>
                <div className="space-between-container">
                    <TextField 
                        id="amount" 
                        type="number"
                        value={amount} 
                        onChange={((e) => setAmount(parseInt(e.target.value)))} 
                        label="Amount" 
                        placeholder="Enter amount"/>
                    <TextField 
                        id="caption" 
                        value={caption} 
                        onChange={((e) => setCaption(e.target.value))} 
                        label="What's it for?" 
                        placeholder="What's it for?"/>
                </div>
                
                <div className="space-between-container">
                    <BasicDatePicker 
                        fieldName="Start date"
                        handleDate={(date) => setStartDate(date)}/>
                    <BasicDatePicker 
                        fieldName="End date"
                        handleDate={(date) => setEndDate(date)}/>
                    <TextField 
                        id="frequency" 
                        type="number"
                        InputProps={{ inputProps: { min: 1 } }}
                        value={frequency} 
                        onChange={((e) => setFrequency(parseInt(e.target.value)))} 
                        label="Frequency" 
                        placeholder="Frequency"/>
                    <FormControl fullWidth>
                        <InputLabel id="freq-unit">How often?</InputLabel>
                        <Select
                            id="freq-unit"
                            value={freqUnit}
                            label="Unit"
                            onChange={(e) => setFreqUnit(e.target.value)}
                        >
                            <MenuItem value={"days"}>Days</MenuItem>
                            <MenuItem value={"months"}>Months</MenuItem>
                        </Select>
                    </FormControl>
                </div>
            </CardContent>
            <CardActions sx={{ display: "flex", flexDirection: "row" , justifyContent: "flex-end"}}>
                <Button 
                    variant="contained" 
                    size="medium" 
                    onClick={(e) => handleScheduleRequest(e)}>Request</Button>
            </CardActions>
        </Card>
    );
}