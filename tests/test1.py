from passgenpy.generate_password import gen_pass

passwrd_len = int(input("Enter the length of the password that will be generated:\n"))
passwrd = ""
passwrd = gen_pass(passwrd_len, passwrd)
print(passwrd)
