#1
tex_0="Привет!"
print(tex_0[::-1])
print("-"*30)
#2
tex_1="Я обучаюсь курсу Python Django"
print("Название курса:", tex_1[17:30])
print("-"*30)
#3
tex_2="$$$Python@@@"
tex_3="%%%Programming"
tex_4="City&&&"
tex_5="****Computer***"
print(tex_2.lstrip('$').rstrip('@'))
print(tex_3.lstrip("%"))
print(tex_4.rstrip("&"))
print(tex_5.lstrip("*").rstrip("*"))
print("-"*30)
#4
L_color="Белый"
l_number="9"
l_city="Бактен"
l_food="Плов"
print("Любимый цвет: {0}\nЛюбимое число: {1}\nЛюбимый город: {2}\nЛюбимая еда:{3}".format(L_color,l_number,l_city,l_food))
# F_format
print("-"*30)
print(f"Любимый цвет:{L_color}\nЛюбимое число:{l_number}" f"\nЛюбимый город:{l_city}\nлюбимая еда: {l_food}")
