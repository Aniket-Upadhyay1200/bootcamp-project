import hashlib
my_string=input('Enter a string to hash by sha512 sha1 and blake2b algorithm ')
obj1=hashlib.sha512(my_string.encode())
obj2=hashlib.sha1(my_string.encode())
obj3=hashlib.blake2b(my_string.encode())
print('sha512 Hashing in byte form',obj1.digest())
print('sha1 Hashing in byte form',obj2.digest())
print('blake2b Hashing in byte form',obj3.digest())