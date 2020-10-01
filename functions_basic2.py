# Countdown
def countdown(num):
    countdown_list = []
    for i in range(num, -1, -1):
        countdown_list.append(i)
    return countdown_list

x = countdown(5)
print(x)

# Print and Return
def print_and_return(a,b):
    print(a)
    return b

x = print_and_return(1,2)
print(x)

# First Plus Length
def first_plus_length(some_list):
    return (some_list[0] + len(some_list))

x = first_plus_length([1,2,3,4,5])
print(x)

# Values Greater than Second

def values_greater_than_second(some_list):
    if len(some_list) < 2:
        return False
    new_list = []
    for i in range(0, len(some_list)):
        if i > some_list[1]:
            new_list.append(i)
    print(len(new_list))
    return new_list

x = values_greater_than_second([5,2,3,2,1,4])
y = values_greater_than_second([3])
print(x)
print(y)

# This Length, That Value

def length_and_value(size,value):
    new_list = []
    for i in range(0, size):
        new_list.append(value)
    return new_list

x = length_and_value(4,7)
y = length_and_value(6,2)
print(x)
print(y)


    
