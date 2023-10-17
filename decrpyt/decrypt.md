## Decrypt

By using the filter http in wireshark you get two packets.Follow the tcp stream and you get the public key
![image](https://user-images.githubusercontent.com/92258994/209699439-187560e1-64ab-4c88-8985-62585e1f6273.png)

```
-----BEGIN PGP MESSAGE----- 
Version: OpenPGP v2.0.8 
Comment: https://sela.io/pgp/
wcBMA8fXP+32fyviAQf/T+NzsOgQ+ejW16GeK6h9WS9IDelAN9GLY5x5o9ilBlEL G4IPati4/zqd+kyV5mmA7k2eKnNByRnxElpp0PoGULX0ykjBTcXuLtNXzGWcDsFF xAkH8PduoPCcnNGWrCU6D8ZuWNtp7oeZ1krUZP+Kg9sfjjKfx0aUFhWs9SQH6mif AlbJQwxKi2xXv0UsHvg4Mz4TpVstoO5XcN9d4V+gygc+wx0K61JwAFw96xptNi9y hdMz/c7yW56JwBfwyiHvYmgLdWYJW9OEoQIj7Rwh1v8mD846vbvEDmagQ0Ra/K6q lnxa37gBFE+4kYpSXP7yqr8QMhmGDpMROJoJqxYyY9JxAe6317HZ+UUEOmNR+0tB EmPl/VVaoPc5q6RQ/cxwY4VhR4DtPsG9Gw237Sx+xSTAG5JbmtBf4KfQdVbeaXn1 PYPYBeCVL6nb6uPz6ZHBJ2SODWg9+Ssas+Gd5P7Q0zSA/35qYdamnAqUM/ujM2nN k2U= =+x+V
```

After this by putting the dns filter you understand that the packet has a .png in it which will have to be extracted 

![image](https://user-images.githubusercontent.com/92258994/209699489-fe162d52-7c52-49a2-b032-0702a85313fb.png)



It is extracted using a scapy python code which also available online


Once u get the png file which is infact QR code,you could simply scan it to get the corresponding pgp private key.
![image](https://user-images.githubusercontent.com/92258994/209700197-7f0919b5-d32d-462d-bb36-054cf5d1e8fa.png)


![image](https://user-images.githubusercontent.com/92258994/209700011-daa8f0fb-be31-46bc-9afc-e7aa1bc0ca3d.png)


And by decrypting the base64 encryption from the TCP stream of the http packet you can easily acquire the private parraphrase .

![image](https://user-images.githubusercontent.com/92258994/209700061-0ae3c772-ce4a-4ea3-a941-8c9dd9157375.png)


Using an online pgp decrytion tool you can find the flag

```
flag{eNcryP7!ng_t0_Pgp_1s_r34LLy_Pre3tY_g00D_pr1V4cyY}
```
