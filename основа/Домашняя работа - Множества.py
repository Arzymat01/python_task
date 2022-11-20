#Task
set1 = {10, 20, 30, 40, 50}
set1.difference_update({10, 20, 30})
print(set1)
#Task2
set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}
if set1.isdisjoint(set2):
    print("")
else:
    print("Два множества имеют общий элемент и это: ")
    print(set1.intersection(set2))

#Task3
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
print(set1.intersection(set2))
print("*"*20)
#Task4

seT_2={15,87,67,78,36}
seT_2.difference_update({67})
print(seT_2)
seT_2.update({56,39})
print(seT_2)
a=int(input("Введите:"))
seT_2.add(a)
print(seT_2)
