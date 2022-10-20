i = 0
sum = 0
n = 64

while i < n:
  sum = sum + 2**i
  i += 1

print(sum)

# print (2**64 - 1)

# Wolfram
# 1 + 2 + 4 + 8 + ... + 2^63 = 2^64 - 1

# Python

# 2**0 + 2**1 + 2**2 + ... + 2**n = 2**(n+1) - 1 