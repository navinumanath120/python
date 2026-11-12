n=int(input("Enter the limit:"))
li=[]
c=0
for i in range(n):
    x=input("Enter the name:")
    li.append(x)
for i in li:
    for j in i:
        if 'a' in j.lower():
            c=c+1
print("The occurrence of 'a' is: ",c)