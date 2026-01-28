in_string=input("enter string to convert to uppercase: ")
def convert_lower(in_string):
    str2=""
    for i in in_string:
        o=ord(i)
        if o in range(65, 91):
            o=o + 32
            i=chr(o)
            str2+=i
        else:
            str2+=i
    print("converted string is ", str2)
convert_lower(in_string)
