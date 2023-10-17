 
from scapy.all import * 
file = rdpcap("Extraction.pcapng") 
z = bytes() 
a = [12,23,34,45,56,67,78,89,108,119,130,141,158,169,180,191,202,217,228,243,254] 
for i in range(len(a)): 
	k = bytes(file[a[i]-1]) 
	k = k[66:] 
	z += k 
print(z) 
open("flag.jpg","wb").write(z) 
 

