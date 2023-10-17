from scapy.all import * 
file = rdpcap("Dig_deep.pcapng") 
z = bytes() 
for i in file: 
	if TCP in i and IP in i and i[IP].src == "192.168.43.242" and i[TCP].dport == 81 and len(i) == 854: 
        	i = bytes(i) 
        	z += i[54:] 
print(z) 
open("flags","wb").write(z) 
file = open("flags","rb").read() 
z = bytes() 
for i in file: 
	z += bytes(([(i-5)%256])) 
print(z) 
open("flag.zip","wb").write(z) 
 

