import random
from genPassword import genPass


passwrd_len = int(input("Enter the length of the password that will be generated:\n"))
passwrd = ""
passwrd = genPass(passwrd_len, passwrd)
print(passwrd)
