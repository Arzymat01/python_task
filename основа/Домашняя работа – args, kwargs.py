#Task1
def info_kwargs(**kwargs):
    for key,value in kwargs.items():
        print (key,value)
info_kwargs(first_name="John",last_name="Doe",age=33)
#Task2
def format_namelist(x):
    c=[]
    for i in range(0,len(x)):
        y=x[i].get('name')
        c.append(y)
    if len(c)>1:
        c.insert(len(c)-1,'и')
    if len(c)>3:
        for i in range(0,len(c)-3):
            c[i]=c[i].ljust(len(c[i])+1,',')
    print(*c)
format_namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
format_namelist([ {'name': 'Bart'}, {'name': 'Lisa'} ])






