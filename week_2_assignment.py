# creating a list
my_list = []
# append value 10,20,30,40,50
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(my_list)
# insert value on index 1, value must be 15
my_list.insert(1, 15)
print(my_list)
# extend my_list to 50,60,70
my_list_2 = [50,60,70]
my_list.extend(my_list_2)
print("Extended list",my_list)
# remove the last value in the list
my_list.remove(70)
print(my_list)
#Sort my_list in ascending order.
my_list.sort()
print(my_list)
#Find and print the index of the value 30 in my_list.
print(my_list[3])




