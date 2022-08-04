#!/bin/bash

if [ "$1" == "" ] ; then
  echo "url is required."
  exit 1
elif [ "$1" == "--help" ] ; then
  echo "remove_wapp.sh (--help|name)"
  echo "Name - Name of application"
  exit 0
fi

wapp_name=$1

if [ ! -d "/usr/share/mgcpt/apps/${wapp_name}" ] ; then
  echo "${wapp_name} is already removed or invalid name."
  exit 1
fi

echo "Removing ${wapp_name}...(1/2)"
rm -rf "/usr/share/mgcpt/apps/${wapp_name}"
echo "Removing shortcut...(2/2)"
rm -rf "/usr/share/applications/${wapp_name}.desktop"

echo "Done!"

exit 0