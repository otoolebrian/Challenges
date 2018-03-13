# Vigenere Cipher Challenge Code
#
# This script is used to create ciphertext from plaintext in a file
# and to decrypt ciphertext to plaintext using a user supplied key
# 
# Source code is available at https://github.com/otoolebrian/Challenges/

import sys
import re

# I will use the alphabet for encrypting and decrypting letters,
# I will also be able to use the alphabet to create the ciphertext
# TODO: Implement Number Handling and special chars handling
# Ignore these characters for the moment & jump over them in the 
# Cipher
ALPHABET='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Hardcode the password into the file, it might make it easier
# than having to remember to add a key at runtime. It's not in the
# top 24 passwords of the year, so that should be ok
# PASSWORD = Removed the password from here, it's not great to have
# it hardcoded, no matter how easy it makes it

def main():
	if(len(sys.argv) == 4):
		textfile = open(sys.argv[3], "r")
		text = textfile.read()
		if(len(text) == 0):
			print("No Data in Textfile")
			exit()
		else:

			# I don't want to worry about lowercase letters in the key
			# so I will just convert the key to uppercase
			key = sys.argv[3].upper()

			# I am also worried about memory usage, so I have decided to
			# only take the first 5 chars of the key. This still leaves a
			# potential keyspace of like nearly 12 million passwords
			# TODO: Any special chars in the key cause me issues, so strip
			# them out. When I implement number handling, I'll put it back in
			fixed_key = re.sub('[ !@#$%^&*123456789]', '', sys.argv[2])[:5]

	
			if(sys.argv[1] == 'e'):
				print(encrypt(fixed_key, text))
			elif(sys.argv[1] == 'd'):
				print(decrypt(fixed_key, text))
			else:
				print("Supported modes are e for encryption or d for decryption")
		
				exit()


	else:
		print('USAGE: ./crypto.py <mode:e|d> <key> <textfile> ')
		exit()

	return()


#Function to encrypt plaintext to ciphertext
def encrypt(key, message):
	cipher = []

	index=0

	#Loop through the message
	for char in message:
		num = ALPHABET.find(char.upper())
		
		#Check if it's a supported character, otherwise jump it		
		if num != -1:
			num += ALPHABET.find(key[index].upper())
			num %= len(ALPHABET)

			if char.isupper():
				cipher.append(ALPHABET[num])
			else:
				cipher.append(ALPHABET[num].lower())
		else:
			cipher.append(char)

		# Move on to the next part of the key, or go back to the 
		# start of the key if needed
		# We rotate through the key, even if the character is 
		# unencryptable. I'd say that's more secure. IDK. Probably?
		# TODO: Check if this is more secure???		
		index += 1
		if index == len(key):
			index = 0

	return ''.join(cipher)


#Function to decrypt ciphertext to plaintext
def decrypt(key, message):
	plaintext = []

	index=0

	#Loop through the message
	for char in message:
		num = ALPHABET.find(char.upper())
		
		#Check if it's a supported character, otherwise jump it		
		if num != -1:
			num -= ALPHABET.find(key[index].upper())
			num %= len(ALPHABET)

			if char.isupper():
				plaintext.append(ALPHABET[num])
			else:
				plaintext.append(ALPHABET[num].lower())
		else:
			plaintext.append(char)

		# Move on to the next part of the key, or go back to the 
		# start of the key if needed
		# Why are we rotating through the key? This is a terrible
		# idea
		# TODO: Tell the guy who wrote the encrypt function to change this	
		index += 1
		if index == len(key):
			index = 0

	return ''.join(plaintext)


if __name__ == '__main__':
	main()
