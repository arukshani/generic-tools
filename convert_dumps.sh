#/bin/bash

for arg in "$@"
do
case $arg in
    -f|--file_name)
        shift
        file_name=$1
        shift
        ;;
esac
done

path="/Users/rukshani/Documents/Opera"
file_name="L1_client_3s"

# tshark -2 -r $path/$file_name.pcap -R "tcp.srcport == 45604" -T fields -e frame.time -e ip.src -e ip.dst -e tcp.seq > $path/$file_name.csv

tshark -2 -r $path/$file_name.pcap -R "tcp.analysis.retransmission" -T fields -e frame.time -e ip.src -e ip.dst -e tcp.seq > $path/rt_L1_client_3s.csv