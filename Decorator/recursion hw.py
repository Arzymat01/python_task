#Task1
def reversNum(n1,n2=0):
    if n1//10==0:
        return (n2*10)+n1
    else:
        return reversNum(n1//10,(10*n2)+(n1%10))
#Task2
def list_sum_recursive(number):
    if len(number) == 0:
        return 0
    elif len(number) == 1:
        return number[0]
    else:
        n1 = len(number)-1
        return number[n1] + sum(number[0:n1])
number=[]
n=int(input("Сколько чисел?"))
for i in range(n):
    a=int(input("Введите:"))
    number.append(a)
#Task3
def flatten(*args):
    list1=[]
    for i in args:
        for j in i:
            if not isinstance(j,list):
                list1.append(j)
            else:
                r=flatten(j)
                list1.extend(r)
    return list1

if __name__=='__main__':
    print(flatten([1, [2, 3], [[2], 5], 6]))
    print(list_sum_recursive(number))
    print(reversNum(int(input("Введите число:"))))

