import React, { useState } from 'react';
import Friend from './Friend';
import { List } from '@mui/material';

export default function FriendList(props) {
    const { friendList }  = props;

    return (
        <List>
            { friendList.map(friend => 
                <Friend username={ friend.username } 
                        display_name={ friend.display_name }
                        profile_picture_url={ friend.profile_picture_url }
                        id={ friend.id }
                        key={ friend.id } />
            ) }
        </List>
    );
}