Comparing files and folders

```
diff -r dir1/ dir2/
diff --brief --recursive dir1/ dir2/
diff -qr dir1/ dir2/

diff -qr linux-4.1.8/ /users/rukshani/juggler/linux-4.1/

diff linux-4.1.8/include/linux/netdevice.h /users/rukshani/juggler/linux-4.1/include/linux/netdevice.h
diff linux-4.1.8/include/linux/skbuff.h /users/rukshani/juggler/linux-4.1/include/linux/skbuff.h 
diff linux-4.1.8/Makefile /users/rukshani/juggler/linux-4.1/Makefile
diff linux-4.1.8/net/core/dev.c /users/rukshani/juggler/linux-4.1/net/core/dev.c
diff linux-4.1.8/net/core/net-sysfs.c /users/rukshani/juggler/linux-4.1/net/core/net-sysfs.c
diff linux-4.1.8/net/core/skbuff.c /users/rukshani/juggler/linux-4.1/net/core/skbuff.c
diff linux-4.1.8/net/ipv4/af_inet.c /users/rukshani/juggler/linux-4.1/net/ipv4/af_inet.c
diff linux-4.1.8/net/ipv4/tcp_offload.c /users/rukshani/juggler/linux-4.1/net/ipv4/tcp_offload.c 
```

```
<!-- wget https://cdn.kernel.org/pub/linux/kernel/v5.x/linux-5.9.9.tar.xz
tar -xf linux-5.9.9.tar.xz -->
wget https://cdn.kernel.org/pub/linux/kernel/v5.x/linux-5.15.1.tar.gz
tar -xf linux-5.15.1.tar.gz
```

## leed
```
6.2.0-39-generic
6.5.0-14-generic
```

```
Files linux-4.1.8/include/linux/netdevice.h and /users/rukshani/juggler/linux-4.1/include/linux/netdevice.h differ
Files linux-4.1.8/include/linux/skbuff.h and /users/rukshani/juggler/linux-4.1/include/linux/skbuff.h differ
Files linux-4.1.8/Makefile and /users/rukshani/juggler/linux-4.1/Makefile differ
Files linux-4.1.8/net/core/dev.c and /users/rukshani/juggler/linux-4.1/net/core/dev.c differ
Files linux-4.1.8/net/core/net-sysfs.c and /users/rukshani/juggler/linux-4.1/net/core/net-sysfs.c differ
Files linux-4.1.8/net/core/skbuff.c and /users/rukshani/juggler/linux-4.1/net/core/skbuff.c differ
Files linux-4.1.8/net/ipv4/af_inet.c and /users/rukshani/juggler/linux-4.1/net/ipv4/af_inet.c differ
Files linux-4.1.8/net/ipv4/tcp_offload.c and /users/rukshani/juggler/linux-4.1/net/ipv4/tcp_offload.c differ

Only in /users/rukshani/juggler/linux-4.1/net/ipv4: .af_inet.c.swp
Only in /users/rukshani/juggler/linux-4.1/: .config
Only in /users/rukshani/juggler/linux-4.1/net/ipv4: .tcp_offload.c.swp

```

## Patched Kernel
```
cd linux-5.9.9/
cp -r /users/rukshani/jug-new/linux-5.9/* .
```

```
export DEBIAN_FRONTEND=noninteractive DEBCONF_NONINTERACTIVE_SEEN=true
sudo debconf-set-selections kexec-preseed.txt
sudo apt-get install -y build-essential libncurses-dev bison flex libssl-dev libelf-dev kexec-tools python3 python3-pip

echo "GRUB_DEFAULT=\"Advanced options for Ubuntu>Ubuntu, with Linux $(uname -r)\"" | sudo tee -a /etc/default/grub


```