"""
"""

# Importing the required modules
try:
	from os import system, path, listdir, remove, chdir, mkdir
	from sys import platform, argv as arguments
except Exception as e:
	# If there are any errors during the importing of the modules, then we display the error on the console screen

	input(f'\n[ Error : {e} ]\nPress enter key to continue...')
	exit()

class Shell:
	def __init__(self):
		# Initially switching to the data/ directory as it is the default location for our shell
		if path.isdir('data/'):
			# If the data/ directory exists, then we directly switch to it

			chdir('data/')
		else:
			# If the data/ directory does not exists, then we first create it and then switch to it

			mkdir('data/')
			chdir('data/')
		
		# Setting the initial directory and the current working directory
		self.initialDirectory = path.dirname(path.abspath(__file__))
		self.currentWorkingDirectory = self.initialDirectory

		# Using a while true loop for infinite runtime of the shell, and would stop only if the user wants so
		while True:
			# The default shell prompt (It can be changed during thr runtime, if the user wants to)
			if self.currentWorkingDirectory == self.initialDirectory:
				# If the current working directory and the initial directory are same, then we donot display the working directory info on the shell prompt

				self.shellPrompt = 'wsb-shell:~$ '
			else:
				# If the current working directory and the initial directory are not same

				self.shellPrompt = f'wsb-shell:{self.currentWorkingDirectory}$'

			# Asking the user to enter a command
			self.command = input(f'{self.shellPrompt}')

			# Parsing and executing the command
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
			# If the user entered command is to exit the script, then we do it

			exit()
		elif token["command"] == 'list-files' or token["command"] == 'ls':
			# If the user entered command is to list the files and folders of the current directory, then we continue

			# Setting a blank variable for directory location
			directory = ''

			# Checking the user entered arguments
			if len(token["arguments"]) == 0:
				# If there are no arguments entered by the user, then we consider the current folder files to be listed

				directory = self.currentWorkingDirectory
			else:
				# If there are arguments entered by the user, then we consider the first argument to be the directory location

				directory = token["arguments"][0]

			# Checking if the specified directory exists or not
			if path.isdir(directory):
				# If the user specified directory exists, then we continue to list the files

				print(f'\nContents of "{directory} :')
				for i in listdir(directory):
					print(f'[*] {i}')
			else:
				# If the user specified directory does not exists, then we display an error message on the screen

				print(f'[ Error : No such directory "{directory}" ]')
				return 0
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
					# if i.isnumeric():
					# 	isNumber = True
					# else:
					# 	isNumber = False
					# 	break

					# Checking wheter numeric or not
					try:
						i = float(i)
					except ValueError:
						# If the value error is encountered, it means the argument is not a numeric term

						isNumber = False
						break
					except Exception as e:
						# If there are any other errors encountered during the process, then we display the error on the console screen

						print(f'[ Error : Failed to parse the arguments for the command "{token["command"]}" ]')
						return 0
					else:
						# If there are no errors in the process, then we assume that the argument is a numebr

						isNumber = True
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
