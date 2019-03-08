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
from termcolor import colored
from Core.func import linux_type
from Core.func import clean_terminal
from Core.banners import banner
from Core.config import *
from Core.text import zones
from Core.colour import color
from Core.managefile import combine_file
from Core.managefile import count_int


read_config()

# Check if crunch is installed or not. Install if Debian.
def install_crunch():
	clean_terminal()
	banner()
	print('[PHONE NUMBER MODE]')
	
	if os.path.isfile('/usr/bin/crunch') == False:
		print(colored('\n  [-] Its seems like crunch is not installed in your system.','red'))
		print(colored('  [+] NCPG uses crunch to generate phone numbers.','yellow'))
		
		install_cru = input('\nDo you want to install cruch? Y/[N]: ').lower()
		if install_cru in ('y','yes'):
			if linux_type() == 'Debian':
				print('\n----------------------------------------------------------------------')
				print(colored('[Installing Crunch]','yellow'))
				os.system('sudo apt-get install crunch')
				print('----------------------------------------------------------------------')
				
			else:
				print(colored('\n  [-] Its seems your system is not debian. Please install cruch manually.','red'))
	else:
		pass

# Generate phone numbers using crunch.
# Name will be given automatically to generated phonenumber.
def num(n):
	for i in n:
		print(colored('\n[Generating Numbers starting with ' + i + ']','yellow'))
		j = 10 - len(i)
		os.system("crunch 10 10 -t " + i + (j*"%") + " -o '.Temporary Files/" + i + "'")
		print('----------------------------------------------------------------------')

# Generate phone numbers using crunch.
# Name should be given to the file to be generated.
def num2(n,name):
	for i in n:
		print(colored('\n[Generating Numbers starting with ' + i + ']','yellow'))
		j = 10 - len(i)
		os.system("crunch 10 10 -t " + i + (j*"%") + " -o '.Temporary Files/" + name + "'")
		print('----------------------------------------------------------------------')

# Generating phonenumbers for other telecom services exccept ncell because it uses different pattern according to zones.
def pattern(x):
	if x == 'ntc':
		n = ['984','985','986']
	if x == 'sky':
		n = ['974','975']
	if x == 'smart cell':
		n = ['961','988']
	if x == 'utl':
		n = ['972']
	if x == 'hello mobile':
		n = ['963']
	
	if x in ('utl','hello mobile'):
		if CONFIG[x] in ('true','True'):
			clean_terminal()
			banner()
			print('[PHONE NUMBER MODE]')
			print("\n=====================================================================\n")
			print(colored('                 Genetating ' + x.upper() + ' Numbers\n','yellow'))
			print('======================================================================')
			num2(n,x.title())
	
	else:
		if CONFIG[x] in ('true','True'):
			clean_terminal()
			banner()
			print('[PHONE NUMBER MODE]')
			print("\n=====================================================================\n")
			print(colored('                 Genetating ' + x.upper() + ' Numbers\n','yellow'))
			print('======================================================================')
			num(n)
		
			# Combining phone numbers
			print(colored('\n[+] Combining phone numbers. Please be patient','red'))
			new2 = []
			for i in n:
				i = ['.Temporary Files/' + i]
				new2 = new2 + i
			combine_file(new2,'.Temporary Files/' + x.title())

# Ncell number pattern for different zones...
mechi = ['98014','98140','98150','98170','98240','98249','98049','98079','98060','98149','98159','98169','98179','98160','98259','98269','98279']

koshi = ['98027','98207','98040','98190','98110','98113','98123','98009','98043','98070','98073','98053','98143','98153','98163','98173','98193','98104','98105','98243','98253','98263']

sagarmatha = ['98015','98047','98077','98059','98147','98157','98167','98177','98197','98199','98117','98247','98257','98267']

janakpur = ['98016','98048','98076','98078','98148','98158','98168','98178','98198','98196','98176','98120','98121','98008','98096','98248','98258','98268']

narayani = ['98029','98209','98042','98068','98071','98072','98142','98152','98162','98172','98192','98111','98112','98118','98122','98091','98092','98211','98212','98218','98242','98252']

bagmati = ['98021','98020','98011','98022','98018','98019','98012','98010','98023','98024','9803','9808','9813','9818','98100','98101','98102','98103', '98230','98231','98232','98233','98234','98235','98236','98237','98238','98239']

gandaki = ['98028','98166','98241','98251','98261','98041','98065','98066','98067','98058','98141','98151','98161','98171','98191','98271','98291','98266']

lumbini = ['98026','98129','98007','98214','98215','98219','98044','98069','98074','98075','98054','98144','98154','98164','98174','98194','98175','98114','98115','98119','98244','98254']

dhaulagiri = ['9801300','98061','98051','98052','98213']

rapti = ['9801325','98062','98095','98097','98098','98128','98108','98109','98228','98229']

karnali = ['9801350','98063','98093']

bheri = ['98025','98195','98124','98125','98005','98224','98225','98045','98145','98155','98165','98245','98255','98265']

seti = ['98017','98046','98146','98156','98116','98126','98006','98246','98256','98216','98226']

mahakali = ['9801375','98127','98106','98107','9805740','98064','98094']

# Generate phone numbers for Ncell numbers.
def ncell():
	clean_terminal()
	banner()
	print('[PHONE NUMBER MODE]')
	print(colored('\n[+] Ncell has different number pattern according to zones. It help to reduce \n    the numbers of combination.\n','yellow'))
	print(colored(zones,'blue'))
	print(colored("[+] Type the zone number you want to generate phone numbers for.",'magenta'))
	print(colored("[+] For more than one zone type the number separated by comma.",'magenta'))
	print(colored("[+] Type 'all' to generate Ncell numbers of all zone.",'magenta'))
	opt4 = input(colored(color.bold + "\nncpg> ","cyan")).lower().split(',')
	
	numb = []
	if '1' in opt4:
		numb = numb + mechi
	if '2' in opt4:
		numb = numb + koshi
	if '3' in opt4:
		numb = numb + sagarmatha
	if '4' in opt4:
		numb = numb + janakpur
	if '5' in opt4:
		numb = numb + narayani
	if '6' in opt4:
		numb = numb + bagmati
	if '7' in opt4:
		numb = numb + gandaki
	if '8' in opt4:
		numb = numb + lumbini
	if '9' in opt4:
		numb = numb + dhaulagiri
	if '10' in opt4:
		numb = numb + rapti
	if '11' in opt4:
		numb = numb + karnali
	if '12' in opt4:
		numb = numb + bheri
	if '13' in opt4:
		numb = numb + seti
	if '14' in opt4:
		numb = numb + mahakali
	if 'all' in opt4:
		numb = []
		numb = mechi + koshi + sagarmatha + janakpur + narayani + bagmati + gandaki + lumbini + dhaulagiri + rapti + karnali + bheri + seti + mahakali
	if '1' in opt4 or '2' in opt4 or '3' in opt4 or '4' in opt4 or '5' in opt4 or '6' in opt4 or '7' in opt4 or '8' in opt4 or '9' in opt4 or '10' in opt4 or '11' in opt4 or '12' in opt4 or '13' in opt4 or '14' in opt4 or 'all' in opt4:
		clean_terminal()
		banner()
		print('[PHONE NUMBER MODE]')
		print("\n=====================================================================\n")
		print(colored('                 Genetating NCELL Numbers\n','yellow'))
		print('======================================================================')
		num(numb)
	else:
		pass
		
	
# Phone Number Mode
def phone_num():
	if os.path.isfile('/usr/bin/crunch') == True:
		print(colored('\nPhone Numbers have good chance to be password.But,it highly increases the \nnumber of wordlists.NCPG generated phone numbers of different telecom of nepal.\nEdit the configuration file to genetare phone numbers of your wish.','blue'))
	
		ph = input('\n> Do you want to generate phone numbers? Y/[N]: ')
		if ph in ('y','yes'):
			print(colored('\n  [-] No options are provided in this mode.','red'))
			print(colored('  [+] Edit the configuration file to change the settings.','yellow'))
			if CONFIG['ncell'] in ('true','True'):
				ncell()
				# Combining all ncell numbers in single files
				files_combine = mechi + koshi + sagarmatha + janakpur + narayani + bagmati + gandaki + lumbini + dhaulagiri + rapti + karnali + bheri + seti + mahakali
				print(colored('\n[+] Combining phone numbers. Please be patient','red'))
				new = []
				for i in files_combine:
					i = ['.Temporary Files/' + i]
					new = new + i
				combine_file(new,'.Temporary Files/Ncell')
				if count_int('.Temporary Files/Ncell') == 0:
					os.remove('.Temporary Files/Ncell')
		
			pattern('ntc')
			pattern('sky')
			pattern('smart cell')
			pattern('utl')
			pattern('hello mobile')
		
		
