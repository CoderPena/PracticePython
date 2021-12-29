a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 8,4,2,9]
b = []
x = int(input("Type a integer number: "))
for elem in a:
   if elem < x:
      b.append(elem)
      
print(b)
