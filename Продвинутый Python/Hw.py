import collections
def task1(numList):
      counnterNumlist=collections.Counter(numList)
      listnum=[k for k,v in counnterNumlist.items() if v>=2 ]
      print(listnum)

def task2(numList):
      commomNums=collections.Counter(numList).most_common()
      print(commomNums)
def task3():
      counterNumlist=collections.Counter(numList)
      numlist=list(counterNumlist)
      newtuple=tuple(counterNumlist)
      dictcounter=dict(counterNumlist)
      print(numlist)
      print(newtuple)
      print(dictcounter)

def task4(numList):
      def chekNum(n):
            return n % 5==0
      newList=list(filter(chekNum,numList))
      print(newList)



def task5(text):
      worlist=text.split('')
      worlist=list(filter(bool,worlist))

      def chekword(word):
            return  word.islower()
      worlistRegistr=list(filter(chekword,worlist))
      print(f'Срисок в нижнем регистре{worlistRegistr}')




if __name__ == '__main__':
      numList = [2, 25, 43, 2, 4, 55, 2, 43, 54, 3, 21, 2, 50, 54, 2, 4, 10, 12, 13, 41, 43]
      ext = """ Hi! My name is Adam, I am from Boston, I would like to visit San-Fransico 
      and Washington, because I have a lot of friends from these cities. They works in 
      companies such as IBM, INTELL, APPLE, GOOGLE, ORACLE"""
      # task1(numList)
      # task2(numList)
      # task3()
      task4(numList)
      task5(text)





