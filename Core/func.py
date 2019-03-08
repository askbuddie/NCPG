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
import platform


def clean_terminal():
	operating_system = platform.system()
	if operating_system == "Linux":
		os.system("clear")

	elif operating_system == "Windows":
		os.system("cls") 		
	else:
		pass


def linux_type():
    # If source.list exist its Debian.
    if os.path.isfile("/etc/apt/sources.list"):
        return "Debian"

    # If pacman.conf exists its Arch.
    elif os.path.isfile("/etc/pacman.conf"):
        return "Arch"
            
    # If dnf.conf exist its fedora. 
    elif os.path.isfile("/etc/dnf/dnf.conf"):
        return "Fedora"
        
    else:
        return "Unknown"
