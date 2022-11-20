# def decarito(fun):
#     def wrapper(*args,**kwargs):
#         print(f'Добро пожоловать Гость!\nПожалуйста представтесь:')
#         fun(*args,**kwargs)
#
#         print(f'Приятно с вами познокомиться!{args[0]} {args[0]}'
#               f'\nЖелаем удачи команде {args[3]}!')
#     return wrapper
# @decarito
# def showFullname(fName,sName,country,fcClub):
#     print(f'Меня зовут{fName}   {sName}')
# showFullname('Arzymat',  'Arkabaev',  'Kyrgyzstan',  'Shumkar')

def factoria(n):
    if n==1 or n==0:
        return n
    else:
        return n*factoria(n-1)
print(factoria(0))