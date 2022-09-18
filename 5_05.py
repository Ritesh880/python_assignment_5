#Write a python script which takes a three digit number from the user and displays
#only its first digit.

num=int(input("enter three digit number "))
num//=100
print(num)