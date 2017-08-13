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
    #FIXME:  This function needs a good docstring
    """
    users = { } # we want a dictionary with the key being the username and the ssh-key being the value
    on_username = True # true because we expect to start file on a username
    cur_user = "" # used for saving the current username between line iterations

    for line in users_file:
        if on_username:
            cur_user = line.strip()
            on_username = False
        else:
            users[cur_user] = line.strip()
            on_username = True

def generate_output_block(username, ssh_key):
    """
    This function generates the raw output of one user, returns chunk of
    plaintext to be put directly into the init.pp file
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
    count_codes(users_file)


if __name__ == "__main__":
    main( )
