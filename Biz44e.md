### Biz44e
We may infer from the analysis of numerous packets that ICMP needs to be used in some way.
 Apply the ICMP filter and begin your analysis.
 We can observe that several ZIP Magic Numbers are present in the packets coming from source 10.30.8.102 and destination 192.168.42.83.
 There are numerous methods for extracting data in Scapy.
 Here, we can simply extract the content because each packet's length varies.
 Apply a filter to the slices in order to prevent the undesirable chunks.
 The ZIP's hex code can be used to identify it.
![image](https://github.com/swetaajit/NetworkForensics/assets/92258994/1fc493a0-7c3f-43d5-aa1e-8236ffcc81ae)

 
## scapy code

from scapy.all import *

def extract_icmp_payload(pcap_file, output_file):

    with open(output_file, "wb") as output:
    
        for packet in rdpcap(pcap_file):
        
            if packet.haslayer(ICMP):
            
                icmp_packet = packet[ICMP]
                
                if icmp_packet.haslayer(Raw):
                
                    payload = icmp_packet[Raw].load
                    
                    output.write(payload)


input_pcap_file = "your_input.pcap"

output_text_file = "extracted_payload.txt"


extract_icmp_payload(input_pcap_file, output_text_file)

![image](https://github.com/swetaajit/NetworkForensics/assets/92258994/691bb51d-467f-46f5-a05a-8b2c5fcce5a8)
