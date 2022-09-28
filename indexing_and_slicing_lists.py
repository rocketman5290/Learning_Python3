from re import A


a_list = []
a_list.append('william')
a_list.append('everett')
a_list.append('george')


for name in a_list:
    print(name)

print(a_list[-1])
reversed_a_list = a_list[-1::-1]
print(reversed_a_list)
print(reversed_a_list[0][-1::-1])
print(len(reversed_a_list))
print(type(float((len(reversed_a_list)))))
slice_copy = a_list[:]
print(slice_copy)
