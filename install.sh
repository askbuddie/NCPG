#!/bin/bash

clear
echo $(tput setaf 1)
sleep 0.1 && echo "     ███▄▄▄▄     ▄████████     ▄███████▄     ▄██████▄ "
sleep 0.1 && echo "     ███▀▀▀██▄  ███    ███    ███    ███    ███    ███ "
sleep 0.1 && echo "     ███   ███  ███    █▀     ███    ███    ███    █▀  "
sleep 0.1 && echo "     ███   ███  ███           ███    ███   ▄███        "
sleep 0.1 && echo "     ███   ███  ███         ▀█████████▀   ▀▀███ ████▄  "
sleep 0.1 && echo "     ███   ███  ███    █▄     ███           ███    ███ "
sleep 0.1 && echo "     ███   ███  ███    ███    ███           ███    ███ "
sleep 0.1 && echo "      ▀█   █▀   ████████▀    ▄████▀         ████████▀  "
sleep 0.1 && echo
sleep 0.1 && echo "  $(tput setaf 6)Version: $(tput setaf 3)1.0"
sleep 0.1 && echo
	


if [ "$(id -u)" != "0" ]; then
    sleep 0.1 && echo -e "  $(tput setaf 1)[-] This script must be run as root$(tput sgr0)"
	sleep 0.1 && echo
	sleep 0.1 && echo "  $(tput setaf 6)usage:$(tput setaf 5) sudo bash install.sh --install | --uninstall"
	sleep 0.1 && echo

else
	if [ "$1" = "--install" ] ; then
		sleep 0.1 && echo "  Installing..."
		sleep 0.1 && echo
		if [ -d /usr/share/NepaliCustomPasswordGenerator ]; then
			echo "  $(tput setaf 2)[+] Directory already exists."
		else
			echo "  $(tput setaf 4)[+] Creating Directory."
			mkdir /usr/share/NepaliCustomPasswordGenerator
		fi
		sleep 0.1 && echo
		sleep 0.1 && echo "  $(tput setaf 4)[+]  Copying Files"
		cp -r Core /usr/share/NepaliCustomPasswordGenerator
		cp -r Dictionaries /usr/share/NepaliCustomPasswordGenerator
		cp -r .Install /usr/share/NepaliCustomPasswordGenerator
		cp config.ini /usr/share/NepaliCustomPasswordGenerator
		cp LICENSE /usr/share/NepaliCustomPasswordGenerator
		cp ncpg.py /usr/share/NepaliCustomPasswordGenerator
		cp README.md /usr/share/NepaliCustomPasswordGenerator
		cp install.sh /usr/share/NepaliCustomPasswordGenerator
		cp CHANGELOG.md /usr/share/NepaliCustomPasswordGenerator
		cp /usr/share/NepaliCustomPasswordGenerator/.Install/ncpg /usr/bin
		chmod +x /usr/bin/ncpg
		cp /usr/share/NepaliCustomPasswordGenerator/.Install/'Nepali Custom Password Generator.desktop' /usr/share/applications
		sleep 0.1 && echo
		sleep 0.1 && echo "  $(tput setaf 5)[+] Install successfully.You can now exexute NCPG just by "
		sleep 0.1 && echo "      typing 'ncpg' anywhere in terminal."
		sleep 0.1 && echo
	elif [ "$1" = "--uninstall" ] ; then
		sleep 0.1 && echo "  Uninstalling..."
		sleep 0.1 && echo
		sleep 0.1 && echo "  $(tput setaf 4)[+] Removing Directory."
		if [ -d /usr/share/NepaliCustomPasswordGenerator ] ; then
			rm -r  /usr/share/NepaliCustomPasswordGenerator
		fi
		if [ -e /usr/bin/ncpg ] ; then
			rm /usr/bin/ncpg
		fi
		if [ -e /usr/share/applications/'Nepali Custom Password Generator.desktop' ] ; then
			rm  /usr/share/applications/'Nepali Custom Password Generator.desktop'
		fi
		sleep 0.1 && echo
		sleep 0.1 && echo "  $(tput setaf 5)[-] NCPG uninstalled .You cannot exexute NCPG by using "
		sleep 0.1 && echo "      command $ 'python3 ncpg.py'  "
		sleep 0.1 && echo
	else
		sleep 0.1 && echo "  $(tput setaf 6)usage:$(tput setaf 5)  bash install.sh --install | --uninstall"
		sleep 0.1 && echo
	fi			
fi
echo "$(tput setaf 7)"
read -p "Press {enter} to continue..."
