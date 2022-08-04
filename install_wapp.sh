#!/bin/bash

if [ "$1" == "" ] ; then
  echo "url is required."
  exit 1
fi

wget "$1"

tar -xvf ./main.tar -C /usr/share/mgcpt/apps/

rm ./main.tar