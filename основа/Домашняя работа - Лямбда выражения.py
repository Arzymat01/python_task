#Task1
reverse=lambda n:n[::-1]
print(reverse("Python"))
#Task3
printEverSecLetter=lambda word:word[::2]
print(printEverSecLetter("Python"))
#Task4
avg=lambda somelist:sum(somelist)/len(somelist)
print(avg([2,5,8,9]))
#Task5
num1=int(input("Введите 1-ое число:"))
num2=int(input("Введите 2-ое число:"))
number=lambda num1,num2:num1**num2
print(f'Число{num1},в степени {num2}-это:',number(num1,num2))

#Task6
n1 = int(input("Введите 1-ое число:"))
n2 = int(input("Введите 2-ое число:"))
t=lambda n1,n2:'делится бз остатки' if n1%n2==0 else 'неделится бз остатки'
print(t(n1,n2))









