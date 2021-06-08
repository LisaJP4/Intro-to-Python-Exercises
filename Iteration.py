animals = ["cow", "pig", "duck"]

animals.append("sheep")

for animal in animals:
    print(animal)

for i in range(0, 51, 2):
    print(i)

for i in range (20):
    if i == 5:
        continue
    print(i)

for i in range(3):
    for j in range(4):
        print(i, "x", j, "=", i*j)

        
count = 0
name = str(input("What is your name?"))

while count < 5:
    print(name, "is awesome!")
    count += 1

count = 2
name = str(input("What team do you support?"))

while count < 10:
    print(name, "is fantastic!")
    count += 1