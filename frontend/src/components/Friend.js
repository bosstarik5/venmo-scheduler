import { ListItemButton, ListItemAvatar, Avatar, ListItemText } from '@mui/material';
import React, { useState } from 'react';
import { useNavigate } from "react-router-dom";

export default function Friend(props) {
    const { username, display_name, profile_picture_url, id } = props;
    let navigate = useNavigate();

    async function handleFriendClick(e) {
        e.preventDefault();
        console.log("click friend with id= " + id);
        navigate("schedule", { state: props } );
    }

    return (
        <ListItemButton
          onClick={ e => handleFriendClick(e) }
        >
            <ListItemAvatar>
                <Avatar alt={ display_name } src={ profile_picture_url } />
            </ListItemAvatar>
            <ListItemText primary={ display_name } />
        </ListItemButton>
    );


}