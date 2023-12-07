# Password Generator

import random,string

password_length= int(input("Enter the length of password you want: "))

characters= string.ascii_letters + string.digits +string.punctuation +string.ascii_uppercase
password= ""

for index in range(password_length):
    password= password + random.choice(characters)

print("Generated password : {}" .format(password))


