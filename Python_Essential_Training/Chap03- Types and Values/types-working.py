# x = (1, 2, 3, 4, 5)
# print('x is {}'.format(x))
# print(type(x))

x = (1, "two", 3, [4, "four"], 5)
y = [1, "two", 3, [4, "four"], 5]
print('x is {}'.format(x))
print(type(x))
print(type(x[1]))
print("id: {}".format(id(x)))
print(id(y))

#Verify if they are exactly the same object
# if x[0] is y[0]:
#     print("yep")
# else: print("Nope")

# if x is y:
#     print("yep")
# else: print("Nope")

if isinstance(y, tuple):
    print("yep")
elif isinstance(y, list):
    print("list")
else: print("nope")