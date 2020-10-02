## Only had time this week to work on one of these. Got _.filter to work!

class Underscore:
    # def map(self, iterable, callback):
        # your code here
    # def find(self, iterable, callback):
        # your code here

    def filter(self, iterable, callback):
        filtered_list = []
        for i in range(0, len(iterable)):
            if callback(iterable[i]):
                filtered_list.append(iterable[i])
        return filtered_list

    #def reject(self, iterable, callback):
        # your code
# you just created a library with 4 methods!
# let's create an instance of our class
_ = Underscore() # yes we are setting our instance to a variable that is an underscore
evens = _.filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
# should return [2, 4, 6] after you finish implementing the code above
print(evens)
