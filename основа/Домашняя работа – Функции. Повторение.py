#Task1
def countDuplicate(list):
    dict={}
    for i in list:
        dict[i]=list.count(i)
    return dict
print(countDuplicate([12,3,54,5,12,3,2,7,6,3,2]))
#Task2
def cons(str_:str):
    v="aeoiyu"
    c="qwrtpsdfghjklzxcvbnm"
    list1=[]
    list2=[]
    for i in list(str_):
        if i.lower() in v:
            list1.append(i)
        elif i.lower() in c:
            list2.append(i)
    return [list1,list2]

print(cons("Heloo world"))
#Task3
def findMaxMean(myList:str):
    myList = [
        [3, 4, 5, 12],
        [7, 4, 6, 2],
        [3, 2],
        [5, 6, 7, 10, 3]
    ]
    if sum(myList[0])/len(myList[0])>sum(myList[1])/len(myList[1])>sum(myList[2])/len(myList[2])<sum(myList[3])/len(myList[3]):
        return myList[3]
print(findMaxMean(5))





