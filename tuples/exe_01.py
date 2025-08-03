# unchanged lists
_list  = [2, 3, 5]
_tuple = (2, 3, 5)

_list[0]  = 20
# _tuple[0] = 20 # Error

del _list[0]
# del _tuple[0] # Error

_list.append(10)
# tup_tuplele.append(10) # Error

new_tuple = tuple(_list)
print(_list)
print(type(new_tuple))