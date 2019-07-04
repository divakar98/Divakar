a=input()
li=('a','e','i','o','u')
if(a>='a' and a<='z'):
    if a in li:
        print("Vowel")
    else:
        print("Consonant")
else:
    print("Invalid")
