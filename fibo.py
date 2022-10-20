# Program to display the Fibonacci sequence up to n-th term
from tkinter import Variable


nterms = int(input("How many terms? "))

# first two terms
# n1, n2 = 0, 1

n1 = 0
n2 = 1
count = 0

# check if the number of terms is valid
if nterms <= 0:
   print("Please enter a positive integer")
# if there is only one term, return n1
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
# generate fibonacci sequence
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1

fibonacci = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

print(fibonacci)
print(fibonacci[0])
print(len(fibonacci))

for x in fibonacci:
 print(x)

fibonacci.append(89)
print(fibonacci)

