#!/usr/bin/python3
#  Nepali Custom Password Generator
#
#  <NCPG>  Copyright (C) <2019>  <Hemanta Pokharel>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.

# Check if configuration file exists or not!!!
from Core.config import *
check_config()

# Check whether there is any error in configuration file or not!!!
try:
	read_config()
except Exception:
	reset_config()

import platform , os , shutil
from pathlib import Path
from Core.managefile import count
from termcolor import colored
from Core.banners import banner
from Core.dictionary import dictionary
from Core.text import *
from Core.colour import *
from Core.interactive import *
from Core.func import *
from Core.ph_num import *


# Clean terminal and ask option...
osys = platform.system()
clean_terminal()
banner()
home_text()
option_main()   

opt = input(colored(color.bold + "\nncpg> ","cyan"))

while opt not in ("1","2","3","4","5"):
	clean_terminal()
	banner()
	home_text()
	option_main()
	opt = input(colored(color.bold + "\nncpg> ","cyan"))


while opt in ('2','3','4','5'):
	
	# Help and about
	if opt == "4":
		opt_help_about()
		opt = input(colored(color.bold + "\nncpg> ","cyan")).lower()
	
	# Exit
	elif opt == "5":
		exitt()
	
	# Edit and Reset configuration file
	elif opt == "2":
		text_config()
		opt2 = input(colored(color.bold + "\nncpg> ","cyan")).lower()
		
		while opt2 not in ("1","2","3"):
			clean_terminal()
			banner()
			home_text()
			text_config()
			opt2 = input(colored(color.bold + "\nncpg> ","cyan"))
		
		# Edit configuration
		if opt2 == "1":
			if osys == "Linux":
				os.system("x-terminal-emulator -e 'nano config.ini'")
			else:
				pass
		
		# Reset configuration
		elif opt2 == "2":
			reset_config()
			clean_terminal()
			banner()
			home_text()
			text_reset_conf()

		#Back
		elif opt2 == "3":
			pass
			
		clean_terminal()
		banner()
		home_text()
		option_main()
		opt = input(colored(color.bold + "\nncpg> ","cyan")).lower()
		
	#Install and uninstall
	elif opt == "3" :
		clean_terminal()
		banner()
		home_text()
		text_install()
		opt3 = input(colored(color.bold + "\nncpg> ","cyan"))
		
		while opt3 not in ("1","2","3"):
			clean_terminal()
			banner()
			home_text()
			text_install()
			opt3 = input(colored(color.bold + "\nncpg> ","cyan"))
		
		# Install
		if opt3 == "1":
			if osys == "Linux":
				os.system("x-terminal-emulator -e 'sudo bash install.sh --install'")
			else:
				pass
		
		# Uninstall
		elif opt3 == "2":
			if osys == "Linux":
				os.system("x-terminal-emulator -e 'sudo bash install.sh --uninstall'")
			else:
				pass
		
		elif opt3 == "3":
			pass
			
		clean_terminal()
		banner()
		home_text()
		option_main()
		opt = input(colored(color.bold + "\nncpg> ","cyan"))
		opt = opt.lower()
		
	while opt not in ("1","2","3","4","5"):
		clean_terminal()
		banner()
		home_text()
		option_main()
		opt = input(colored(color.bold + "\nncpg> ","cyan"))

# Generate Password...

if opt == "1":
	clean_terminal()
	banner()
	read_config()
	# Interactive Mode!!!
	is_interactive = input("Do you know any information about victim? Y/[N]: ").lower()
	if is_interactive in ('yes','y'):
		clean_terminal()
		banner()
		interactive()

# Removing old temporary files and making new one...
if is_interactive not in ('yes','y'):
		if os.path.exists('.Temporary Files'):
			shutil.rmtree('.Temporary Files')
		os.makedirs('.Temporary Files')

# Dictionary Mode
dictionary()
dic_int_count = count('.Temporary Files/Wordlists') # Counting words from dictionary and interactive mode...

# Start Phone number mode if atleast one telecom is made True...
count = 0
ph = ['ntc','ncell','sky','smart cell','utl','hello mobile']
for i in ph:
	if CONFIG[i] in ('true','True'):
		count = count + 1

if count > 0 :
	# Check either crunch is installed or not 
	install_crunch()

	# Phone number mode
	phone_num()

# Show result
clean_terminal()
banner()
home = str(Path.home())
print('\n[RESULT]')

# Remove old directory if exists...
if os.path.isdir('Generated Passwords - NCPG') == True:
	shutil.rmtree('Generated Passwords - NCPG')
if os.path.isdir( home + '/Generated Passwords - NCPG') == True:
	shutil.rmtree(home + '/Generated Passwords - NCPG')

print('\n[+] Making Directory on Home.')
print('[+] Saving dictionary on ' + colored(home,'red')  + colored("/'Generated Passwords - NCPG'",'red'))
os.rename('.Temporary Files','Generated Passwords - NCPG')  # Renaming into Generated Passwords - NCPG
os.system("mv 'Generated Passwords - NCPG' " + home   )     # Moving into Home directory

print('[+] Counting passwords from Interactive and Dictionary mode : ' + str(dic_int_count)) 
print(colored('\nTest Your Luck With The Wordlists. Goodluck!!! ','cyan')) 

# (¬‿¬)
