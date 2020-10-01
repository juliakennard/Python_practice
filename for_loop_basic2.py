# Biggie Size

def biggie_size(some_list):
    biggie_list = []
    for i in range(0, len(some_list)):
        if some_list[i] <= 0:
            biggie_list.append(some_list[i])
        else:
            biggie_list.append("big")
    return biggie_list

x = biggie_size([-1,3,5,-5])
print(x)

# Count Positives

def count_positives(some_list):
    new_list = some_list
    positive_count = 0
    for i in range(0, len(some_list)):
        if some_list[i] > 0:
            positive_count += 1
    new_list[len(some_list)-1] = positive_count
    return new_list

x = count_positives([-1,1,1,1])
y = count_positives([1,6,-4,-2,-7,-2])
print(x)
print(y)

# Sum Total

def sum_total(some_list):
    sum_total = 0
    for i in range(0, len(some_list)):
        sum_total = sum_total + some_list[i]
    return sum_total

x = sum_total([1,2,3,4])
y = sum_total([6,3,-2])
print(x)
print(y)

# Average

def average(some_list):
    sum_total = 0
    for i in range(0, len(some_list)):
        sum_total = sum_total + some_list[i]
    average = sum_total / len(some_list)
    return average

x = average([1,2,3,4])
print(x)

# Length

def length(some_list):
    return len(some_list)

x = length([37,2,1,-9])
y = length([])
print(x)
print(y)

# Minimum

def minimum(some_list):
    if len(some_list) < 1:
        return False
    minimum = some_list[0]
    for i in range(0, len(some_list)):
        if some_list[i] < minimum:
            minimum = some_list[i]
    return minimum

x = minimum([37,2,1,-9])
y = minimum([])
print(x)
print(y)

# Maximum

def maximum(some_list):
    if len(some_list) < 1:
        return False
    maximum = some_list[0]
    for i in range(0, len(some_list)):
        if some_list[i] > maximum:
            maximum = some_list[i]
    return maximum

x = maximum([37,2,1,-9])
y = maximum([])
print(x)
print(y)

# Ultimate Analysis

def ultimate_analysis(some_list):
    sum_total = some_list[0]
    minimum = some_list[0]
    maximum = some_list[0]

    for i in range(1, len(some_list)):
        sum_total = sum_total + some_list[i]
    
    for i in range(0, len(some_list)):
        if some_list[i] < minimum:
            minimum = some_list[i]
    
    for i in range(0, len(some_list)):
        if some_list[i] > maximum:
            maximum = some_list[i]

    average = sum_total / len(some_list)
    length = len(some_list)

    return {"sumTotal": sum_total, "average": average, "minimum": minimum, "maximum": maximum, "length": length}

x = ultimate_analysis([37,2,1,-9])
print(x)

# Reverse List

def reverse_list(some_list):
    for i in range(0, int(len(some_list)/2)):
        some_list[i], some_list[len(some_list)-(i+1)] = some_list[len(some_list)-(i+1)], some_list[i]
    return some_list

x = reverse_list([37,2,1,-9])
print(x)





