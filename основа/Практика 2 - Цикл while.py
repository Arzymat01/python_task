#1
spisok=['Sergei', 'Valeriy', 'Elena', 'Marat', 'Stepan', 'Uson']
delete_name=""
while delete_name !="Стоп":
    delete_name=input("Введите имя для удаления:")
    if delete_name in spisok:
        spisok.remove(delete_name)
print(spisok)

#2
listNum = [23,45,4,5,12,4,5, 7, 15, 21, 78, 41]
i = 0
while (i < len(listNum)):
    if listNum[i] % 3 == 0:
        print(listNum[i], end=" ")

    i += 1
print("*"*25)

#3
word=['Hello', 'There', 'World', 'Bishkek', 'Tokyo', 'Almaty']
i=0
while i<len(word):
    s=word[i]
    if "o" in s:
        word.remove(s)
    i+=1
print(word)
