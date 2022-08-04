#!/usr/bin/env python3

import subprocess
import platform
import os
from struct import pack
import sys
import requests
import urllib.request
import gzip

pretty_name=""

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
		subprocess.run(["./install_wapp.sh", nowurl])
	return

def getwappList():
	URL="https://raw.githubusercontent.com/magic0824/mgcpt/main/wapps/PackagesList"
	plfile = requests.get(URL, allow_redirects=True)
	plfileContent3 = plfile.content
	plfileContent2 = plfileContent3.decode('utf-8')
	plfileContent = plfileContent2.split('\n')
	for packageInfo2 in plfileContent:
		packageInfo = packageInfo2.split(',')
		print('Package Name: {}\n\tPackage URL: {}'.format(packageInfo[0],packageInfo[1]))
	return

def install_wapp(name):
	if name == '':
		print('No packages spectified.')
		return
	print('Are you sure to install {}?\n(If package {} is not found, will be interupt installation) '.format(name, name),end='')
	if y_or_n() == False:
		print('Install is stoped.')
		return
	installwapp(name)
	print('Successfuly installed {}"'.format(name))
	return

if __name__ == '__main__': 
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