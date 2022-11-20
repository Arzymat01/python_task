1#
num= [123,4,45,6,7]
print(max(num))
print("-"*45)
#2
numList = [21,43,54,6,76,8,34]
print(sum(numList))
print(sum(numList)/len(numList))
print("-"*45)
#3
alphabetList = ["a", "s", "d", "t"]
alphabetList.sort()
print(alphabetList)
alphabetList.reverse()
print(alphabetList)
print("-"*45)
#4
num.append([45,61])
print(num)
clear=numList[-2]
numList.remove(clear)
print(numList)
numList.insert(0,[65])
print(numList)
print("-"*45)
#5
import copy
someList = [12,454,65,76,1,23]
someList_2=copy.deepcopy((someList))
someList_2.append(65)
print(someList)
print(someList_2)

someList_3=someList
someList_3.append(89)
print(someList_3)
