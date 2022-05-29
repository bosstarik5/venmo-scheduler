import React, { useState } from 'react';
import { useLocation } from 'react-router-dom';
import { Button, Card, TextField, CardContent, CardActions } from '@mui/material';

export default function Schedule() {
    const [amount, setAmount] = useState(null);
    const location = useLocation();
    console.log(location);
    const { username, display_name, profile_picture_url, id } = location.state;

    const handleScheduleRequest = e => {
        console.log("requested " + amount);
    }
    return (
        <Card variant="outlined" sx={{ width: 600, p:1 }} >
            <CardContent className="name-amount">
                <h2>{ display_name }</h2>
                <TextField 
                    id="amount" 
                    value={amount} 
                    onChange={((e) => setAmount(e.target.value))} 
                    label="amount" 
                    placeholder="Enter amount"/>
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