### Users
| type       | char |
| ---------- | ---- |
| owner      | u    |
| file group | g    |
| other      | o    |
| all        | a    |

### Permissions

| type    | char | digit |
| ------- | ---- | ----- |
| read    | r    | 4     |
| write   | w    | 2     |
| execute | x    | 1     |


Permisions are given to:	
![[Promisions1.png|500]]
1. Owner of a file (creator)
2. Owner group
3. Other users

## Change permissions
To add permisions to a file use '+' sign and '-' to remove.

`sudo chmode a+x filename`
give all users execution access to this file

## Check file permissions
> `ls -l`

