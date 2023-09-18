import random
list1 = []

while len(list1) <= 8:
  a = random.randint(0, 90)
  list1.append(a)
  list1.sort()
print()

def list():
  global list1
  list2 = []
  list3 = [] 
  
  for c in list1:
    if len(list2) <= 2:
      list2.append(c)
    else:
      list3.append(list2)
      list2 = []
      list2.append(c)
  list3.append(list2)
  list3[1][1] = 'BINGO'
  return list3
b = list()

r = '   _________________________'
def printer(d):
  print("\033[1;33m   David's Nan's Bingo Card Generator.")
  print()
  print()
  for i in d:
    for j in i:
      if i.index(j) == 2:
        print(f'\033[1;33m{j:^10}', end='')
      else:
        print(f'\033[1;33m{j:^10}|', end='')
      
    print()
    if d.index(i) != 2:
      print(f'{r}')
    print()
     
printer(b) 