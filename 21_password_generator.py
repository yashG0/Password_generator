    # Password Generator script

import string
import random as rm


# if __name__ =="__main__":
#     s1 = string.ascii_lowercase
#     # print(s1)
#     s2 = string.ascii_uppercase
#     # print(s2)
#     s3 = string.digits
#     # print(s3)
#     s4 = string.punctuation
#     # print(s4)
#     plen = input("Enter password length: ")
#     plen = int(plen)
#     s = []
#     s.extend(21)
#     print(s)

s1 = string.ascii_lowercase
s2 = string.ascii_uppercase
s3 = string.ascii_letters
s4 = string.punctuation

while True:

    plen = input("Enter length of the password: ")    
    if plen.isnumeric():
        plen = int(plen)
        break
    else:
        continue
     


# passwd = int(passwd)
s = []
s.extend(list(s1))
s.extend(list(s2))
s.extend(list(s3))
s.extend(list(s4))
# print(s)
print("After shuffle")
rm.shuffle(s)
# print(s)
print("Your strong password is : ")
print("".join(s[0:plen]))

