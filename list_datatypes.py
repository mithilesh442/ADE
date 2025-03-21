# Defining Lists
my_list = [1, 1, 2, 3, 12.34]
print(my_list)

#Insert values into the list
my_list.append(100)
print(my_list)

#Delete Elements
my_list.pop()  # pop = Last In First Out (LIFO)
print(my_list)

#Delete a specific element from the list
my_list.remove(12.34)
print(my_list)

#Count a specific element in the list
my_count = my_list.count(1)
print(my_count)

#Copy the existing list
my_list1 = my_list.copy()
print(my_list1)

#Extend will combine together 2 lists
my_cars = ['BMW', 'AUDI', 'THAR']
my_list.extend(my_cars)
print(my_list)

#Index will tell the element present in which index position
my_index = my_list.index(3)
print(my_index)

#Insert a value in a specific index(index position, value)
my_list.insert(4, 4)
print(my_list)

#Reverse will reverse the existing list
my_list.reverse()
print(my_list)

#Clear will delete all the elements in the list
my_list.clear()
print(my_list)

#It will print the index position of 4
my_nums = [10, 30, 20, 40, 100, 50]
print(my_nums[4])

#It will take start as 0 and stops as 4-1=3 and step = default or 1
print (my_nums[0:4])

#It will take start as 0 if we dont mention any value
print(my_nums[:4])

#It will take start as 0 and stop as -1 and step as 2
print(my_nums[::2])

#It will take -1 as last position
print(my_nums[-1])

#It will take -2 from last postion
print(my_nums[-2])

#It will give index position of 40
print(my_nums.index(40))

#Sort will arrange the values in ascending order
my_nums.sort()
print(my_nums)
