#--------------List---------------

a=[1,2,3,4]
print("a is ",a)
print("type of a is ",type(a))
print("id of a is ",id(a))
a[2]=5
print("changed a is",a)
print("type of a is ",type(a))
print("id of a is ",id(a))

#-------------tuple--------------

b=(1,2,3,4)
print("b is ",b)
print("type of b is ",type(b))
print("id of b is ",id(b))
b=(1,2,5,4)
print("changed b is",b)
print("type of b is ",type(b))
print("id of b is ",id(b))

#-------------------------conclusion----------------------------

print("Hence id of a remains same, so a is a mutable data type")
print("Hence id of b got changed, so b is a immutable data type")
