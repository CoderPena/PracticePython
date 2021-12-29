x = int(input("Type a integer number: "))

# THIS
a = range(1, x+1)
b = []

for elem in a:
   if x % elem == 0:
      b.append(elem)
      
print(b)

# OR THIS

print([i for i in range(1, x+1) if x % i == 0])
