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
import random

banner1 = \
''' 
     ███╗   ██╗     ██████╗    ██████╗      ██████╗ 
     ████╗  ██║    ██╔════╝    ██╔══██╗    ██╔════╝ 
     ██╔██╗ ██║    ██║         ██████╔╝    ██║  ███╗
     ██║╚██╗██║    ██║         ██╔═══╝     ██║   ██║
     ██║ ╚████║    ╚██████╗    ██║         ╚██████╔╝
     ╚═╝  ╚═══╝     ╚═════╝    ╚═╝          ╚═════╝ 
                                               
'''



banner2 = \
'''
      ███▄    █     ▄████▄      ██▓███       ▄████ 
      ██ ▀█   █    ▒██▀ ▀█     ▓██░  ██▒    ██▒ ▀█▒
     ▓██  ▀█ ██▒   ▒▓█    ▄    ▓██░ ██▓▒   ▒██░▄▄▄░
     ▓██▒  ▐▌██▒   ▒▓▓▄ ▄██▒   ▒██▄█▓▒ ▒   ░▓█  ██▓
     ▒██░   ▓██░   ▒ ▓███▀ ░   ▒██▒ ░  ░   ░▒▓███▀▒
     ░ ▒░   ▒ ▒    ░ ░▒ ▒  ░   ▒▓▒░ ░  ░    ░▒   ▒ 
     ░ ░░   ░ ▒░     ░  ▒      ░▒ ░          ░   ░ 
        ░   ░ ░    ░           ░░          ░ ░   ░ 
              ░    ░ ░                           ░                   
'''

banner3 = \
'''
     ███▄▄▄▄     ▄████████     ▄███████▄     ▄██████▄  
     ███▀▀▀██▄  ███    ███    ███    ███    ███    ███ 
     ███   ███  ███    █▀     ███    ███    ███    █▀  
     ███   ███  ███           ███    ███   ▄███        
     ███   ███  ███         ▀█████████▀   ▀▀███ ████▄  
     ███   ███  ███    █▄     ███           ███    ███ 
     ███   ███  ███    ███    ███           ███    ███ 
      ▀█   █▀   ████████▀    ▄████▀         ████████▀  
                                                              
'''

 

banner4 = \
'''                                                  
     @@@  @@@      @@@@@@@     @@@@@@@       @@@@@@@@  
     @@@@ @@@     @@@@@@@@     @@@@@@@@     @@@@@@@@@  
     @@!@!@@@     !@@          @@!  @@@     !@@        
     !@!!@!@!     !@!          !@!  @!@     !@!        
     @!@ !!@!     !@!          @!@@!@!      !@! @!@!@  
     !@!  !!!     !!!          !!@!!!       !!! !!@!!   
     :!:  !:!     :!:          :!:          :!:   !::
     ::   ::      ::: :::      ::           ::: ::::  
     ::    :       :: :: :      :            :: :: :                                                   
'''                                                                                    

                                  

list_banner = [banner1,banner2,banner3,banner4]

list_color = ["yellow","red","blue","white","green","cyan","magenta"]

def banner():
	print(colored(random.choice(list_banner),random.choice(list_color)))
