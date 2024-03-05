import random
import string

pass_len=12
charvaluse=string.ascii_letters+string.punctuation+string.digits

password=""
for i in range(pass_len):
    password += random.choice(charvaluse)

print("your random password is :",password)