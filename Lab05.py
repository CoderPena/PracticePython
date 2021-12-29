x = [1,4,7,9]
y = [2,3,4,9,13,1]

# THIS
a = []
for elem in x:
   if elem in y:
      a.append(elem)
      
print(a)

# OR THIS

print([i for i in x if i in y])
