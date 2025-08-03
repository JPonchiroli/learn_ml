dictionary = {'Course':'Python ML',
              'Producer':'Didatica Tech',
              'Price':'Free',
              'Grade': 10}

a = dictionary['Course']

print(a)

dictionary['Price'] = 'R$ 300,00'
print(dictionary)

dictionary['Prerequisite'] = 'Basic Python'
print(dictionary)

dictionary.keys()
dictionary.values()
dictionary.items()
dictionary.clear()