import random
#Here I imported random libary
print("Hi welcome to the random guess game")
#Here I printed some message
start=int(input("Enter the number from start: "))
end=int(input("Enter the number from end: "))
#Here I will take 2 input from the user first is to start the random number the second is to end the random number
random=random.randint(start,end)
#Here I tell the computer to think number between start input and end input
guess1=int(input("Enter the random number: "))
#Here I will take input from the user of random number
if(guess1==random):
    print("You won")
#Here I will check that the input is matching to the computer random number if it's matching then it will print you won
else:
 print("ops you lose")
#Here I will check that the input not match to the computer random number if not then it wil print ops you lose
print("The number is",random)