# while loop

x=1
while x<6:
    print(x)
    x+=1
    if x==3:
        continue
else:
  print("i is no longer less than 6")

# for loop

furits=["apple","banana","orange",]
for x in furits :
    print(x)
    if x=="banana":
        continue
    print(x)

for x in range(1,6):
    if (x == 3):
        pass
    print(x)

for x in range(2,4):
    print(x)
    for y in range(1,10):
        print("   *")

furits=["apple","orange","banana"]
veg=["onion","Cabbage"]
for i in furits:
    print(i)
    for j in veg:
        print("  ",j)


for i in range(1,10):
    print()
    for j in range(1,i+1):
        print(j,end="  ")


count=0
for i in range (10):
    if i%2==0:
        count=count+1
print(count)

for i in "myblog":
    print(i,"?")

for i in range(1,11):
    print(i)
even=0
for i in range(1,21):
    if (i%2==0):
        even=even+1
        print(i)

print(even)

for i in range (20,0,-2):
   print(i)

num=int(input("enter the value"))
for x in range(1,11):
    print(num*x)

for i in range(1,11):
    print("3x",i,"=",i*3)

for x in range(0,11):
    x=x*2
    print(x)

vowel=['a','e','i','o','u']
string="pythonprogramming"
count=0
for i in string:
    if i in vowel:
     count+=1

print(count)


a2b="jeeva"
a3b="vidhya"
count=0
for i in  a2b :
    if i in a3b:
        count+=1
print(count)

num=int(input("Enter the number:"))
f=1
for i in range(1,num+1):
    f=f*i
    print("factorial is:",f)

f=1
for i in range (1,6):
    f=f*i
    print(f)


ampt=3
crt_user_name="jeeva"
crt_pass_word=1234
success=0

while (ampt>0):
    user_name=str(input("username:"))
    pass_word=int(input("password:"))
    ampt=ampt-1
    if (user_name==crt_user_name and pass_word==crt_pass_word):
        print("valid login")
        success=1
        break
else:
    print("invalid login")


# fibonacci series

num=10
first=1
sec=2
for x in range(10):
    ampt=first+sec
    print(ampt)
    first=sec
    sec=ampt



fuction=2
while (fuction<5):
    print(fuction)
    fuction+=1




