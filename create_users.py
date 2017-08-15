"""
Count the number of occurrences of each major code in a file.
Authors: Holden Oullette, James Dolan
Credits: #FIXME

Input is a file(s)

Output is a
"""

import argparse

users = { }

def parse_users(users_file):
	"""
	Parses users from users_file
	"""
	#global users = { } # we want a dictionary with the key being the username and the ssh-key being the value
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
	with open('test.txt', 'w') as f:
		# Start the beginning of the init.pp file
		f.write("class users {\n")
		for username, ssh_key in users.items():
			f.write('\tuser { "%s":\n' % str(username))
			f.write('\t\thome => "/home/%s",\n' % str(username))
			f.write('\t\tmanagehome => true,\n')
			f.write('\t\tpassword => "!",\n')
			f.write('\t\tpassword_max_age => "99999",\n')
			f.write('\t\tpassword_min_age => "0",\n\t}\n')
			f.write('\tssh_authorized_key { "%s-key-pair-oregon":\n' % str(username))
			f.write('\t\tuser => "%s",\n' % str(username))
			f.write('\t\ttype => "ssh-rsa",\n')
			f.write('\t\tkey => "%s"\n\t}\n' % str(ssh_key))
		f.write("}")

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
	generate_output()


if __name__ == "__main__":
	main( )