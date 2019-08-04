import time


def abundant(abu_number):
    limit = int(abu_number / 2) + 1
    summ = 0
    for i in range(1, limit):
        if abu_number % i == 0:
            summ += i
    if summ > abu_number:
        return True


def binary_search(item, lst):
    mid = len(lst) // 2
    low = 0
    high = len(lst) - 1
    while lst[mid] != item and low <= high:
        if item > lst[mid]:
            low = mid + 1
        else:
            high = mid - 1
        mid = (low + high) // 2

    if low > high:
        return False
    else:
        return True


start_time = time.time()

all_numbers_list = [x for x in range(1, 28124)]
print(f'all done')

list_of_abu_numbers = []
for number in range(1, 28123):
    if abundant(number):
        list_of_abu_numbers.append(number)
print(f'abu done {list_of_abu_numbers}')

sum_of_abu_numbers = [0, 0, 0]
for i in list_of_abu_numbers:
    ind = list_of_abu_numbers.index(i)
    for j in list_of_abu_numbers[ind:]:
        s = i + j
        sum_of_abu_numbers.append(s)
sum_of_abu_numbers.sort()
print(f'various sums abu {sum_of_abu_numbers[-100:]}')

result_lst = []
for i in all_numbers_list:
    if not binary_search(i, sum_of_abu_numbers):
        result_lst.append(i)


print(f'result list: {result_lst}')
print(sum(result_lst))
print('--- %s seconds ---' % (time.time() - start_time))

