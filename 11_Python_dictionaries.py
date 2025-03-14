# ==========Python Dictionaries===============
# It represent in {} where we define the keys and values
# We can define any data types

D = { 'name': 'max', 'age': 15, 'year': 2004}
print(D)

print(D['name'])
print(D['age'])

E = {'name': 'Tom', 15:15, 15.1:15, True:True, (2,3):5}
print(E)

print(E[True])
print(E[15])
print(len(E))

print(D.get('name'))

print(D)
D['surname']= 'Tesar'
print(D)

print(E)
E.clear()
print(E)

del E
print(E)

D['name'] = 'tom'
print(D)

D.update({'name':'raj'})
print(D)