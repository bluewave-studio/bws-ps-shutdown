#!/bin/bash

if [ "$EUID" -ne 0 ]
  then echo "Please run with sudo."
  exit
fi

echo "Installing bws-shutdown script"
cp bws-shutdown.py /usr/local/bin/
chmod +x /usr/local/bin/bws-shutdown.py

echo "Installing bws-ps service"
cp bws-ps /etc/init.d/
chmod +x /etc/init.d/bws-ps
sudo update-rc.d bws-ps defaults

echo "Starting bws-ps service"
service bws-ps start
