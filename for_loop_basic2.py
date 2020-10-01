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