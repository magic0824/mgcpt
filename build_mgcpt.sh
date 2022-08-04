#!/bin/bash

if [ ! -e "./build/BUILDDIR" ] ; then
	echo "No build directory."
	exit 1
fi

echo "Removing old builded file..."
rm -rf ./build/usr
echo "Building..."
echo "Make directorys(3/1)"
mkdir -p ./build/usr/share/mgcpt/apps
mkdir -p ./build/usr/local/bin
echo "Copy files(3/2)"
cp ./mgcpt.py ./build/usr/local/bin
cp ./install_wapp.sh ./build/usr/local/bin/install_wapp.sh
cp ./remove_wapp.sh ./build/usr/local/bin/remove_wapp.sh
echo "Change permission(3/3)"
chmod +x ./build/usr/local/bin/mgcpt.py
chmod +x ./build/usr/local/bin/install_wapp.sh
chmod +x ./build/usr/local/bin/remove_wapp.sh
echo "Done! Copy files (exclude 'BUILDDIR') to MGCLinux."
exit 0