import React, { useState } from 'react';
import FriendList from './FriendList';

export default function Home() {

    const friendList = [
        {
          "username": "random-name",
          "last_name": "Name",
          "friends_count": null,
          "is_group": false,
          "is_active": true,
          "trust_request": null,
          "phone": null,
          "profile_picture_url": "https://s3.amazonaws.com/venmo/no-image.gif",
          "is_blocked": false,
          "id": "5611330498099736263",
          "identity": null,
          "date_joined": "2017-12-31T23:50:17",
          "about": " ",
          "display_name": "Random Name",
          "first_name": "Random",
          "friend_status": "not_friend",
          "email": null
        }, 
        {
            "username": "random-name-2",
            "last_name": "Name",
            "friends_count": null,
            "is_group": false,
            "is_active": true,
            "trust_request": null,
            "phone": null,
            "profile_picture_url": "https://s3.amazonaws.com/venmo/no-image.gif",
            "is_blocked": false,
            "id": "99999999999999999",
            "identity": null,
            "date_joined": "2017-12-31T23:50:17",
            "about": " ",
            "display_name": "Random Name 2",
            "first_name": "Random",
            "friend_status": "not_friend",
            "email": null
          }
      ];

    return (
        <FriendList friendList={ friendList } />
    );
}