# =======Slice and Dictionaries==========

# how to use negative number

a = [0,1,2,3,4,5,6,7,8,9]
b= [0,1,2,3,4,5,6,7,8,9]
c='0123456789'

x =slice(0,5)
print(a[x])

print(a[0:5])

print(b[4:])
print(b[:6])

print(c[:5])

print(c[:])

print(a)
print(a[0:9:2])

print(b[0:9:4])


print(c[-1])
print(a)
print(a[::-1])
print(a[1::-1])
print(a[:-3:-1])