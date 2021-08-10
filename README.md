# Raspberry Pi - Python Server GPIO command
* This is to demonstrate how to get easily GPIO header pin pull (down/up) from a http request

### Requirements
* Raspberry pi with internet connectivity (and with something to attach and interact with)
* Windows/mac/Linux PC with internet connectivity
* Possible router or common access-point (or straight connection between devices) to PC and Raspberry pi, and possibility to configure it (for static ip's)

## Configuration
1. install basic rasbian to microSD for raspberry pi to run on, no need to have graphical UI
2. for basic user usually named `pi` ( **password** `raspberry`) has home directory where you start, create folder with name you like `mkdir <foldername>` and then run less secure priviledges to whole folder with `chmod 755 <foldername>` (its easier for file transfers this way) (chmod a (everyone) +w and +x are for write and run, chmod 777 are for user groups and 1-7 amount of "openess")
3. for convenience, after you have made connection to network with raspberry `sudo raspi-config` and under *System Options* LAN or Wireless LAN, make sure to leash/make pi's ip address static (tied to mac address in example).
4. _optional_: under *Interface Options* there is SSH which you can enable to have direct commandline access from computer.
5. to connect to rasbperry with SSH remember to make rasbperry to be known_host or use PUTTY to create that for you with prompt. `ssh -R 52698:localhost:52698 pi@192.168.xx.xx`


## Installation

#### On Raspberry

```sh
sudo apt-get install python-pip
# try to see if RPi it is available
pip freeze | grep RPi

# for python2
sudo apt-get install python-dev python-rpi.gpio
# or
pip install RPi.GPIO

# for python3
sudo apt-get install python3-dev python3-rpi.gpio

sudo apt-get install python3-flask
```

'till this point we have 
* python, for running code
* flask, for creating simple server

and
* rpi.gpio library to make a use of physical GPIO pins with python

#### On PC
On windows 
* Putty, to ssh
* WinSCP, to filetransfer
* ngrok, to route raspberry server to available for public internet


## Running
* Run app.py on raspberry with command
```sh
python3 app.py
```