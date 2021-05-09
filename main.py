"""
"""

# Importing the required modules
try:
	from os import system, path
	from sys import platform, argv as arguments
except Exception as e:
	# If there are any errors during the importing of the modules, then we display the error on the console screen

	input(f'\n[ Error : {e} ]\nPress enter key to continue...')
	exit()

class Shell:
	def __init__(self):
		while True:
			self.shellPrompt = 'wsb-shell~$ '
			self.command = input(f'{self.shellPrompt}')
			token = self.commandParser()
			self.executeCommand(token)

	def commandParser(self):
		""" """

		# The token which is a dictionary item, it contains the main command, as well as the arguments for the command
		token = {
		"command" : "",
		"arguments" : [],
		}

		# Setting the command to the token
		token["command"] = self.command.split(' ')[0].lower()

		# Setting the rest of the arguments from the command input
		for i in self.command.split(' ')[1:]: token["arguments"].append(i)
		return token

	def executeCommand(self, token):
		""" """

		# Executing the requested command on the basis of the token
		if token["command"] == '':
			# If the command is blank, then we skip the line

			pass
		elif token["command"] == 'exit':
			# If the user command is to exit the script, then we do it

			exit()
		elif token["command"] == 'add':
			# If the user command is to add, then we continue

			# Checking for the numeric arguments if exists
			if len(token["arguments"]) == 0:
				# If there are no arguments entered by the user

				print('[ add : requires arguments, use add --help for more info ]')
			else:
				# If there are atleast more than 0 arguments entered by the user

				isNumber = False
				for i in token["arguments"]:
					if i.isnumeric():
						isNumber = True
					else:
						isNumber = False
						break
				if isNumber:
					# If the arguments are all numbers, then we continue to find out the sum

					result = 0
					for number in token["arguments"]:
						result += float(number)
					print(result)
				else:
					# If the arguments are not all numbers, then we continue to create a new file

					filename = token["arguments"][0]
					if filename.lower() == '--help':
						# If the user entered argument for displaying the help for the command, then here we go

						self.help(token["command"])
					else:
						choice = input('Creating a new file - Enter N to cancel : ')
						if choice.lower() == 'no' or choice.lower() == 'n':
							return 0
						else:
							open(f'data/{filename}', 'w+').write('')
							print(f'[ File created : {filename} ]')

		else:
			# If the user entered command is unrecognized, then we display an error on the console screen

			print(f'[ Command not recognized : {self.command.split(" ")[0]} ]')

	def help(self, command):
		""" """

		print(f'Help info for command : {command}')

if __name__ == '__main__':
	try:
		shell = Shell()
	except KeyboardInterrupt:
		# If the user presses CTRL+C key combo, then we exit the script

		exit()
	except Exception as e:
		# If there are any errors during the process, then we display the error on the console screen

		print(f'[ Error {e} ]')
