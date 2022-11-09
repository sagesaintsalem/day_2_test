# For the following list of numbers:

numbers = [1, 6, 2, 2, 7, 1, 6, 13, 99, 7]

# 1. Print out a list of the even integers:
even_nums = []
for i in numbers:
     if i % 2 == 0:
         even_nums.append(i)
 print(even_nums)


# 2. Print the difference between the largest and smallest value:
print(max(numbers) - min(numbers))

# 3. Print True if the list contains a 2 next to a 2 somewhere.
for x in range(len(numbers)-1):
    print(numbers[x])
    if numbers[x] == 2 and numbers[x+1] == 2:
        print(True)
        break

#Alternative solution from class
result = False
index = 0
for number in numbers:
     if (number == 2 and numbers[index-1] == 2):
          result = True
     index += 1
print(result)
          
#I stopped here because I am very tired - Rita

# 4. Print the sum of the numbers, 
#    BUT ignore any section of numbers starting with a 6 and extending to the next 7.
#    
#    So [11, 6, 4, 99, 7, 11] would have sum of 22
sum_tot = 0
stop_adding = False
for y in numbers:
     if y == 6:
          stop_adding = True
     elif stop_adding:
          if y == 7:
               stop_adding = False
     else:
          sum_tot += y
print(sum_tot)

    
               
               

# 5. HARD! Print the sum of the numbers. 
#    Except the number 13 is very unlucky, so it does not count.
#    And numbers that come immediately after a 13 also do not count.
#    HINT - You will need to track the index throughout the loop.
#
#    So [5, 13, 2] would have sum of 5. 

total = 0
index = 0
for number in numbers:
     if number == 13 or numbers[index-1] == 13:
          pass
     else:
          total += number
     index += 1
     
 print(total)




