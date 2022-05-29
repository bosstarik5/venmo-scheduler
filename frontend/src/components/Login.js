import { Button, Card, TextField, CardContent, CardActions } from '@mui/material';
import React, { useState } from 'react';

const ROOT_URL = "http://localhost:5000/api";
const NEED_OTP = 401;

export default function Login() {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");

    const handleLogin = (e, username, password) => {
        let req_body = {
            "username": username,
            "password": password
        };
        fetch(ROOT_URL + "/login", {
                method: "POST",
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(req_body)
                }
            ).then(response => {
                if (response.status === NEED_OTP) {
                    console.log(response.json());
                    //redirect to the OTP page
                } else {
                    console.log("login successful");
                }
            });
    };

    return (
        <div className="login">
            <Card variant="outlined" sx={{ maxWidth: 300, p:1 }}>
                <CardContent>
                    <TextField id="username" value={username} onChange={((e) => setUsername(e.target.value))} label="username" placeholder='Enter Username'/>
                    <TextField id="password" value={password} onChange={((e) => setPassword(e.target.value))} label="password" placeholder='Enter Password'/>
                </CardContent>
                <CardActions sx={{ display: "flex", flexDirection: "column" }}>
                    <Button variant="contained" size="medium" onClick={(e) => handleLogin(e, username, password)}>Login</Button>
                </CardActions>
            </Card>
        </div>
    );
}