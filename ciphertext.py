def decrypt(msg,x):
    msg_mod=""
    for i in range(len(msg)):
        a=msg[i]
        if(a.isupper()):
            msg_mod=msg_mod+chr((ord(a)-x-65)%26 + 65)
        elif(a.islower()):
            msg_mod=msg_mod+chr((ord(a)-x-97)%26 + 97)
        elif(a==" "):
            msg_mod=msg_mod+" "
        elif(a=="'"):
            msg_mod=msg_mod+"'"
        elif(a=="."):
            msg_mod=msg_mod+"."
            
    return msg_mod

msg= "payzgmuujurjigkygxiovnkxlcgihubb"
for x in range(1,26):
    decrypted = decrypt(msg,(x-2))
    print(x,decrypted)

