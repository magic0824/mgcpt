#!/usr/bin/env python3

import subprocess
import platform
import os
from struct import pack
import sys
import requests

sh_install_wapp="install_wapp.sh"
sh_remove_wapp="remove_wapp.sh"

def get_command():
	try:
		return sys.argv[1]
	except:
		return ""

def get_package():
	try:
		return sys.argv[2]
	except:
		return ""

def help_command():
	print('mgcpt.py - The package tool for MGCLinux')
	print('mgcpt.py help|install|install-wapp name\n')
	print('help - Show this help')
	print('install - Install application(beta)')
	print('install-wapp - Install web application')
	return

def y_or_n():
	print('(y/N)')
	yn=input()
	yn='{}'.format(yn.lower())
	if yn == 'y' or yn == 'ye' or yn == 'yes':
		return True
	elif yn == 'n' or yn == 'no':
		return False
	else:
		return False
	return

def install(name):
	print('This feature is under development.')
	return

def list_app():
	print('This feature is under development.')
	return

def remove_app():
	print('This feature is under development.')
	return

def installwapp(name):
	URL="https://raw.githubusercontent.com/magic0824/mgcpt/main/wapps/PackagesList"
	plfile = requests.get(URL, allow_redirects=True)
	plfileContent3 = plfile.content
	plfileContent2 = plfileContent3.decode('utf-8')
	plfileContent = plfileContent2.split('\n')
	foundPackage=False
	for packageInfo2 in plfileContent:
		packageInfo = packageInfo2.split(',')
		if packageInfo[0] == name:
			nowname=name
			nowurl=packageInfo[1]
			foundPackage=True
			break
	if foundPackage == False:
		print('Sorry, package {} is not found.'.format(name))
		return
	if foundPackage == True:
		subprocess.run([sh_install_wapp, nowurl, nowname])
	return

def removewapp(name):
	try:
		subprocess.run([sh_remove_wapp, name], check=True)
		return True
	except:
		print('Uninstallation error: application cannot be removed.')
		return False
	return False

def getwappList():
	URL="https://raw.githubusercontent.com/magic0824/mgcpt/main/wapps/PackagesList"
	plfile = requests.get(URL, allow_redirects=True)
	plfileContent3 = plfile.content
	plfileContent2 = plfileContent3.decode('utf-8')
	plfileContent = plfileContent2.split('\n')
	for packageInfo2 in plfileContent:
		packageInfo = packageInfo2.split(',')
		print('Package Name: {}\n\tAuthor: {}\n\tURL: {}'.format(packageInfo[0],packageInfo[2],packageInfo[1]))
	return

def install_wapp(name):
	if name == '':
		print('No packages spectified.')
		return
	print('Are you sure to install {}?\n(If package {} is not found, will be interupt installation) '.format(name, name),end='')
	if y_or_n() == False:
		print('Installation is stoped.')
		return
	installwapp(name)
	print('Successfuly installed {}.'.format(name))
	return

def remove_wapp(name):
	print('Are you sure to remove {}?\nThis action cannot be UNDONE!'.format(name), end='')
	if y_or_n() == False:
		print('Uninstallation is stoped.')
		return
	if removewapp(name) == False:
		print('Uninstallation failed.')
		return
	print('Successfuly uninstalled {}.'.format(name))
	return

if __name__ == '__main__':
	if platform.system() != 'Linux':
		sys.exit("This program can run on linux.")

	command = get_command()
	if command == "":
		print('No command.\n')
		help_command()
	elif command == "help":
		help_command()
	elif command == "install":
		package=get_package()
		install(package)
	elif command == "install-wapp":
		package=get_package()
		install_wapp(package)
	elif command == "list":
		list_app()
	elif command == "list-wapp":
		getwappList()
	elif command == "remove":
		remove_app()
	elif command == "remove-wapp":
		package=get_package()
		remove_wapp(package)