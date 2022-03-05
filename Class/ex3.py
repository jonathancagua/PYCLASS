my_list = []

print(id(my_list))
print(type(my_list))
print(len(my_list))

for element in my_list:
    print (element)

my_list.append(10)
print(id(my_list))
print(type(my_list))
print(len(my_list))

for element in my_list:
    print (element)