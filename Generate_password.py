import random
import string
def joint(let, num):
    return "".join(random.choice(let) for i in range(num))
len_password=5
while(len_password < 6):
    len_password = int(input("Enter the length of password: "))

L=int(input("Number of Letter in password: "))

I=int(input("Number of digit in password: "))
# generate random alphabets(lowwer case and upper case)
letter=string.ascii_letters
# generate random digits
d=string.digits
# generate random special characters
p=string.punctuation

g_password=""
p1= joint(letter,L)
p2=joint(d,I)
p3=joint(p,len_password-I-L)
g_password =g_password + p1 + p2 + p3

random.sample(g_password,len(g_password))

print(g_password)