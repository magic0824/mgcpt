#!/bin/bash

if [ "$1" == "" ] ; then
  echo "gz filename is required."
  exit 1
fi

tar cf $1 -C /usr/share/mgcpt/apps/