# num1=int(input("Введите число1:"))
# num2=int(input("Введите число2:"))
#
# for i in range(num1, num2+1):
#     if i % 3 == 0 and i % 5 == 0:
#         print('FizzBuzz')
#     elif i % 5 == 0:
#         print('Buzz')
#     elif i % 3 == 0:                #
#         print('Fizz')
#     else:
#         print(i)
#
#
# number_0 = int(input("Введите число1:"))
# number_1 = int(input("Введите число2:"))
# for i in range(number_0, number_1 + 1):
#     print(f'Число {i}; его квадрат = {i ** 2}; его куб = {i ** 3}')

# numbers=int(input("Сколько количестово записей выполнить:"))
# name=input("Имя:")
# for name in range(numbers-1):
#
#     name = input("Имя:")
#
 # print(list(range(name)))

num=int(input("Введите :"))
for i in range(1, num+1):
     for j in range(i, i*num+1, i):
         print(j, end='\t')
     print()
