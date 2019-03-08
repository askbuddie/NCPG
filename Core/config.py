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

import configparser
import os
import functools

default_config = \
"""
################################################################################
#              Nepali Custom  Password Generator (NCPG)                        #
#                Generate common weak nepali password                          #
#  This is configuration file of NCPG.                                         #
#                                                                              #
# -Edit the settings according to your wish.                                   #
# -Replace 'true' with 'false' if you dont want to use the functions.          #
#                                                                              #
################################################################################


[PASSWORD LENGTH]
# Set the minimum and maximum length of password to be generated.
minimum length = 8     
maximum length = 15    


[APPEND]
# These words will be added at the end of passwords. Only for dictionary mode.
append = 123,1234,12345,@123,@1234,@12345


[APPEND INTERACTIVE]
# These words will be added at the end of passwords. Only for interactive mode.
append = 2070,2071,2072,2073,2074,2075,2076,123,1234,12345,@123,@1234,@12345


[REPLACE]
# Replace alphabet characters with special characters. Eg; password => p@$$w0rd
a = @
c = c
h = h
i = i
l = l
o = 0
s = $


[LEET]
# leet mode. Eg; password => p455w0rd
a = 4
i = 1
e = 3
t = 7
o = 0
s = 5
g = 9
z = 2


[SPECIAL CHARACTERS]
# These characters will be included in the wordlists.
chars = !,@,'#',$,%%,&,*


[RANDOM NUMBERS]
# Add ramdom numbers from and to. Only for interactive mode not for dictionary mode.
from = 0
to = 100


[RANDOM NUMBERS2]
# Add ramdom numbers from and to. Only for dictionary mode not for interactive mode.
from = 0
to = 10


[DICTIONARIES]
# Dictionaries to be included in the wordlists.
nepali_names = true   
nepali_castes = true
nepali_places = true
 
 
[CASES]
# Cases of wordlists. Only for dictionary mode not for interactive mode.
# lower case = true by default
title case = true
upper case = true


[PHONE NUMBERS]
# Ncell numbers starts with 980 / 981 / 982
# Nameste commonly known as NTC numbers starts with  984 / 985 / 986
# Sky numbers starts with 974 / 975
# Smart Cell numbers starts with  961 / 988
# UTL numbers starts with  972
# Hello mobile or Nepal Satellite Telecom starts with 963
Ncell = true
Namaste = false
Sky = false
Smart Cell = false 
UTL = false
Hello Mobile = false
"""

# Checking whether config file exist or not and write if not.
def check_config():
	if os.path.isfile("config.ini") == False:
		with open("config.ini","w") as configuration:
			configuration.write(default_config)
	else:
		pass

# Reset configuration file
def reset_config():
	with open("config.ini","w") as configuration:
			configuration.write(default_config)
			
# Reading confiuration file
CONFIG = {}
LEET_CONFIG = {}
REPLACE_CONFIG = {}
def read_config(filename='config.ini'):
    # Reading configuration file
    config = configparser.ConfigParser()
    config.read(filename)

    CONFIG.update({
        'years':     config.get('APPEND INTERACTIVE', 'APPEND').split(','),
        'appnd':     config.get('APPEND', 'APPEND').split(','),
        'chars':     config.get('SPECIAL CHARACTERS', 'chars').split(','),

        'numfrom':   config.getint('RANDOM NUMBERS', 'from'),
        'numto':     config.getint('RANDOM NUMBERS', 'to'),
        
        'numfrom2':   config.getint('RANDOM NUMBERS2', 'from'),
        'numto2':     config.getint('RANDOM NUMBERS2', 'to'),

        'maxlen':    config.getint('PASSWORD LENGTH', 'maximum length'),
        'minlen':      config.getint('PASSWORD LENGTH', 'minimum length'),
        
        'tit_case':    config.get('CASES', 'title case'),
        'upp_case':      config.get('CASES', 'upper case'),
        
        'is_nepali_names':    config.get('DICTIONARIES', 'nepali_names'),
        'is_nepali_castes':      config.get('DICTIONARIES', 'nepali_castes'),
        'is_nepali_places':    config.get('DICTIONARIES', 'nepali_places'),
        
        'ntc':    config.get('PHONE NUMBERS', 'Namaste'),
        'ncell':      config.get('PHONE NUMBERS', 'Ncell'),
        'sky':    config.get('PHONE NUMBERS', 'Sky'),
        'smart cell':    config.get('PHONE NUMBERS', 'Smart Cell'),
        'utl':      config.get('PHONE NUMBERS', 'UTL'),
        'hello mobile':    config.get('PHONE NUMBERS', 'Hello Mobile'),
        
        
    })
    
    # For leet mode.
    leet = functools.partial(config.get, 'LEET')
    LEET_CONFIG.update(dict(a=leet('a'), e=leet('e'), g=leet('g'), i=leet('i'),
                            o=leet('o'), s=leet('s'), t=leet('t'), z=leet('z')))
                            
    # For replace mode. 
    rep = functools.partial(config.get, 'REPLACE')
    REPLACE_CONFIG.update(dict(a=rep('a'), h=rep('h'), i=rep('i'), l=rep('l'), o=rep('o'), s=rep('s') ))
