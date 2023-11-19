#Networking #VM 

Bridge interface in Linux allows to connect one or multiple VMs to the same network as host.

It acts like a network switch.


- Stop `NetworkManager.service`
	``` bash
	sudo systemctl stop NetworkManager.service
	```

- Down ethernet interface to loose ip 
	``` bash
	sudo ip link set {replace_with_eth} down
	```  

- Create a bridge interface
  ``` bash
  sudo ip link add br0 type bridge
	```

- Up bridge and ethernet interfaces
  ``` bash
  sudo ip link set br0 up
  sudo ip link set {replace_with_eth} up
	```

- Connect ethernet to bridge
  ``` bash
  sudo ip link set {replace_with_eth} master br0
	```
  
- Set ip address to bridge
  ``` bash
  sudo ip addr add 192.168.0.{ip}/24 dev br0
	```