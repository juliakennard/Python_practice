# ranInt Function
import random
def randInt(min = 0, max = 100):
    if min > max:
        return("Error: Min has to be less than max")
    if max == 0:
        return("Error: Max must be more than zero")
    num = random.random() * (max - min) + min
    return num

print(randInt())
print(randInt(max = 50))
print(randInt(min = 50))
print(randInt(min = 50, max = 500))
