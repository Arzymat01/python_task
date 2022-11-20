#Task1
def rev(n1,n2=0):
    if n1 // 10 == 0:
        return (n2 * 10) + n1
    else:
        return rev(n1 // 10, (10 * n2) + (n1 % 10))
print(rev(12345))
#Task3
def numbers(a,b,c):
    x = 0
    if a > 0:
        x += 1
    if b > 0:
        x += 1
    if c> 0:
        x += 1
    print("Количество положительных чисел: ", x)
    y = 0
    if a < 0:
        y += 1
    if b < 0:
        y += 1
    if c < 0:
        y += 1
    print("Количество отрицательных чисел: ", y)
numbers(-1,2,-2)
#Task5
defFing=lambda n1,n2:n1/n2
print(defFing(120,2))

#Task6
def numvers():
    n=[]
    n1=[12,33,45 ,4,54,1,32,11 ,67,88]
    for i in n1:
        if i%2==0:
            n.append("Четный")
        else:
            n.append("Не четный")
    print(n)
numvers()
#Task7
lst=["HELLO","HOW ARE YOU", "I AM FINE", "THANK YOU"]
llist=list(map(lambda x:x.lower(),lst))
print(llist)
