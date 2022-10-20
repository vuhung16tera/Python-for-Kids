sum = 0
for x in range(1001):
    if x*x % 7 != 0:
        sum = sum + x*x 
    
print(sum)



counter = 1
sum = 0
finalnumber = 999

while counter < (finalnumber + 1):
  sum = sum + counter * counter
  counter += 2

print (sum)

fileresult = open("result.txt", "w")
# convert sum from int to str (string)
fileresult.write(str(sum))
fileresult.close()

sum = 0

for x in range(6):
  print (x)
  sum = sum + x*x
  
print (sum)