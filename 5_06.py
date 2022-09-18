'''Write a python script which takes a three digit number from the user and displays
only its middle digit.'''

num=int(input("enter three digit number "))
num//=10
num%=10
print("middle digit of entered number is ",num)
