#create empty lists
empty_1 = []
empty_2 = list()

#create a list with items
fruits = ["apple", "orange", "banana", "me"]
print(fruits)
#reassign value at index
fruits[2] = "kiwi"
print(fruits)
#find length
print(len(fruits))

#add a new fruit
fruits.append("plum")
print(fruits)

#remove last element
removed_fruit = fruits.pop(3)
print(f'I removed {removed_fruit}')
print(f'My fruits are now {str(fruits)}')