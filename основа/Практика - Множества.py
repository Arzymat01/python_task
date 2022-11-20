#Task1
sampleSet = {"Yellow", "Orange", "Black"}
sampleList = ["Blue", "Green", "Red"]
sampleSet2=sampleSet.union(sampleList)
print(sampleSet2)
#Task2
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
print(set1.intersection(set2))
#Task3
set_1 = {10, 20, 30}
set_2 = {20, 40, 50}
set_1.difference_update(set_2)
print(set_1)
#Task4
set_3={45,69}
set_3.add(78)
print(set_3)

for i in range(3):
    num=int(input("Введите:"))
    set_3.add(num)
    print(set_3)
set_3.update(set_2)
print(set_3)
liSt=["python","java","c++"]
set_3.update(liSt)
print(set_3)
#Task5
set={"one","two","three","four","five"}
frozenset={1,2,3,4,5}
frozenset.update(set)
print(frozenset)
