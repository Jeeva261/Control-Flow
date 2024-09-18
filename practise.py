# Write a Python script to find the factorial of a number using loops

num=int(input("Enter the value:"))
f=1

for i in range(1,10):
    f=f*i
    print("the factorial is:",f)


# Implement a program to print even numbers between 1 to 100

for i in range(1,101,2):
    print(i,end="  ")
