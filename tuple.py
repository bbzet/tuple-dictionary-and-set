myfamily = ("mother", "father", "sister", "brother", "sister")
#1 Use type() to check the type of the object
print(type(myfamily))



# 2 Access tuple item sister by using index numbers
print(myfamily[2])
# We can also assign value to variable
sister = myfamily[2]



#3 Whether we can add an item me by using the append() method
# We can not add an item in tuple as tuple is unchangeable,  so I convert it into list and add "me"
lst = list(myfamily)
lst.append("me")
#I return tuple to output as tuple
myfamily = tuple(lst)
print(myfamily)


#4 Check whether we can remove the item brother by using the pop() method
# As we can not remove again we change tuple into list
lst = list(myfamily)
lst.pop(-3)
myfamily = tuple(lst)
print(myfamily)
