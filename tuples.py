# Tuples used to store multiple items in a variable ,it using (  ) brackets 
# tuples have : ordered, immutable, duplicate allowed, any datatype, mix of different data types.
colours = ("red","yellow","green")

#creating a tuple with 1 item
#fruit = ("apple",)
#print(type(fruit))

#another way to create tuple
fruit = tuple("apple")

#accessing items in tuple
print(colours[1]) #positive indexing

#negative indexing
print(colours[-1])

#range indexing
print(colours[1:3]) # +1 add to have last index
#in negative way range
print(colours[-2:]) 

# check item exists in tuple
if "green"in colours:
    print("Green is part of tuple")

#concanicate 2 tuples
# more_colours = ("blue", "Black")
# colours = colours + more_colours
# print(colours) 

#unpacking a tuple: taking a value from variable  to multiple variables
colours1 , colours2 , colours3 = colours
print(colours1, colours2, colours3)
