x = 'Hello my name is alan'
y = ',how are you?'
print(x+y)   #concatenation

a1 = ""
a2 = " "
a3 = "1 2 3"
print(len(a1))
print(len(a2))
print(len(a3))

print('h' in x)
print('e' not in x)
print(x*5)
print(x[0])       #   x[i]     The i (lenght) item of string x where the first character is 0.
print(x[0:4])     #   x[i:j]   A slice from string x beginning with the character at position i through to the character at position j.
print(x[0:22:2])  #   x[i:j:k] slice of s from i to j with step k.
print(max(x))     #   every string have it's own amount which depends on ASCII code
print(x.index('m'))
print(x.index('m',7))        #  index.(sympol,i,j) the first time the number occur in range from i to j
print(x.index('l',10,20))
print(x.count('l'))          #  cpint.('sympol') shows how many time the letter occur we can add range ('l',5,10)
print(x.capitalize())
print(x.upper())             #there is also isupper() and islower() methods
print(x.lower())
print(x.isalpha())           # is it alphapatical?
print(x.isdecimal())         # is it numerical?
print(x.replace("a","i"))
#there is many other methods I recommend viewing them at least once.



