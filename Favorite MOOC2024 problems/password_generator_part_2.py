# Write your solution here
import string
from random import randint

def generate_strong_password(length : int,a:bool,b:bool):
    lowercase_chars = list(string.ascii_lowercase)
    no="0123456789"
    ch="!?=+-()#"
    c=1
    if a==True:
        lowercase_chars+=no
        c+=1
    if b==True:
        lowercase_chars+=ch
        c+=1
    parola = ""
    for i in range(length-c):
        random_index = randint(0, len(lowercase_chars)-1)
        parola += lowercase_chars[random_index]
    if a==True:
        parola+=no[randint(0,len(no)-1)]
    if b==True:
        parola+=ch[randint(0,len(ch)-1)]
    parola+=lowercase_chars[randint(0,len(lowercase_chars)-1)]



    return parola

if __name__=="__main__":
    print(generate_strong_password(10,True,True))