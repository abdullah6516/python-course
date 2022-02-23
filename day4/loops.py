for x in range(1, 10):    # try (10) and (1,10,2) try break and continue
    print(x)
print("All done")


word = "Hello"   # try ["Hello"] and ["Hello" , "Hi" , "Nice to meet you"]
for x in word:
    print(x)
print("Done")

x = 10
while x != 15 :
    print(x)
    x = x + 1


for outer in ['first' , 'second' , 'third'] :
    print(outer)
    for inner in range (1,4):
        print(inner)