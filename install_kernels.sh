#!/bin/bash

# install required packages
# export DEBIAN_FRONTEND=noninteractive DEBCONF_NONINTERACTIVE_SEEN=true
# sudo debconf-set-selections kexec-preseed.txt
# sudo apt-get install -y build-essential libncurses-dev bison flex libssl-dev libelf-dev kexec-tools python3 python3-pip binutils
# sudo apt install dwarves
# pip install numpy pandas matplotlib cycler

# # set default boot to current (vanila) kernel
# echo "GRUB_DEFAULT=\"Advanced options for Ubuntu>Ubuntu, with Linux $(uname -r)\"" | sudo tee -a /etc/default/grub

cd linux-5.15.1
# cd linux-5.9.9
# cp /boot/config-`uname -r` .config
# yes '' | make oldconfig
make clean
# make ARCH=x86
time make -j`nproc` bzImage
# time make -j`nproc` bzImage > /users/rukshani/log_std_5_15.txt 2> /users/rukshani/log_err_5_15.txt
# make -j $(nproc)
# sudo make modules_install
# sudo make install


