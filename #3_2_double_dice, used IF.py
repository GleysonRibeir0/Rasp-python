#3_2_double_dice, used IF
import random
for x in range(1, 11):
    throw_1=random.randint(1, 6)
throw_2=random.randint(1, 6)
total = throw_1 + throw_2
print(total)
if total == 7:
      print('seven throw !')
if total == 11:
      print('eleven throw!')
if throw_1 == throw_2:
     print('double thrown!')

print("main-branch")    