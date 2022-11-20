

#Task2
a=lambda n:n**2
print("квадарт число:",a(2))
#Task3
a=lambda a,b,c,d:(a+b+c+d)/4
print("Среднее значение:",a(2,3,4,5))
#Task4
price=int(input(f"Введите сумма:"))
discount=lambda priceIn,prosent:priceIn-(priceIn*prosent)
if 100<=price<2000:
    print(f"Ваше скидка с {price} состовляет 2% -{discount(price,0.02)}")
elif 2000<=price<5000:
    print(f"Ваше скидка с {price} состовляет 5% -{discount(price, 0.05)}")
elif 5000<=price<1000:
    print(f"Ваше скидка с {price} состовляет 10% -{discount(price, 0.1)}")
else:
    print(f"Ваше скидка с {price} состовляет 20% -{discount(price, 0.2)}")


