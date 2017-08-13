"""
Count the number of occurrences of each major code in a file.
Authors: Holden Oullette, James Dolan
Credits: #FIXME

Input is a file(s)

Output is a
"""

import argparse

def parse_users(users_file):
    """
    Parses users from users_file
    """
    global users = { } # we want a dictionary with the key being the username and the ssh-key being the value
                        # assigned globally so we can access it in other functions and we can guarantee parse_users will be called
    on_username = True # true because we expect to start file on a username
    cur_user = "" # used for saving the current username between line iterations

    for line in users_file:
        if on_username:
            cur_user = line.strip()
            on_username = False
        else:
            users[cur_user] = line.strip()
            on_username = True

def generate_output():
    """
    This function generates the raw output of ALL users, writes to init.pp file
    """

def generate_output_block(username, ssh_key):
    """
    This function generates the raw output of ONE user, returns chunk of
    plaintext to be put directly into the init.pp file
    """

def establish_file_structure():
    """
    This function checks for the existence of file structure for the users module,
    if it exists, it will simply update the file, if not, it will make the proper folders.
    It assumes script will run in proper location (i.e. Puppet root directory)
    """

def main( ):
    """
    Interaction if run from the command line.
    Usage:  python3 create_users.py  username_keyfile_list.txt
    """
    parser = argparse.ArgumentParser(description="Create a user module file containing all user information")
    parser.add_argument('users', type=argparse.FileType('r'),
                        help="A text file containing usernames and ssh keys, one username followed by ssh-key on following file.")
    args = parser.parse_args()  # gets arguments from command line
    users_file = args.users
    parse_users(users_file)


if __name__ == "__main__":
    main( )
