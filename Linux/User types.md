There are two main types of users: root, not root

### Root
root (**uid: 0**)
root user doesn't have any constrains

### Not Root (user)
Can be divided into (just for understanding. Linux approches them the same):
- Daemons - users on behalf of which services run
- Usual users (people)

daemons (uid: != 0 & < 1000) uid untill 1000
user (uid: 1000) uid usually starts from 1000
