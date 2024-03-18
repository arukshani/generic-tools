```
sudo tcpdump -i enp24s0np0 -w L1_server_5s.pcap
sudo tcpdump -i enp24s0np0 -w L1_server_5s.pcap
```

```
tcp.analysis.retransmission or tcp.analysis.fast_retransmission
tcp.dstport
tcp.port

-T fields -e tcp.seq

frame.time_relative
```