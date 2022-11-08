#Create empty dictionaries
my_1st_dict = {}
my_2nd_dict = dict()

#Here's a dictionary!
meals = {"breakfast":"porridge", "lunch":"sammich", "dinner":"pasta"}
print(meals)

#Get you a value from a key
print(meals['breakfast'])

#What keys are available?
print(meals.keys())

#What values are in there?
print(meals.values())

#Look at all these types!
hings = {1:'2', 'straight':False, 7.77:666}
print(hings.keys())
print(hings.values())

#Is it there at all?
print("breakfast" in meals)

#Let's add a thing!
meals["snacc"] = "chocolate"
print(meals)

#Let's remove a thing!
del(meals["snacc"])
print(meals)

#I convert thee to a list
print(list(meals)) #Notice how it only puts in the keys, not the values.


countries = {
    "Scotland":{"capital":"Edinburgh", "population":5000000},
    "Germany":{"capital":"Berlin", "population":60000000},
    "France":{"capital":"Paris", "population":60000000}
}

print(countries["Germany"]["population"])