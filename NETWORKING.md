## namespace commands

```
ip netns list
sudo ip netns del <namespace-name>
sudo ip netns exec <namespace-name> bash
```

```
sudo ip netns exec ns1 ip link set vethin2 mtu 3400
sudo ip link set vethout2 mtu 3400
sudo ip link set enp24s0np0 mtu 3600
```