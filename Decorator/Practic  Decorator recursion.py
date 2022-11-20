# #Task1
# def  decorotor_find_sum_text(somolist):
#     def wrapper():
#
#         print('-------------')
#         print("Сумма всех значений в списке:")
#         print('-------------')
#         somolist()
#         print('-------------')
#     return wrapper
#
# @decorotor_find_sum_text
# def main():
#   print(sum([32, 54, 546, 65]))
# show_list=[32,54,546,65]
# print(show_list[0])
# print(show_list[1])
# print(show_list[2])
# print(show_list[3])
# main()
import xlsxwriter
def decorator_findSum_ex(func):
    workbook = xlsxwriter.Workbook('decor_result.xlsx')
    worksheet = workbook.add_worksheet('Sheet1')
    def wrapper(params):
        row = 0
        col = 0
        dict_ = {}
        dict_['Количество элементов'] = len(params)
        dict_['Среднее значение'] = sum(params)/len(params)
        dict_['Сумма'] = sum(params)
        for key,value in dict_.items():
            worksheet.write(row, col, key)
            worksheet.write(row+1, col, value)
            col += 1
        workbook.close()
    return wrapper
@decorator_findSum_ex
def return_list(list_):
    return list_

def main():
    return_list([32, 54, 546, 65])

if __name__ == '__main__':
    main()
