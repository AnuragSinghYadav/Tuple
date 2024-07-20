input_tuple = (1,2,3,4,5,6)
list = []

#added reversed values in a list
for x in reversed(input_tuple):
    list.append(x)


output_tuple = tuple(list)
print(output_tuple)