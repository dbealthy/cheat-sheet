
Users and their hashed passwords are stored in `/etc/passwd`

- Create a new user
> `sudo useradd -s /bin/bash -m -c "Mary Quinn" -Gsambashare maryq`

The command is composed of:

- **sudo**: We need administrator privileges to allow a new user to access the computer.
- **useradd**: The `useradd` command.
- **-s /bin/bash**: The shell option. This sets the default shell for this new user.
- **-m**: The make home directory option. This creates a directory in the “/home/” directory, with the same name as the new user account name.
- **-c “Mary Quinn”**: The full name of the new user. This is optional.
- **-Gsambashare**: The additional group option. This is optional. The new user is added to a group with the same name as their account name. The `-G` option (note, capital “G”) adds the user to supplementary groups. The groups must already exist. We’re also making the new user a member of the “sambashare” group.
- **maryq**: The name of the new user account. This must be unique. It cannot already be in use for another user.

- Set password for a user 
>`sudo passwd maryq`

- Remove a user
> `userdel username`

- List all connected users
> `who`
> `users`

- List all users
> `cat /etc/passwd`
![[list-users-linux-768x415.png |500]]

## User types

### Root
root (**uid: 0**)
root user doesn't have any constrains

### Not Root (user)
Can be divided into (just for understanding. Linux approches them the same):
- Daemons - users on behalf of which services run
- Usual users (people)

daemons (uid: != 0 & < 1000) uid untill 1000
user (uid: 1000) uid usually starts from 1000
