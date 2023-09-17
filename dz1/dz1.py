numbers = [1, 10, -9, 6, 3, 40, 0, 99, 25, 36]
print(f'Исходный массив: {numbers}')


def sort_list_imperative(numbers):
    sort_array = []
    for elem in numbers:
        sort_array.append(elem)

    for i in range(len(sort_array)):
        for j in range(i + 1, len(sort_array)):
            if sort_array[i] > sort_array[j]:
                sort_array[i], sort_array[j] = sort_array[j], sort_array[i]
    return sort_array


print(f'Императивная сортировка:  {sort_list_imperative(numbers)}')


def sort_list_declarative(numbers):
    return sorted(numbers)


print(f'Декларативная сортировка: {sort_list_declarative(numbers)}')



