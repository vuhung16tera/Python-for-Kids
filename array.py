cars = ["Ford", "Volvo", "BMW"]
print(cars)
print(cars[0])
print(len(cars))

for x in cars:
 print(x)

cars.append("Honda")
print(cars)
print(len(cars))

cars[0] = "Toyota"
print(cars)

cars.sort()

naturalnumbers = [1, 4, 6, 8, 12, 9, 12, 20, 8]
print(naturalnumbers)
naturalnumbers.sort()
# naturalnumbers.sort(reverse=True)
print(naturalnumbers)

x = naturalnumbers.count(4)
print (x)