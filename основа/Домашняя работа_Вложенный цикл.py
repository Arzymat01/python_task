#1
num_0=input("Введите:").split()
for i in num_0:
    i=int(i)
    print("*" * i)
#2
nuM=int(input("Число лесенки:"))
for i in range(nuM,0,-1):
    for j in  range(1,i+1):
       print("*",end="")
    print()