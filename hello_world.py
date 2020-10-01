# 1. TASK: print "Hello World"
print("Hello World")
# 2. print "Hello Noelle!" with the name in a variable
name = "Julia"
print("Hello", name)	# with a comma
print("Hello " + name)	# with a +
# 3. print "Hello 42!" with the number in a variable
number = 27
print("Hello", number)	# with a comma
#print("Hello " + number)	# with a +	-- this one should give us an error!
# 4. print "I love to eat sushi and pizza." with the foods in variables
fave_food1 = "sushi"
fave_food2 = "pizza"
print("I love to eat {} and {}.".format(fave_food1, fave_food2)) # with .format()
print(f"I love to eat {fave_food1} and {fave_food2}.") # with an f string

#NINJA BONUS

print("Hello " + str(number))

food_one = "asparagus"
food_two = "ice cream"

print("I love to eat {} and {}.".format(food_one, food_two))

print(f"I love to eat {food_one} and {food_two}.")

my_string = "   No White Space   "
print(my_string.strip())

my_string = "Lower Case"
print(my_string.lower())

my_string1 = "ABC"
my_string2 = "DEF"

print(my_string1.startswith("A"))

print(my_string2.startswith("A"))
