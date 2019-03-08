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

from termcolor import colored
from Core.config import *
from os import path

# Managing unmanaged case...
def manage_case(file_name):
    f_in = open(file_name,"r")
    data = f_in.read()
    lowerr = data.lower()
    f_out = open(file_name,"w")
    f_out.write(lowerr)

# Counting number of words... 
def count(filename):
    with open(filename,'r') as f:
        count = str(len(list(f)))
        return colored(count,"yellow")
        
def count_int(filename):
    if os.path.isfile(filename) == True:
        with open(filename,'r') as f:
            count = len(list(f))
            return count
    else:
        count = 0

# Counting repeated number and removing them...
def repeat(file_name):
    with open(file_name,"r") as f_in:
        lines = len(list(f_in))
    with open(file_name,"r") as f_in:
        string = f_in.read()
        output = []
        seen = set()
        for word in string.split():
             if word not in seen:
                output.append(word + "\n")
                seen.add(word)
    a = ''.join(output)
    with open(file_name,"w") as files:
        files.write(a)
    with open(file_name,"r") as files:
        after_lines = len(list(files))
        repeated = str(lines - after_lines)
        return colored(repeated,'red')

# Removing repeated words without counting...
def repeat_nocount(file_name):
    with open(file_name,"r") as f_in:
        string = f_in.read()
        output = []
        seen = set()
        for word in string.split():
             if word not in seen:
                output.append(word + "\n")
                seen.add(word)
    a = ''.join(output)
    with open(file_name,"w") as files:
        files.write(a)


# Count,manage case and remove repeated words...
def manage_file(file_name):
	print("  [+] Current File : " + colored(file_name[13:].title(),"white"))
	print("  [+] Number Of Words : " + count(file_name))
	manage_case(file_name)
	print("  [+] Repeated Words : " + repeat(file_name))

def leet_replace(s): # For leet mode.
    for c, n in LEET_CONFIG.items():
        s = s.replace(c, n)
    return s
  
def char_replace(s): # For character replacing.
    for c, n in REPLACE_CONFIG.items():
        s = s.replace(c, n)
    return s
    
def concats(seq, start, stop): # CUPP interactive mode.
    for s in seq:
        for num in range(start, stop):
            yield s + str(num)

def komb(seq, start): # CUPP interactive mode.
    for mystr in seq:
        for mystr1 in start:
            yield mystr + mystr1


# Append things reading from configuration file...
def apnd(file1,file2,open_type):
	with open(file1, 'r') as f_in, open(file2,open_type) as f_out:
		for line in f_in:
			for i in CONFIG["appnd"]:
				f_out.write('{}'.format(line.strip()+ i +'\n'))

# Append random number...
def rand_num(file1,file2,open_type):
	with open(file1, 'r') as f_in, open(file2,open_type) as f_out:
				for line in f_in:
					for i in range(CONFIG['numfrom2'],CONFIG['numto2'] + 1):
						i = str(i)
						f_out.write('{}'.format(line.strip()+ i +'\n'))
						
# Converting into lower case...
def lower_case(file1,file2,open_type):
        f_in = open(file1,"r")
        generated_capitalize = f_in.read()
        lower = generated_capitalize.lower()

        f_out = open(file2,open_type)
        f_out.write(lower)

# Converting into title case...
def title_case(file1,file2,open_type):
        f_in = open(file1,"r")
        generated_capitalize = f_in.read()
        title = generated_capitalize.title()

        f_out = open(file2,open_type)
        f_out.write(title)

# Converting into upper case...
def upper_case(file1,file2,open_type):
        f_in = open(file1,"r")
        generated_capitalize = f_in.read()
        upper = generated_capitalize.upper()

        f_out = open(file2,open_type)
        f_out.write(upper)

# Replace with special characters for dictionaries...
def replace_char(file1,file2,open_type):
	with open(file1, 'r') as f_in, open(file2,open_type) as f_out:
		for i in f_in:
			f_out.write(char_replace(i))

# Leet mode for dictionaries.			
def replace_leet(file1,file2,open_type):
	with open(file1, 'r') as f_in, open(file2,open_type) as f_out:
		for i in f_in:
			f_out.write(leet_replace(i))

# Combine file if exists.
def combine_file(file_in,name):
	with open(name,'w') as f_out:
		for i in file_in:
			if os.path.isfile(i) == True:
				with open(i,'r') as f_in:
					for line in f_in:
						f_out.write(line)
				os.remove(i)
