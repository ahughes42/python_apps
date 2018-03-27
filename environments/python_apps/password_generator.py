import random

chars = 'abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&Z*()ABCDEFGHIJKLMNOPQRSTUV'
num_of_passwords = input('How many passowrds should I generate?: ')
num_of_passwords = int(num_of_passwords)
length = input('Password length?: ')
length = int(length)
passwords = []

for p in range(num_of_passwords):
    password = ''
    for c in range(length):
        password += random.choice(chars)
    passwords.append(password)

print(passwords)