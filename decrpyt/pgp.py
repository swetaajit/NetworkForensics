from scapy.all import * 
file = rdpcap("Decrypt.pcap") 
z = bytes() 
for i in file: 
	if DNS in i: 
    	  j = bytes(i) 
    	  if len(j) > 400:
            j = j[224:] 
            z += j 
print(z) 
open("img.png","wb").write(z)

