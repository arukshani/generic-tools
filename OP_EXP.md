
## O TCP 3s
```
L1_client_3s
L2_server_3s
```

## O TCP 5s
```
Retransmissions reported from iperf - 
Connecting to host 10.1.0.1, port 5020
[  5] local 10.0.0.1 port 49130 connected to 10.1.0.1 port 5020
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  1.08 GBytes  9.31 Gbits/sec  390    983 KBytes
[  5]   1.00-2.00   sec  1.09 GBytes  9.33 Gbits/sec    0   1.04 MBytes
[  5]   2.00-3.00   sec  1.09 GBytes  9.33 Gbits/sec    1   1.09 MBytes
[  5]   3.00-4.00   sec  1.09 GBytes  9.33 Gbits/sec    1   1.13 MBytes
[  5]   4.00-5.00   sec  1.09 GBytes  9.33 Gbits/sec  482   1.14 MBytes
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-5.00   sec  5.43 GBytes  9.33 Gbits/sec  874             sender
[  5]   0.00-4.53   sec  5.43 GBytes  10.3 Gbits/sec                  receiver

## try2

Connecting to host 10.1.0.1, port 5020
[  5] local 10.0.0.1 port 35352 connected to 10.1.0.1 port 5020
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  1.08 GBytes  9.31 Gbits/sec  117    857 KBytes
[  5]   1.00-2.00   sec  1.09 GBytes  9.33 Gbits/sec    0    861 KBytes
[  5]   2.00-3.00   sec  1.09 GBytes  9.33 Gbits/sec   11    988 KBytes
[  5]   3.00-4.00   sec  1.09 GBytes  9.33 Gbits/sec    1   1.03 MBytes
[  5]   4.00-5.00   sec  1.09 GBytes  9.33 Gbits/sec    1    915 KBytes
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-5.00   sec  5.43 GBytes  9.33 Gbits/sec  130             sender
[  5]   0.00-4.54   sec  5.43 GBytes  10.3 Gbits/sec                  receiver
```

## 100s with tcp_reordering: default 3

dathapathu@leed-01:~$ iperf3 -c 10.1.0.1 -p 5201 -t 100
Connecting to host 10.1.0.1, port 5201
[  5] local 10.0.0.1 port 36622 connected to 10.1.0.1 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  1.09 GBytes  9.33 Gbits/sec  182    800 KBytes
[  5]   1.00-2.00   sec  1.09 GBytes  9.33 Gbits/sec    0    806 KBytes
[  5]   2.00-3.00   sec  1.09 GBytes  9.33 Gbits/sec    1    933 KBytes
[  5]   3.00-4.00   sec  1.09 GBytes  9.34 Gbits/sec    0   1011 KBytes
[  5]   4.00-5.00   sec  1.09 GBytes  9.33 Gbits/sec    0   1011 KBytes
[  5]   5.00-6.00   sec  1.09 GBytes  9.33 Gbits/sec    0   1.03 MBytes
[  5]   6.00-7.00   sec  1.09 GBytes  9.33 Gbits/sec    0   1.05 MBytes
[  5]   7.00-8.00   sec  1.09 GBytes  9.33 Gbits/sec    7    908 KBytes
[  5]   8.00-9.00   sec  1.09 GBytes  9.33 Gbits/sec    0    998 KBytes
[  5]   9.00-10.00  sec  1.09 GBytes  9.33 Gbits/sec    0   1.02 MBytes
[  5]  10.00-11.00  sec  1.09 GBytes  9.33 Gbits/sec    0   1.05 MBytes
[  5]  11.00-12.00  sec  1.09 GBytes  9.33 Gbits/sec    8    830 KBytes
[  5]  12.00-13.00  sec  1.09 GBytes  9.33 Gbits/sec    0    953 KBytes
[  5]  13.00-14.00  sec  1.09 GBytes  9.33 Gbits/sec    0   1011 KBytes
[  5]  14.00-15.00  sec  1.09 GBytes  9.33 Gbits/sec    0   1011 KBytes
[  5]  15.00-16.00  sec  1.09 GBytes  9.33 Gbits/sec    0   1.02 MBytes
[  5]  16.00-17.00  sec  1.09 GBytes  9.33 Gbits/sec    0   1.05 MBytes
[  5]  17.00-18.00  sec  1.09 GBytes  9.33 Gbits/sec    0   1.07 MBytes
[  5]  18.00-19.00  sec  1.09 GBytes  9.33 Gbits/sec    3    881 KBytes
[  5]  19.00-20.00  sec  1.09 GBytes  9.33 Gbits/sec    7    788 KBytes
[  5]  20.00-21.00  sec  1.09 GBytes  9.33 Gbits/sec    0    891 KBytes
[  5]  21.00-22.00  sec  1.09 GBytes  9.33 Gbits/sec    0    987 KBytes
[  5]  22.00-23.00  sec  1.09 GBytes  9.33 Gbits/sec    0   1.02 MBytes
[  5]  23.00-24.00  sec  1.09 GBytes  9.34 Gbits/sec    0   1.05 MBytes
[  5]  24.00-25.00  sec  1.09 GBytes  9.33 Gbits/sec    8    786 KBytes
[  5]  25.00-26.00  sec  1.09 GBytes  9.33 Gbits/sec    0    932 KBytes
[  5]  26.00-27.00  sec  1.09 GBytes  9.33 Gbits/sec    0   1018 KBytes
[  5]  27.00-28.00  sec  1.09 GBytes  9.33 Gbits/sec    1    793 KBytes
[  5]  28.00-29.00  sec  1.09 GBytes  9.33 Gbits/sec    0    939 KBytes
[  5]  29.00-30.00  sec  1.09 GBytes  9.33 Gbits/sec    0   1021 KBytes
[  5]  30.00-31.00  sec  1.09 GBytes  9.33 Gbits/sec    0   1.05 MBytes
[  5]  31.00-32.00  sec  1.09 GBytes  9.33 Gbits/sec    0   1.07 MBytes
[  5]  32.00-33.00  sec  1.09 GBytes  9.33 Gbits/sec    0   1.08 MBytes
[  5]  33.00-34.00  sec  1.09 GBytes  9.33 Gbits/sec    0   1.10 MBytes
[  5]  34.00-35.00  sec  1.09 GBytes  9.33 Gbits/sec    0   1.11 MBytes
[  5]  35.00-36.00  sec  1.09 GBytes  9.33 Gbits/sec    2    921 KBytes
[  5]  36.00-37.00  sec  1.09 GBytes  9.33 Gbits/sec    0   1008 KBytes
[  5]  37.00-38.00  sec  1.09 GBytes  9.33 Gbits/sec    0   1.04 MBytes
[  5]  38.00-39.00  sec  1.09 GBytes  9.34 Gbits/sec    0   1.06 MBytes
[  5]  39.00-40.00  sec  1.09 GBytes  9.33 Gbits/sec    0   1.08 MBytes
[  5]  40.00-41.00  sec  1.09 GBytes  9.33 Gbits/sec    0   1.10 MBytes
[  5]  41.00-42.00  sec  1.09 GBytes  9.33 Gbits/sec    1   1.11 MBytes
[  5]  42.00-43.00  sec  1.09 GBytes  9.33 Gbits/sec    0   1.12 MBytes
[  5]  43.00-44.00  sec  1.09 GBytes  9.33 Gbits/sec    0   1.13 MBytes
[  5]  44.00-45.00  sec  1.09 GBytes  9.33 Gbits/sec    0   1.13 MBytes
[  5]  45.00-46.00  sec  1.09 GBytes  9.33 Gbits/sec    0   1.14 MBytes
[  5]  46.00-47.00  sec  1.09 GBytes  9.33 Gbits/sec    0   1.18 MBytes
[  5]  47.00-48.00  sec  1.09 GBytes  9.33 Gbits/sec    0   1.19 MBytes
[  5]  48.00-49.00  sec  1.09 GBytes  9.33 Gbits/sec    0   1.26 MBytes
[  5]  49.00-50.00  sec  1.09 GBytes  9.33 Gbits/sec    0   1.26 MBytes
[  5]  50.00-51.00  sec  1.09 GBytes  9.33 Gbits/sec    0   1.48 MBytes
[  5]  51.00-52.00  sec  1.09 GBytes  9.33 Gbits/sec    0   1.48 MBytes
[  5]  52.00-53.00  sec  1.09 GBytes  9.33 Gbits/sec    2   1.04 MBytes
[  5]  53.00-54.00  sec  1.09 GBytes  9.33 Gbits/sec    6    812 KBytes
[  5]  54.00-55.00  sec  1.09 GBytes  9.33 Gbits/sec    0    936 KBytes
[  5]  55.00-56.00  sec  1.09 GBytes  9.33 Gbits/sec    6    942 KBytes
[  5]  56.00-57.00  sec  1.09 GBytes  9.33 Gbits/sec    0    943 KBytes
[  5]  57.00-58.00  sec  1.09 GBytes  9.33 Gbits/sec    6    766 KBytes
[  5]  58.00-59.00  sec  1.09 GBytes  9.33 Gbits/sec    0    926 KBytes
[  5]  59.00-60.00  sec  1.09 GBytes  9.33 Gbits/sec    8    884 KBytes
[  5]  60.00-61.00  sec  1.09 GBytes  9.33 Gbits/sec    4    850 KBytes
[  5]  61.00-62.00  sec  1.09 GBytes  9.33 Gbits/sec    1    909 KBytes
[  5]  62.00-63.00  sec  1.09 GBytes  9.34 Gbits/sec    6    790 KBytes
[  5]  63.00-64.00  sec  1.09 GBytes  9.33 Gbits/sec    3    864 KBytes
[  5]  64.00-65.00  sec  1.09 GBytes  9.33 Gbits/sec    0    967 KBytes
[  5]  65.00-66.00  sec  1.09 GBytes  9.33 Gbits/sec    5    823 KBytes
[  5]  66.00-67.00  sec  1.09 GBytes  9.33 Gbits/sec    1    928 KBytes
[  5]  67.00-68.00  sec  1.09 GBytes  9.33 Gbits/sec    1   1008 KBytes
[  5]  68.00-69.00  sec  1.09 GBytes  9.33 Gbits/sec    0   1.03 MBytes
[  5]  69.00-70.00  sec  1.09 GBytes  9.33 Gbits/sec    0   1.06 MBytes
[  5]  70.00-71.00  sec  1.09 GBytes  9.33 Gbits/sec    0   1.07 MBytes
[  5]  71.00-72.00  sec  1.09 GBytes  9.33 Gbits/sec    9    839 KBytes
[  5]  72.00-73.00  sec  1.09 GBytes  9.33 Gbits/sec    3    833 KBytes
[  5]  73.00-74.00  sec  1.09 GBytes  9.33 Gbits/sec    0    953 KBytes
[  5]  74.00-75.00  sec  1.09 GBytes  9.34 Gbits/sec    0   1.00 MBytes
[  5]  75.00-76.00  sec  1.09 GBytes  9.33 Gbits/sec    0   1.04 MBytes
[  5]  76.00-77.00  sec  1.09 GBytes  9.34 Gbits/sec    0   1.06 MBytes
[  5]  77.00-78.00  sec  1.09 GBytes  9.33 Gbits/sec    0   1.06 MBytes
[  5]  78.00-79.00  sec  1.09 GBytes  9.32 Gbits/sec    0   1.06 MBytes
[  5]  79.00-80.00  sec  1.09 GBytes  9.34 Gbits/sec    2    870 KBytes
[  5]  80.00-81.00  sec  1.09 GBytes  9.33 Gbits/sec    0    971 KBytes
[  5]  81.00-82.00  sec  1.09 GBytes  9.33 Gbits/sec    0   1.02 MBytes
[  5]  82.00-83.00  sec  1.09 GBytes  9.33 Gbits/sec    4    878 KBytes
[  5]  83.00-84.00  sec  1.09 GBytes  9.33 Gbits/sec    0    980 KBytes
[  5]  84.00-85.00  sec  1.09 GBytes  9.33 Gbits/sec    0   1.01 MBytes
[  5]  85.00-86.00  sec  1.09 GBytes  9.33 Gbits/sec    7    793 KBytes
[  5]  86.00-87.00  sec  1.09 GBytes  9.33 Gbits/sec    1    786 KBytes
[  5]  87.00-88.00  sec  1.09 GBytes  9.33 Gbits/sec    0    874 KBytes
[  5]  88.00-89.00  sec  1.09 GBytes  9.33 Gbits/sec    0    974 KBytes
[  5]  89.00-90.00  sec  1.09 GBytes  9.33 Gbits/sec    0    981 KBytes
[  5]  90.00-91.00  sec  1.09 GBytes  9.33 Gbits/sec    0    981 KBytes
[  5]  91.00-92.00  sec  1.09 GBytes  9.33 Gbits/sec    0    984 KBytes
[  5]  92.00-93.00  sec  1.09 GBytes  9.33 Gbits/sec    0   1.01 MBytes
[  5]  93.00-94.00  sec  1.09 GBytes  9.33 Gbits/sec    9    894 KBytes
[  5]  94.00-95.00  sec  1.09 GBytes  9.33 Gbits/sec   11    790 KBytes
[  5]  95.00-96.00  sec  1.09 GBytes  9.33 Gbits/sec    0    891 KBytes
[  5]  96.00-97.00  sec  1.09 GBytes  9.33 Gbits/sec    1    758 KBytes
[  5]  97.00-98.00  sec  1.09 GBytes  9.33 Gbits/sec    0    919 KBytes
[  5]  98.00-99.00  sec  1.09 GBytes  9.33 Gbits/sec    0    996 KBytes
[  5]  99.00-100.00 sec  1.09 GBytes  9.33 Gbits/sec    0   1.03 MBytes
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-100.00 sec   109 GBytes  9.33 Gbits/sec  316             sender
[  5]   0.00-90.03  sec   109 GBytes  10.4 Gbits/sec                  receiver

iperf Done.

## 100s with tcp_reordering: 300

sudo sysctl -w net.ipv4.tcp_max_reordering=300
sysctl net.ipv4.tcp_max_reordering
cat /proc/sys/net/ipv4/tcp_reordering

echo 300  > /proc/sys/net/ipv4/tcp_reordering
echo 300 | sudo tee /proc/sys/net/ipv4/tcp_reordering

dathapathu@leed-01:~$ iperf3 -c 10.1.0.1 -p 5201 -t 100
Connecting to host 10.1.0.1, port 5201
[  5] local 10.0.0.1 port 50464 connected to 10.1.0.1 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  1.09 GBytes  9.35 Gbits/sec   43    889 KBytes
[  5]   1.00-2.00   sec  1.09 GBytes  9.33 Gbits/sec  334    984 KBytes
[  5]   2.00-3.00   sec  1.09 GBytes  9.33 Gbits/sec    0   1.01 MBytes
[  5]   3.00-4.00   sec  1.09 GBytes  9.33 Gbits/sec    1    846 KBytes
[  5]   4.00-5.00   sec  1.09 GBytes  9.33 Gbits/sec    1    952 KBytes
[  5]   5.00-6.00   sec  1.09 GBytes  9.33 Gbits/sec    0   1020 KBytes
[  5]   6.00-7.00   sec  1.09 GBytes  9.34 Gbits/sec    0   1.04 MBytes
[  5]   7.00-8.00   sec  1.09 GBytes  9.33 Gbits/sec    0   1.06 MBytes
[  5]   8.00-9.00   sec  1.09 GBytes  9.34 Gbits/sec    0   1.07 MBytes
[  5]   9.00-10.00  sec  1.09 GBytes  9.33 Gbits/sec    0   1.08 MBytes
[  5]  10.00-11.00  sec  1.09 GBytes  9.33 Gbits/sec    1    905 KBytes
[  5]  11.00-12.00  sec  1.09 GBytes  9.33 Gbits/sec    0    997 KBytes
[  5]  12.00-13.00  sec  1.09 GBytes  9.33 Gbits/sec    5    875 KBytes
[  5]  13.00-14.00  sec  1.09 GBytes  9.34 Gbits/sec    0    974 KBytes
[  5]  14.00-15.00  sec  1.09 GBytes  9.33 Gbits/sec    0   1.00 MBytes
[  5]  15.00-16.00  sec  1.09 GBytes  9.33 Gbits/sec    0   1.04 MBytes
[  5]  16.00-17.00  sec  1.09 GBytes  9.33 Gbits/sec    5    882 KBytes
[  5]  17.00-18.00  sec  1.09 GBytes  9.33 Gbits/sec    0    983 KBytes
[  5]  18.00-19.00  sec  1.09 GBytes  9.33 Gbits/sec    0   1.02 MBytes
[  5]  19.00-20.00  sec  1.09 GBytes  9.33 Gbits/sec    1   1.04 MBytes
[  5]  20.00-21.00  sec  1.09 GBytes  9.33 Gbits/sec    0   1.06 MBytes
[  5]  21.00-22.00  sec  1.09 GBytes  9.33 Gbits/sec    0   1.08 MBytes
[  5]  22.00-23.00  sec  1.09 GBytes  9.33 Gbits/sec    5    921 KBytes
[  5]  23.00-24.00  sec  1.09 GBytes  9.33 Gbits/sec    7    769 KBytes
[  5]  24.00-25.00  sec  1.09 GBytes  9.33 Gbits/sec    1    916 KBytes
[  5]  25.00-26.00  sec  1.09 GBytes  9.33 Gbits/sec    1    836 KBytes
[  5]  26.00-27.00  sec  1.09 GBytes  9.33 Gbits/sec    0    953 KBytes
[  5]  27.00-28.00  sec  1.09 GBytes  9.33 Gbits/sec    3    851 KBytes
[  5]  28.00-29.00  sec  1.09 GBytes  9.33 Gbits/sec    0    930 KBytes
[  5]  29.00-30.00  sec  1.09 GBytes  9.33 Gbits/sec    0   1012 KBytes
[  5]  30.00-31.00  sec  1.09 GBytes  9.33 Gbits/sec    0   1.03 MBytes
[  5]  31.00-32.00  sec  1.09 GBytes  9.33 Gbits/sec    0   1.06 MBytes
[  5]  32.00-33.00  sec  1.09 GBytes  9.33 Gbits/sec    0   1.07 MBytes
[  5]  33.00-34.00  sec  1.09 GBytes  9.33 Gbits/sec    0   1.08 MBytes
[  5]  34.00-35.00  sec  1.09 GBytes  9.33 Gbits/sec    0   1.08 MBytes
[  5]  35.00-36.00  sec  1.09 GBytes  9.33 Gbits/sec    7    803 KBytes
[  5]  36.00-37.00  sec  1.09 GBytes  9.33 Gbits/sec    0    938 KBytes
[  5]  37.00-38.00  sec  1.09 GBytes  9.33 Gbits/sec    0   1014 KBytes
[  5]  38.00-39.00  sec  1.09 GBytes  9.33 Gbits/sec    6    816 KBytes
[  5]  39.00-40.00  sec  1.09 GBytes  9.33 Gbits/sec    0    935 KBytes
[  5]  40.00-41.00  sec  1.09 GBytes  9.33 Gbits/sec    0   1010 KBytes
[  5]  41.00-42.00  sec  1.09 GBytes  9.33 Gbits/sec    8    848 KBytes
[  5]  42.00-43.00  sec  1.09 GBytes  9.33 Gbits/sec    5    788 KBytes
[  5]  43.00-44.00  sec  1.09 GBytes  9.33 Gbits/sec    2    898 KBytes
[  5]  44.00-45.00  sec  1.09 GBytes  9.33 Gbits/sec    0    899 KBytes
[  5]  45.00-46.00  sec  1.08 GBytes  9.32 Gbits/sec   94    676 KBytes
[  5]  46.00-47.00  sec  1.09 GBytes  9.33 Gbits/sec    1    789 KBytes
[  5]  47.00-48.00  sec  1.09 GBytes  9.33 Gbits/sec    0    902 KBytes
[  5]  48.00-49.00  sec  1.09 GBytes  9.33 Gbits/sec    0    991 KBytes
[  5]  49.00-50.00  sec  1.09 GBytes  9.33 Gbits/sec   37    798 KBytes
[  5]  50.00-51.00  sec  1.09 GBytes  9.33 Gbits/sec    4    803 KBytes
[  5]  51.00-52.00  sec  1.09 GBytes  9.33 Gbits/sec    1    844 KBytes
[  5]  52.00-53.00  sec  1.09 GBytes  9.33 Gbits/sec    9    826 KBytes
[  5]  53.00-54.00  sec  1.09 GBytes  9.33 Gbits/sec    0    897 KBytes
[  5]  54.00-55.00  sec  1.09 GBytes  9.33 Gbits/sec    0    987 KBytes
[  5]  55.00-56.00  sec  1.09 GBytes  9.33 Gbits/sec    0   1.01 MBytes
[  5]  56.00-57.00  sec  1.09 GBytes  9.34 Gbits/sec    0   1.04 MBytes
[  5]  57.00-58.00  sec  1.09 GBytes  9.33 Gbits/sec    0   1.06 MBytes
[  5]  58.00-59.00  sec  1.09 GBytes  9.33 Gbits/sec    1    909 KBytes
[  5]  59.00-60.00  sec  1.09 GBytes  9.33 Gbits/sec    3    857 KBytes
[  5]  60.00-61.00  sec  1.09 GBytes  9.33 Gbits/sec    0    962 KBytes
[  5]  61.00-62.00  sec  1.09 GBytes  9.33 Gbits/sec    0   1.00 MBytes
[  5]  62.00-63.00  sec  1.09 GBytes  9.33 Gbits/sec    0   1.04 MBytes
[  5]  63.00-64.00  sec  1.09 GBytes  9.33 Gbits/sec    1   1.06 MBytes
[  5]  64.00-65.00  sec  1.09 GBytes  9.33 Gbits/sec    0   1.07 MBytes
[  5]  65.00-66.00  sec  1.09 GBytes  9.33 Gbits/sec    2    806 KBytes
[  5]  66.00-67.00  sec  1.09 GBytes  9.33 Gbits/sec    0    865 KBytes
[  5]  67.00-68.00  sec  1.09 GBytes  9.33 Gbits/sec    3    947 KBytes
[  5]  68.00-69.00  sec  1.09 GBytes  9.33 Gbits/sec    0   1017 KBytes
[  5]  69.00-70.00  sec  1.09 GBytes  9.33 Gbits/sec    0   1.03 MBytes
[  5]  70.00-71.00  sec  1.09 GBytes  9.33 Gbits/sec    0   1.06 MBytes
[  5]  71.00-72.00  sec  1.09 GBytes  9.33 Gbits/sec    0   1.07 MBytes
[  5]  72.00-73.00  sec  1.09 GBytes  9.33 Gbits/sec    0   1.08 MBytes
[  5]  73.00-74.00  sec  1.09 GBytes  9.33 Gbits/sec    0   1.09 MBytes
[  5]  74.00-75.00  sec  1.09 GBytes  9.33 Gbits/sec    0   1.12 MBytes
[  5]  75.00-76.00  sec  1.09 GBytes  9.33 Gbits/sec    0   1.16 MBytes
[  5]  76.00-77.00  sec  1.09 GBytes  9.33 Gbits/sec    0   1.27 MBytes
[  5]  77.00-78.00  sec  1.09 GBytes  9.33 Gbits/sec    0   1.27 MBytes
[  5]  78.00-79.00  sec  1.09 GBytes  9.34 Gbits/sec    8    789 KBytes
[  5]  79.00-80.00  sec  1.09 GBytes  9.33 Gbits/sec   10    748 KBytes
[  5]  80.00-81.00  sec  1.09 GBytes  9.33 Gbits/sec    0    905 KBytes
[  5]  81.00-82.00  sec  1.09 GBytes  9.33 Gbits/sec    0    996 KBytes
[  5]  82.00-83.00  sec  1.09 GBytes  9.33 Gbits/sec    0   1.02 MBytes
[  5]  83.00-84.00  sec  1.09 GBytes  9.33 Gbits/sec    0   1.05 MBytes
[  5]  84.00-85.00  sec  1.09 GBytes  9.33 Gbits/sec    0   1.07 MBytes
[  5]  85.00-86.00  sec  1.09 GBytes  9.33 Gbits/sec    0   1.09 MBytes
[  5]  86.00-87.00  sec  1.09 GBytes  9.33 Gbits/sec    0   1.10 MBytes
[  5]  87.00-88.00  sec  1.09 GBytes  9.33 Gbits/sec    0   1.10 MBytes
[  5]  88.00-89.00  sec  1.09 GBytes  9.33 Gbits/sec    0   1.11 MBytes
[  5]  89.00-90.00  sec  1.09 GBytes  9.33 Gbits/sec    0   1.12 MBytes
[  5]  90.00-91.00  sec  1.09 GBytes  9.33 Gbits/sec    0   1.12 MBytes
[  5]  91.00-92.00  sec  1.09 GBytes  9.33 Gbits/sec    0   1.12 MBytes
[  5]  92.00-93.00  sec  1.09 GBytes  9.33 Gbits/sec    0   1.12 MBytes
[  5]  93.00-94.00  sec  1.09 GBytes  9.33 Gbits/sec    0   1.13 MBytes
[  5]  94.00-95.00  sec  1.09 GBytes  9.33 Gbits/sec   13    816 KBytes
[  5]  95.00-96.00  sec  1.09 GBytes  9.33 Gbits/sec    1    831 KBytes
[  5]  96.00-97.00  sec  1.09 GBytes  9.33 Gbits/sec    0    946 KBytes
[  5]  97.00-98.00  sec  1.09 GBytes  9.33 Gbits/sec    0   1022 KBytes
[  5]  98.00-99.00  sec  1.09 GBytes  9.33 Gbits/sec    7    897 KBytes
[  5]  99.00-100.00 sec  1.09 GBytes  9.33 Gbits/sec    0    991 KBytes
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-100.00 sec   109 GBytes  9.33 Gbits/sec  631             sender
[  5]   0.00-90.03  sec   109 GBytes  10.4 Gbits/sec                  receiver

iperf Done.

### 200 to 600

echo 200 | sudo tee /proc/sys/net/ipv4/tcp_reordering
echo 500 | sudo tee /proc/sys/net/ipv4/tcp_max_reordering