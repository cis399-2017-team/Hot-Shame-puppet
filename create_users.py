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
    users = [ ]

    for line in users_file:
        users.append(line.strip())

def generate_output_block(user):
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
                        help="A text file containing usernames and ssh keys, one username followed by ssh-key on following file, next user is separated by a empty line.")
    args = parser.parse_args()  # gets arguments from command line
    users_file = args.users
    count_codes(users_file)


if __name__ == "__main__":
    main( )
