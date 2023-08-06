Groups and associated users are stored in  `/etc/group`

- Create a new group
> `groupadd groupname`

- Add user to an existing group
> `usermod -a -G groupname username`

- Change user's primary group (associated files)
> `usermod -g groupname username`

- View groups a user is assigned to
> `groups`
> `groups username`

- Remove user from a group
> `gpasswd -d username groupname`

- Remove a group
> `groupdel groupname`

- List all groups
>`cat /etc/group`


![[etc-group-file-768x461.png |500]]