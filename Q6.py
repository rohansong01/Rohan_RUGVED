str1=input("Enter string 1: ")
str2=input("Enter string 2: ")

l1=len(str1)
l2=len(str2)

str1=sorted(str1)
str2=sorted(str2)

str1="".join(str1)
str2="".join(str2)

if(str1==str2):
    print("The inputted strings are anagrams")
else:
    print("The inputted strings are not anagrams")    