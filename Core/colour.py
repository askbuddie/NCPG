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

class color:
	
    # Foreground:
    default = "\x1b[39m"
    black = "\x1b[30m"
    white = "\x1b[97m"
    red = "\x1b[31m"    
    green = "\x1b[32m"
    yellow = "\x1b[33m"
    blue = "\x1b[34m"
    magenta = "\x1b[35m"
    cyan = "\x1b[36m"
    lightgray = "\x1b[37m"
    darkgray = "\x1b[90m"
    lightred = "\x1b[91m"
    lightgreen = "\x1b[92m"
    lightyellow = "\x1b[93m"
    lightblue = "\x1b[94m"
    lightmagenta = "\x1b[95m"
    lightcyan = "\x1b[96m"
    
    # Background Color:
    b_default = "\x1b[49m"
    b_black = "\x1b[40m"
    b_red = "\x1b[41m"
    b_green = "\x1b[42m"
    b_yellow = "\x1b[43m"
    b_blue = "\x1b[44m"
    b_magenta = "\x1b[45m"
    b_cyan = "\x1b[46m"
    b_lightgray = "\x1b[47m"
    b_darkgray = "\x1b[100m"
    b_lightred = "\x1b[101m"
    b_lightgreen = "\x1b[102m"
    b_lightyellow = "\x1b[103m"
    b_lightblue = "\x1b[104m"
    b_lightmagenta = "\x1b[105m"
    b_lightcyan = "\x1b[106m"
    b_white = "\x1b[107m"
    
    # Style:
    bold = '\033[1m'
    underline = '\033[4m' 
    
    # Reset:
    end = '\033[0m'
    NC ='\x1b[0m' #NC = No color
