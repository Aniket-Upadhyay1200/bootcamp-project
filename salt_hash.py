import hashlib
my_string= input('Enter string for salting and hashing')
salt='5gi89o5t'
psw=my_string + salt
h=hashlib.md5(psw.encode())
print('salted and hashed string ',h)
