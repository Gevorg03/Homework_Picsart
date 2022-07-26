"""Subtract two big numbers with list sliceing 3 digits"""

def number_setting(num1, num2):
    mark = None
    if int(num1) < int(num2):
        mark = 'minus'
    max_num = str(max(int(num1), int(num2)))
    min_num = str(min(int(num1), int(num2)))
    num1 = max_num
    num2 = min_num

    i1 = len(num1)
    i2 = len(num2)

    count_0 = '0' * abs(i1 - i2)
    if i1 < i2:
        num1 = f'{count_0}{num1}'
    elif i1 > i2:
        num2 = f'{count_0}{num2}'

    length = len(num1)
    lst1 = []
    lst2 = []

    while length > 0:
        if length > 3:
            lst1.append(num1[length - 3:length])
            lst2.append(num2[length - 3:length])
        else:
            lst1.append(num1[0:length])
            lst2.append(num2[0:length])
        length -= 3

    lst1.reverse()
    lst2.reverse()
    return lst1, lst2, mark

def sum_list_num(lst1: list, lst2: list, mark):
    lst = []

    if len(lst1[0]) < 3:
        lst1[0] = f'{"0" * (3 - len(lst1[0]))}{lst1[0]}'
    if len(lst2[0]) < 3:
        lst2[0] = f'{"0" * (3 - len(lst2[0]))}{lst2[0]}'

    for i in range(len(lst1) - 1, -1, -1):
        str_sum = ''
        for j in range(2, -1, -1):
            try:
                less_digit = int(lst1[i][j]) - int(lst2[i][j]) - reminder
                reminder = 0
            except:
                less_digit = int(lst1[i][j]) - int(lst2[i][j])
                reminder = 0

            if less_digit < 0:
                less_digit += 10
                reminder = 1

            str_sum = str(less_digit) + str_sum

        lst.append(str_sum)

    if mark == 'minus':
        lst.append('-')

    lst.reverse()
    return lst

num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
lst1, lst2, mark = number_setting(num1, num2)
print(sum_list_num(lst1, lst2, mark))
