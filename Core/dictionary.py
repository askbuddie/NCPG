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

import os
from Core.managefile import *
from Core.config import *
from Core.func import clean_terminal
from Core.banners import banner

read_config()

def dictionary_mode(file1):
	clean_terminal()
	banner()
	print('\n[DICTIONARY MODE]\n')
	manage_file(file1)
	print(colored('\n [-] Only few options are given in this mode.','red'))
	print(colored(' [+] Edit the configuration file to change the settings.','yellow'))
	
	# Appending...
	apnd(file1,'.Temporary Files/.Temp_'+file1[20:]+'_append_rand_lower','w')
	
	# Appending random numbers...
	ran_num = input("\n> Do you want to add some random numbers at the end of words? Y/[N]: ").lower()
	if ran_num in ('yes','y'):
		rand_num(file1,'.Temporary Files/.Temp_'+file1[20:]+'_append_rand_lower','a')
	
	# Replacing with special characters...
	repl2 = input("\n> Do you want to replace alphabet with special characters? (password => p@$$w0rd) Y/[N]: ").lower()
	if repl2 in ('yes','y'):
		replace_char('.Temporary Files/.Temp_'+file1[20:]+'_append_rand_lower','.Temporary Files/.Temp_'+file1[20:]+'_leet_char_lower','w')
		
	# Leet Mode.
	leetmode2 = input("\n> Leet mode? (password => p455w0rd) Y/[N]: ").lower()
	if leetmode2 in ('y','yes'):
		replace_leet('.Temporary Files/.Temp_'+file1[20:]+'_append_rand_lower','.Temporary Files/.Temp_'+file1[20:]+'_leet_char_lower','a')
	
	# Merging into singlefile... 
		
	files_combine2 = ['.Temporary Files/.Temp_'+file1[20:]+'_append_rand_lower','.Temporary Files/.Temp_'+file1[20:]+'_leet_char_lower']
	combine_file(files_combine2,'.Temporary Files/.Temp_'+file1[20:]+'_lower')
	
	# Shaping password length...
	with open('.Temporary Files/.Temp_'+file1[20:]+'_lower','r') as f_in , open('.Temporary Files/.Temp_' + file1[20:] + '_low','w') as f_out:
		for i in f_in.readlines():
			if CONFIG['minlen'] < len(i) <= CONFIG['maxlen']+1:
				f_out.write(i)
	os.remove('.Temporary Files/.Temp_'+file1[20:] + '_lower')
	
	# Converting generated password into title case...
	if CONFIG['tit_case'] in ('true',"true"):
		title_case('.Temporary Files/.Temp_' + file1[20:] + '_low','.Temporary Files/.Temp_' + file1[20:] + '_tit','w')
	
	# Converting generated password into upper case...
	if CONFIG['upp_case'] in ('true',"true"):
		upper_case('.Temporary Files/.Temp_' + file1[20:] + '_low','.Temporary Files/.Temp_' + file1[20:] + '_upp','w')
	
	# Combining generated password into single file...
	files_combine = [ '.Temporary Files/.Temp_' + file1[20:] + '_low' , '.Temporary Files/.Temp_' + file1[20:] + '_tit' , '.Temporary Files/.Temp_' + file1[20:] + '_upp','no_file12345' ]
	
	combine_file(files_combine,'.Temporary Files/.Temp_' + file1[20:] )

# Common passwords.
def common_pass():
	if os.path.isfile('Dictionaries/common_passwords') == True:
		repeat_nocount('Dictionaries/common_passwords')
		with open('Dictionaries/common_passwords','r') as f_in , open('.Temporary Files/.Temp_common','w') as f_out:
			for i in f_in.readlines():
				if CONFIG['minlen'] < len(i) <= CONFIG['maxlen']+1:
					f_out.write(i)
	
def dictionary():
	# Applying for different dictionaries.
	# Removing dupplicate words and counting them.
	# To add new dictionary apply it in the function and edit 'config.py' and 'config.ini' file!!!
	if CONFIG['is_nepali_names'] in ('true','True'):
		dictionary_mode('Dictionaries/nepali_names')
		repeat_nocount('.Temporary Files/.Temp_names')
		
	if CONFIG['is_nepali_castes'] in ('true','True'):
		dictionary_mode('Dictionaries/nepali_castes')
		repeat_nocount('.Temporary Files/.Temp_castes')
	
	if CONFIG['is_nepali_places'] in ('true','True'):
		dictionary_mode('Dictionaries/nepali_places')
		repeat_nocount('.Temporary Files/.Temp_places')
		
	common_pass()
		
	# Combining interactive and dictionary passwords and common passwords in single file...
	files_combine = ['.Temporary Files/.Temp_interactive','.Temporary Files/.Temp_common','.Temporary Files/.Temp_names','.Temporary Files/.Temp_castes','.Temporary Files/.Temp_places']
	combine_file(files_combine,'.Temporary Files/Wordlists')

