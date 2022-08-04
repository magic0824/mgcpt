#!/usr/bin/env python3

from inspect import Attribute
import platform
import os
import sys
from xml.dom.minidom import Attr
import requests

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

def getFileFromWeb(url, fname, mode):
	file = requests.get(url, allow_redirects=True)
	open(fname, mode).write(file.content)

def install_wapp(name):
	if name == '':
		print('No packages spectified.')
		return
	print('Are you sure to install {}? '.format(name),end='')
	if y_or_n() == False:
		print('Install is stoped.')
		return
	getFileFromWeb("", "", '')
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