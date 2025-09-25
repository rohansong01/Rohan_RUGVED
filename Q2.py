a=input("Enter the string: ")
str_ls=sorted(a)
print("The sorted array is: ")
for i in range(0,len(a)):
    print(str_ls[i], end="")

print("")
for i in set(str_ls):
     print(i+" frequency is: "+ str(a.count(i)))