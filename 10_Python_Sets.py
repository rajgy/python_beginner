#=======Python Sets======

# define the sets in the {}
#Not define the duplicate value in set

A = {1,2,5,4,7,9,2}
print(A)

print(len(A))

A.add(10)
print(A)

A.update([15,18,17,19])
print(A)

A.remove(18)
print(A)

A.discard(17)
print(A)

# A.remove(100)
# print(A)
#
# A.discard(100)
# print(A)

A.pop()
print(A)

name = { 'max', 'tom', 'Den'}
print(name)
name.clear()
print(name)

Z = set([1,2,3,4,5])
print(Z)

print(A)

B= { 10,11,12,13,14,16,18}
print(B)

print (A|B)  # Give the Union of the set values

print(A.union(B))

print(A&B) # Intersection of the elements in the Set A and Set B

print(A.intersection(B))

print(A-B)
print(B-A)

print(A.difference(B))
print(B.difference(A))

print( A ^ B)
print(B^A)

print(A.symmetric_difference(B))