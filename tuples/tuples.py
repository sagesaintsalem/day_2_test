#define a tuple
car = ('Ford', 'Escort', 1300, 'Red')
car_2 = 'Ford', 'Escort', 1300, 'Green'
#define empty tuple
empty = ()
print(empty)
empty_2 = tuple()

#print them tuples
print(car)
print(type(car))
print(car_2)
print(type(car_2))

#access value by index
model = car[1]
print(model)

#can't change em tho
#car[1] = "Focus" This gives an error message

colour = car[-1]

print(f'Model: {model}, Colour: {colour}')

#count tuple elements
count = len(car)
print(count)

#Count occurrences of a thing in a tuple
nums = (1, 5, 3, 1, 6, 4, 7)
print(nums.count(1))

#One element? No problem!
lonely_tuple = ('billy',) #PAY ATTENTION TO THAT COMMA!
print(type(lonely_tuple))