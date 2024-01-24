# Redbelly Node Utilities

## CheckSync

CheckSync is a utility to find your RPC's block height against to one of the main nodes in redbelly devnet.

### Requirements

You will need python, git and curl installed in your system. 

#### Python

If you are using a Linux or Apple computer with MacOS, you can use the python provided with the operating system.
There is no need to install additional libraries/modules.

If you are using Microsoft Windows, please use the link below to download and follow the instructions to install into your computer.

Any version newer than 3.6 should be ok.

    https://www.python.org/downloads/

#### Curl

Curl is a widely used application to interact with web services.

If you are using Linux or Freebsd, you can install curl using your distribution's package manager:

For ubuntu/debian and derivatives:

    ilker@t440s $ sudo apt install curl

For redhat/fedora and derivatives:

    ilker@t440s $ sudo dnf install curl
   
For freebsd and derivatives:

    $ sudo pkg update
    $ sudo pkg upgrade
    $ sudo pkg install curl
    
For windows 10/11 there is a stripped down version of curl that is maintained by
Microsoft already installed. If you want to have the full featured curl, please
download the appropriate version from:

   https://curl.se/windows/


## Installation

You can download the package from releases, or you can use git command to clone the application. 

You can clone this repository using:

    git clone https://github.com/ilkermanap/redbelly-utils


## How to Run

Using your command line, please go to the directory where you cloned/unzipped the application.

Run the command as shown below. At first, application will query the RPC's two times, to have enough information to calculate the sync speed.

   ilker@t440s:~/src/redbelly-utils$ python3 checksync.py https://redbelly.manap.se:8545
   This is the first check for https://rbn-gcp-australia-southeast1-a-0-b-v2.devnet.redbelly.network:8545. I will wait for 10 seconds and check again
   This is the first check for https://redbelly.manap.se:8545. I will wait for 10 seconds and check again  
   --------------------------------------------------
   URL          :  https://rbn-gcp-australia-southeast1-a-0-b-v2.devnet.redbelly.network:8545
   Block Height :  42105
   Sync Speed   :  0.0
   Time to sync :  0
   --------------------------------------------------
   URL          :  https://redbelly.manap.se:8545
   Block Height :  42105
   Sync Speed   :  0.0
   Time to sync :  0


   Your node is in sync with https://rbn-gcp-australia-southeast1-a-0-b-v2.devnet.redbelly.network:8545 at block number 42105

