
def SortArray(array):  #сортировка
    for i in range(1, len(array)):
        x = array[i]
        idx = i
        while idx > 0 and array[idx - 1] > x:
            array[idx] = array[idx - 1]
            idx -= 1
        array[idx] = x
    return array


def binary_search(array, element, left, right): #бинарный поиск
    if left > right:
        return [right,right + 1]  # терминальное условие когда нет числа в последовательности

    middle = (right + left) // 2
    if array[middle] == element:
        return [left, middle]  # терминальное условие если число в последовательности есть
    elif element < array[middle]:  
        # рекурсируем
        return binary_search(array, element, left, middle - 1)
    else:  # рекурсируем
        return binary_search(array, element, middle + 1, right)

correct_input = 1
borders = []

while correct_input:  #проверка на корректный ввод данных
    if correct_input == 1:
        input_array = input("Введите последывавательность целых чисел: ")
        input_array = input_array.split()

        try:
            input_array = list(map(int, input_array))
        except ValueError:
            print("Вы ввели некорректные данные (в последовательности "
                  "присутсвует спецсимовлы/буквы/не целые числа и.т.п\n"
                  "попробуйте снова.\n ")
        else:
            if input_array.__len__() > 1:
                correct_input = 2
            else:
                print("1 число это не последовательность попробуйте ещё раз\n")

    max_arr = max(input_array)
    min_arr = min(input_array)

    if correct_input == 2:

        try:
            print("Введите произвольное целое числов диапозоне",
                  min_arr , "-", max_arr , ":")
            input_number = int(input())
        except ValueError:
            print("Вы ввели не целое число попробуйте снова\n ")
        else:
            if input_number > max_arr or input_number < min_arr:
                print("выход за пределы диапозона")
            else:
                correct_input = 0

output_list = SortArray(input_array)
borders = binary_search(output_list, input_number, 0, output_list.__len__() - 1)

print("Отсортированый список", output_list)
print("числа между которыми находистя число, заданое пользователем",
      output_list[borders[0]], output_list[borders[1]])
print("позиция искомого числа", borders[0]) #borders[0]+1 если нужна пиозиция без 0 элемента

