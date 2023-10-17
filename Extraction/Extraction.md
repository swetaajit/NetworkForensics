## Extarction
After applying the filter data in wireshark you TCP packets with frame ranging from 12 to 254
![image](https://user-images.githubusercontent.com/92258994/209705792-3d3731de-d193-412d-a2ee-f361d39dd64d.png)

![image](https://user-images.githubusercontent.com/92258994/209705768-db4fd182-a288-4eb0-94d1-fad6e08f0ccb.png)

After creating a scapy python code to exract a jpg file from the given frame you get a flag.jpg.

```
binwalk -e flag.jpg
```

helps you extract the two files inside the jpg file.
This includes a zip file 1BE2.zip  and pdf file  flag.pdf .
After comaparing the password of the zip file using rockyou.txt you get the password Mypassword.
This helps you inflate the flag.pdf 
using the pdftoetxt file you can convert this into a flag.txt file .
![image](https://user-images.githubusercontent.com/92258994/209705875-81681d5c-c2a4-4649-a05a-e4e138cbe9e1.png)


cat the contents and you get the flag.
```
shaktictf{h0p3_y0u_ar3_enj0ying_thi5}
```
