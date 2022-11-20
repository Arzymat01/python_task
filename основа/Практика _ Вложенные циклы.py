#1
for a in range(1,10):
    for b in range(1,10):
        print(a*b, end='\t')
    print()
#2
n = int(input("Введите :"))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print("*", end='')
    print()

#3
row = int(input("Row: "))
col = int(input("Col: "))

numListNested = []

for i in range(row):
    tempList = []
    for j in range(col):
        num = int(input(f'Enter number {j+1} for {i+1} row: '))
        tempList.append(num)
    numListNested.append(tempList)

print('='*25)
print(numListNested)
for row in numListNested:
    for num in row:
        print(num, end=" ")
    print()