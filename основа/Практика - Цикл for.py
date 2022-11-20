#2
word_0=['apple','banana', 'orange', 'pineapple', 'cherry']
for i in word_0:
    print(i.upper())
#3
sum=0
for i in range(5,58):
    if i==34 or i==46 or i==52:
        continue
    else:
        sum+=1
print(sum)

#4
word=input("Ввведите любое слово:")
num=int(input("Ввведите любое число:"))
for i in word:
    print(i*num)



