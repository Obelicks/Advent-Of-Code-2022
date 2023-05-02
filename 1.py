with open("data/1.txt") as file:
      data_1 = [i for i in file.read().strip().split('\n')]
list = []
total = 0
for x in data_1:
  if x == "":
    list.append(total)
    total =0
  else:
    total += int(x)
list.sort(reverse=True)
print(list[:3])
sum = 0
for i in (list[:3]):
   sum += i
print(sum)