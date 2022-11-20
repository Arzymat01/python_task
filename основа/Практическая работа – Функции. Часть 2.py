#Task1
def is_person_teenager(age) :
    if age>=12 and age<17:
        return True
    else:
        return False
print(is_person_teenager(13))
#Task2
def generate_fizz_buzz_list(n=int(input("Введите:"))):
    list1=[ ]
    for i in range(1,n+1):
        if i%3==0 and i%5==0:
            list1.append("FizzBuzz")
        elif i%3==0:
            list1.append("Fizz")
        elif i%5==0:
            list1.append(" Buzz")
        else :
            list1.append(i)
    return list1
print(generate_fizz_buzz_list())
#Task3
def myfunc(*args):
    for x in args:
        if x > 0:
            return True
        else:
            return False
print(myfunc(1,5,6))
print(myfunc(-2,-3))

#Task4
def numberFunc(*args):
    count=0
    for i in args:
        count+=i
    return count
print(numberFunc(10,5,7,9,15))















