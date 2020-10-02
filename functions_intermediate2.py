## Update Values in Dictionaries and Lists

x = [[5,2,3], [10,8,9]]
students = [
    {"first_name": "Michael", "last_name": "Jordan"},
    {"first_name": "John", "last_name": "Rosales"}
]

sports_directory = {
    "basketball": ["Kobe", "Jordan", "James", "Curry"],
    "soccer": ["Messi", "Ronaldo", "Rooney"]
}

z = [{"x": 10, "y": 20}]

# Change the value 10 in x to 15

x[1][0] = 15
print(x)

# Change the last_name of the first student from "Jordan" to "Bryant"

students[0]["last_name"] = "Bryant"
print(students)

# Change "Messi" to "Andres" 

sports_directory["soccer"][0] = "Andres"
print(sports_directory)

# Change the value 20 in z to 30

z[0]["y"] = 30
print(z)

## Iterate Through a List of Dictionaries

students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(some_dictionary):
    for entry in range(0, len(some_dictionary)):
        for key in some_dictionary[entry]:
            print(key + " - " + some_dictionary[entry][key])

iterateDictionary(students)


