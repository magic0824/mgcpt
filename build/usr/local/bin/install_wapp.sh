#!/bin/bash

if [ "$1" == "" ] ; then
  echo "url is required."
  exit 1
elif [ "$2" == "" ] ; then
  echo "name is required."
  exit 1
elif [ "$1" == "--help" ] ; then
  echo "install_wapp.sh URL Name"
  echo "URL - MGCLinuxWebApp URL"
  echo "Name - Name of application"
  exit 0
fi

echo "Installation started."
echo "Downloading...(1/3)"
wget "$1" -P "/tmp/"

echo "Installing...(2/3)"
tar -xvf /tmp/main.tar -C /usr/share/mgcpt/apps/
rm /tmp/main.tar

echo "Creating shortcut...(3/3)"
wapp_name=$2
desktop_file="/usr/share/applications/${wapp_name}.desktop"
echo "[Desktop Entry]"> $desktop_file
echo "Type=Link">> $desktop_file
echo "Name=${wapp_name}">> $desktop_file
echo "Comment=Web Application">> $desktop_file
echo "URL=file:///usr/share/mgcpt/apps/${wapp_name}/index.html">> $desktop_file

echo "${wapp_name} Installed."

exit 0