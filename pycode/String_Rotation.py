string1 = "AACD"
string2 = "ACDAE"

temp = string1 + string1

if temp.count(string2) > 1:
    print"Strings are rotation of each other"
else:
    print"Strings are not rotation of each other"