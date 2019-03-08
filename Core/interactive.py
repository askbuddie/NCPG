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
#
# interactive.py is the part of program "CUPP" which is written by Muris Kurgas. NCPG use CUPP for interactive mode.
# -----------------------------------------------------------------------------------------------------------
# Applying CUPP in NCPG considering GNU GPL license
# -------------------------------------------------
#
#  Author of CUPP
#  --------------
#  Muris Kurgas aka j0rgan
#  j0rgan [at] remote-exploit [dot] org
#  http://www.remote-exploit.org
#  http://www.azuzi.me

import os
import sys
from termcolor import colored
from Core.managefile import *
from Core.config import *
import shutil


def main():
    read_config()


def interactive():
    print("[INTERACTIVE MODE]")
    print(colored("\n[+] Opening cupp for interactive mode.","yellow"))
    print("\n[+] Insert the information about the victim to make a dictionary")
    print("[+] If you don't know all the info, just hit enter when asked! ;)\n")

    # We need some information first!

    name = input("> First Name: ").lower().strip()
    surname = input("> Surname: ").lower()
    nick = input("> Nickname: ").lower()
    birthplace = input("> Birthplace: ")
    birthdate = input("> Birthdate (DDMMYYYY): ").strip()
    while len(birthdate) not in (0, 8):
        print("\n[-] You must enter 8 digits for birthday!", file=sys.stderr)
        birthdate = input("> Birthdate (DDMMYYYY): ").strip()

    wife = input("\n> Partner's name: ").lower()
    wifen = input("> Partner's nickname: ").lower()
    wifeb = input("> Partner's birthdate (DDMMYYYY): ").strip()
    while len(wifeb) not in (0, 8):
        print("\n[-] You must enter 8 digits for birthday!", file=sys.stderr)
        wifeb = input("> Partner's birthdate (DDMMYYYY): ").strip()

    kid = input("\n> First child's name: ").lower()
    kidn = input("> Nickname: ").lower()
    kidb = input("> Birthdate (DDMMYYYY): ").strip()
    while len(kidb) not in (0, 8):
        print("\n[-] You must enter 8 digits for birthday!", file=sys.stderr)
        kidb = input("> Birthdate (DDMMYYYY): ").strip()
    school = input("> School/college: ")
    
    kid2 = input("\n> Second child's name: ").lower()
    kid2n = input("> Nickname: ").lower()
    kid2b = input("> Birthdate (YYYYDDMM): ").strip()
    while len(kid2b) not in (0, 8):
        print("\n[-] You must enter 8 digits for birthday!", file=sys.stderr)
        kid2b = input("> Birthdate (DDMMYYYY): ").strip()
    school2 = input("> School/college: ")
    pet = input("\n> Pet's name: ").lower().strip()
    company = input("> Company name: ").lower().strip()

    prompt = "\n> Do you want to add some key words about the victim? Y/[N]: "
    words1 = input(prompt).lower().strip()
    words2 = ''
    if words1 == 'y'or words1 == "yes" :
        prompt = (">> Please enter the words, comma-separated."
                  " (i.e. favourite star,residental area,hobby), spaces will be removed: ")
        words2 = input(prompt).replace(' ', '')
    words = words2.split(',')

    spechars = []
    prompt = "\n> Do you want to add special characters at the end of words? Y/[N]: "
    spechars1 = input(prompt).lower()
    if spechars1 == "y" or spechars1 == "yes":
        for spec1 in CONFIG['chars']:
            spechars.append(spec1)
            for spec2 in CONFIG['chars']:
                spechars.append(spec1+spec2)
                for spec3 in CONFIG['chars']:
                    spechars.append(spec1+spec2+spec3)

    randnum = input("\n> Do you want to add some random numbers at the end of words? Y/[N]: ").lower()
    repl = input("\n> Do you want to replace alphabet with special characters? (password => p@$$w0rd) Y/[N]: ").lower()
    leetmode = input("\n> Leet mode? (password => p455w0rd) Y/[N]: ").lower().strip()

    #String modification ,  Birthdays first

    birthdate_yy, birthdate_yyy = birthdate[-2:], birthdate[-3:]
    birthdate_yyyy = birthdate[-4:]
    birthdate_xd, birthdate_xm = birthdate[1:2], birthdate[3:4]
    birthdate_dd, birthdate_mm = birthdate[:2], birthdate[2:4]

    wifeb_yy = wifeb[-2:]
    wifeb_yyy = wifeb[-3:]
    wifeb_yyyy = wifeb[-4:]
    wifeb_xd = wifeb[1:2]
    wifeb_xm = wifeb[3:4]
    wifeb_dd = wifeb[:2]
    wifeb_mm = wifeb[2:4]

    kidb_yy = kidb[-2:]
    kidb_yyy = kidb[-3:]
    kidb_yyyy = kidb[-4:]
    kidb_xd = kidb[1:2]
    kidb_xm = kidb[3:4]
    kidb_dd = kidb[:2]
    kidb_mm = kidb[2:4]
    
    kid2b_yy = kid2b[-2:]
    kid2b_yyy = kid2b[-3:]
    kid2b_yyyy = kid2b[-4:]
    kid2b_xd = kid2b[1:2]
    kid2b_xm = kid2b[3:4]
    kid2b_dd = kid2b[:2]
    kid2b_mm = kid2b[2:4]

    # Convert first letters to uppercase...
    nameup = name.title()
    surnameup = surname.title()
    nickup = nick.title()
    birthplaceup = birthplace.title()
    wifeup = wife.title()
    wifenup = wifen.title()
    kidup = kid.title()
    kidnup = kidn.title()
    schoolup = school.title()
    kid2up = kid2.title()
    kid2nup = kid2n.title()
    school2up = school2.title()
    petup = pet.title()
    companyup = company.title()
    wordsup = [words1.title() for words1 in words]
    word = words+wordsup 

    # Reverse a name!!!

    rev_name = name[::-1]
    rev_nameup = nameup[::-1]
    rev_birthplace = birthplaceup[::-1]
    rev_nick = nick[::-1]
    rev_nickup = nickup[::-1]
    rev_wife = wife[::-1]
    rev_wifeup = wifeup[::-1]
    rev_kid = kid[::-1]
    rev_kidup = kidup[::-1]
    rev_schoolup = schoolup[::-1]
    rev_kid2 = kid2[::-1]
    rev_kid2up = kid2up[::-1]
    rev_school2up = school2up[::-1]

    reverse = [rev_name, rev_nameup, rev_birthplace, rev_nick, rev_nickup, rev_wife,
               rev_wifeup, rev_kid, rev_kidup, rev_kid2, rev_kid2up]
    rev_n = [rev_name, rev_nameup, rev_birthplace, rev_nick, rev_nickup]
    rev_w = [rev_wife, rev_wifeup]
    rev_k = [rev_kid, rev_kidup, rev_kid2, rev_kid2up]

    # Birthdays combinations!!!
    bds = [birthdate_yy, birthdate_yyy, birthdate_yyyy, birthdate_xd,
           birthdate_xm, birthdate_dd, birthdate_mm]
    bdss = []

    for bds1 in bds:
        bdss.append(bds1)
        for bds2 in bds:
            if bds.index(bds1) != bds.index(bds2):
                bdss.append(bds1 + bds2)
                for bds3 in bds:
                    condition = (bds.index(bds1) != bds.index(bds2) and
                                 bds.index(bds2) != bds.index(bds3) and
                                 bds.index(bds1) != bds.index(bds3))
                    if condition:
                        bdss.append(bds1+bds2+bds3)

    # For a woman!!!
    wbds = [wifeb_yy, wifeb_yyy, wifeb_yyyy, wifeb_xd, wifeb_xm, wifeb_dd, wifeb_mm]
    wbdss = []

    for wbds1 in wbds:
        wbdss.append(wbds1)
        for wbds2 in wbds:
            if wbds.index(wbds1) != wbds.index(wbds2):
                wbdss.append(wbds1+wbds2)
                for wbds3 in wbds:
                    condition = (wbds.index(wbds1) != wbds.index(wbds2) and
                                 wbds.index(wbds2) != wbds.index(wbds3) and
                                 wbds.index(wbds1) != wbds.index(wbds3))
                    if condition:
                        wbdss.append(wbds1+wbds2+wbds3)

    # And a child!!!
    kbds = [kidb_yy, kidb_yyy, kidb_yyyy, kidb_xd, kidb_xm, kidb_dd, kidb_mm]
    kbdss = []

    for kbds1 in kbds:
        kbdss.append(kbds1)
        for kbds2 in kbds:
            if kbds.index(kbds1) != kbds.index(kbds2):
                kbdss.append(kbds1+kbds2)
                for kbds3 in kbds:
                    condition = (kbds.index(kbds1) != kbds.index(kbds2) and
                                 kbds.index(kbds2) != kbds.index(kbds3) and
                                 kbds.index(kbds1) != kbds.index(kbds3))
                    if condition:
                        kbdss.append(kbds1+kbds2+kbds3)
    # For second child!!!                  
    k2bds = [kid2b_yy, kid2b_yyy, kid2b_yyyy, kid2b_xd, kid2b_xm, kid2b_dd, kid2b_mm]
    k2bdss = []

    for kbds1 in k2bds:
        k2bdss.append(kbds1)
        for kbds2 in k2bds:
            if k2bds.index(kbds1) != k2bds.index(kbds2):
                k2bdss.append(kbds1+kbds2)
                for kbds3 in k2bds:
                    condition = (k2bds.index(kbds1) != k2bds.index(kbds2) and
                                 k2bds.index(kbds2) != k2bds.index(kbds3) and
                                 k2bds.index(kbds1) != k2bds.index(kbds3))
                    if condition:
                        k2bdss.append(kbds1+kbds2+kbds3)

    # string combinations!!!
    kombinaac = [pet, petup, company, companyup]
    kombina = [name, surname, nick, nameup, surnameup, nickup, birthplace, birthplaceup]
    kombinaw = [wife, wifen, wifeup, wifenup, surname, surnameup]
    kombinak = [kid, kidn, kidup, kidnup, surname, surnameup, kid2, kid2n, kid2up, kid2nup, school, schoolup, school2, school2up]

    kombinaa = []
    for kombina1 in kombina:
        kombinaa.append(kombina1)
        for kombina2 in kombina:
            condition = (kombina.index(kombina1) != kombina.index(kombina2) and
                         kombina.index(kombina1.title()) != kombina.index(kombina2.title()))
            if condition:
                kombinaa.append(kombina1+kombina2)

    kombinaaw = []
    for kombina1 in kombinaw:
        kombinaaw.append(kombina1)
        for kombina2 in kombinaw:
            condition = (kombinaw.index(kombina1) != kombinaw.index(kombina2) and
                         kombinaw.index(kombina1.title()) != kombinaw.index(kombina2.title()))
            if condition:
                kombinaaw.append(kombina1+kombina2)

    kombinaak = []
    for kombina1 in kombinak:
        kombinaak.append(kombina1)
        for kombina2 in kombinak:
            condition = (kombinak.index(kombina1) != kombinak.index(kombina2) and
                         kombinak.index(kombina1.title()) != kombinak.index(kombina2.title()))
            if condition:
                kombinaak.append(kombina1+kombina2)

    komb1 = list(komb(kombinaa, bdss))
    komb2 = list(komb(kombinaaw, wbdss))
    komb3 = list(komb(kombinaak, kbdss))
    komb4 = list(komb(kombinaa, CONFIG['years']))
    komb5 = list(komb(kombinaac, CONFIG['years']))
    komb6 = list(komb(kombinaaw, CONFIG['years']))
    komb7 = list(komb(kombinaak, CONFIG['years']))
    komb8 = list(komb(word, bdss))
    komb9 = list(komb(word, wbdss))
    komb10 = list(komb(word, kbdss))
    komb11 = list(komb(word, CONFIG['years']))
    komb12 = komb13 = komb14 = komb15 = komb16 = komb21 = []
    if randnum == "y" or randnum == "yes":
        komb12 = list(concats(word, CONFIG['numfrom'], CONFIG['numto']))
        komb13 = list(concats(kombinaa, CONFIG['numfrom'], CONFIG['numto']))
        komb14 = list(concats(kombinaac, CONFIG['numfrom'], CONFIG['numto']))
        komb15 = list(concats(kombinaaw, CONFIG['numfrom'], CONFIG['numto']))
        komb16 = list(concats(kombinaak, CONFIG['numfrom'], CONFIG['numto']))
        komb21 = list(concats(reverse, CONFIG['numfrom'], CONFIG['numto']))
    komb17 = list(komb(reverse, CONFIG['years']))
    komb18 = list(komb(rev_w, wbdss))
    komb19 = list(komb(rev_k, kbdss))
    komb20 = list(komb(rev_n, bdss))
    komb001 = komb002 = komb003 = komb004 = komb005 = komb006 = []
    if spechars1 == "y" or spechars1 == 'yes':
        komb001 = list(komb(kombinaa, spechars))
        komb002 = list(komb(kombinaac, spechars))
        komb003 = list(komb(kombinaaw, spechars))
        komb004 = list(komb(kombinaak, spechars))
        komb005 = list(komb(word, spechars))
        komb006 = list(komb(reverse, spechars))

    sets = [set(komb1), set(komb2), set(komb3), set(komb4), set(komb5),
            set(komb6), set(komb7), set(komb8), set(komb9), set(komb10),
            set(komb11), set(komb12), set(komb13), set(komb14), set(komb15),
            set(komb16), set(komb17), set(komb18), set(komb19), set(komb20),
            set(komb21), set(kombinaa), set(kombinaac), set(kombinaaw),
            set(kombinaak), set(word), set(komb001), set(komb002), set(komb003),
            set(komb004), set(komb005), set(komb006)]

    uniqset = set()
    for s in sets:
        uniqset.update(s)

    uniqlist = bdss + wbdss + kbdss + k2bdss + reverse + list(uniqset)

    unique_lista = sorted(set(uniqlist))
    unique_leet = []
    if leetmode == "y" or leetmode == "yes":
        for x in unique_lista:
            unique_leet.append(leet_replace(x))
    
    replac = []
    if repl == "y" or repl == 'yes':
        for x in unique_lista:
            replac.append(char_replace(x))
           
    unique_list = unique_lista + unique_leet + replac
    
    unique_list_finished = [x for x in unique_list if CONFIG['minlen'] <= len(x) <= CONFIG['maxlen']]
    
    unique_list_finished.sort()
    
    if os.path.exists('.Temporary Files'):
        shutil.rmtree('.Temporary Files')
    
    os.makedirs('.Temporary Files')
    with open('.Temporary Files/.Temp_interactive', 'w') as f:
        f.write(os.linesep.join(unique_list_finished))
    repeat_nocount('.Temporary Files/.Temp_interactive')

if __name__ == '__main__':
    main()
