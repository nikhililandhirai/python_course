lst=['apple','guava','mango','banana','kiwi']

print("length of list:",len(lst))
print("first Element:",lst[0])
print("last Element:",lst[-1])

lst.append('papaya')
print("updated list :",lst)

lst.remove('guava')
print("updated list:",lst)

lst.sort()
print("sorted list:",lst)

lst.pop()
print("updated list:",lst)

lst.reverse()
print("reversed list:",lst)

lst=lst[0:4]
print("sliced list :",lst)

lst.clear()
print("updated list:",lst)