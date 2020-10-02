my_array = [4,3,2,1,2]

def selection_sort(some_list):
    for j in range(0, len(some_list) - 1):
        min = some_list[j]
        for i in range(j, len(some_list)):
            if some_list[i] < min:
                min = some_list[i]
                some_list[i], some_list[j] = some_list[j], some_list[i]
    return some_list

print(selection_sort(my_array))

