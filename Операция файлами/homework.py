#Task2
file=open("lorem.txt")
l=0
for i in file:
    l+=1
print("Стоки:",l)
#Task3
import random
t=open("text.text",encoding="utf-8")
dt=t.read()
lns=dt.split('\n')
ln=random.randrange(len(lns))
print(lns[ln])
file = open('text.text')
lines = 0
words = 0
symbols = 0
for line in file:
    lines += 1
print("Lines:", lines)
#Task4
list = input("Ведите работников:").split(",")
with open(" workers.txt","w") as worker:
    for i in list:
        worker.write(i)
        worker.write('\n')
##Task5
def l_words(file):
    with open(file,encoding='utf-8')as text:
        words=text.read().split()
        max_len=len(max(words,key=len))
        s_words=[word for word in words if len(word)==max_len]
        if len(s_words)==1:
            return s_words[0]
        return s_words
print(l_words('article.txt'))
