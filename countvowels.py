strv=input("enter a string to count vowels: ")
vowels=['a', 'e', 'i', 'o', 'u']
strl=strv.lower()
count=0
for i in strl:
    for j in vowels:
        if i== j:
            count+=1
print("There are ", count, "vowels in input string")
