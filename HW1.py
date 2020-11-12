####### Homework 1

####### Maksym Bilyi, ID: 101169

# Step 1: declaring variables
import random as random

random.seed(66627)
A = random.randrange(0, 20, 1)
B = random.randrange(30, 40, 1)

print(A)
print(B)

# Step 2: checking variable types. Result: <class 'int'>
type(A)
type(B)

# Step 3: programming prime numbers
for prm in range(A,B):
    if all(prm%i!=0 for i in range(2,prm)):
       print (prm)
