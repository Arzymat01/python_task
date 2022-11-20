#Task2
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
            row += 1

    workbook.close()
    return wrapper
@decorator_findSum_ex
def return_list(list_):
    return list_

def main():
    return_list([32, 54, 546, 65])

if __name__ == '__main__':
    main()