# CIS399 Final Project

This is our final project for CIS399 system administration.  The program takes a list of users and keys and creates puppet modules for each user.

## Getting Started


### Prerequisites

You will need Python3.x and puppet2.7.25 to be installed.  If you wish to create admin users, you will need to already have an admin group set up.

### Installing

To install, drop the python script in the root directory of your puppet installation.  

## Running the program

The script takes a file of users and keys with each being on its own line.

```
username
key
username2
key2
```
There is also an option ```[--Admin | -A]``` to create admin users.  This will add the users to the admin group.

To run simply execute:
```
python3 create_users.py [-A] user_file.txt
```

## Future Plans

In the future we would like to support adding users to which ever group you like.  The program could also create the group, if it is not already created.

## Authors

* **Holden Oullette**
* **James Dolan** 



