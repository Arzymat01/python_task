#Task1
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
d = dict1.copy()
for i, j in dict2.items():
    d[i] = d.get(j,0) + j
print(d)

#Task2
sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}
print(sampleDict['class']['student']['marks']['history'])

#Task3
votersDict = {
    "Denis":32,
    "Sergey":21,
    "Elena":18,
    "Timur":17,
    "Oleg":27
    }
for k,v in votersDict.items():
    if v>18:
        print(f'Ваш зовут {k}, вам {v} года и вы можете голосовать')
    else:
        print(f'Ваш зовут {k}, вам {v} лет и вы НЕ можете участвовать в голосовании, потому что вы слишком молоды! ')



#Task4
tudentList={
    "Oleg":"Mockow",
    "Stepan":"Novesibirsk",
    "Olga":"Ekaterenburg",
    "Murat":"Bishkek",
    "David":"New York"
}
del tudentList[input("Введите :")]
print(tudentList)