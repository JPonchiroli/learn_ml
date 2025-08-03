kmh = [40, 50, 56, 64, 73, 79, 85, 96, 100, 120]

mph1 = []

for i in kmh:
  mph1.append(i / 1.61)
print(mph1)


mph2 = list(map(lambda x: x / 1.61, kmh)) # Lambda
print(mph2)

mph3 = [x / 1.61 for x in kmh] # List Comprehension
print(mph3)