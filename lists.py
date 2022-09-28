l10= [1,2,3,4,5,6,7,8,9,10]
for n in l10:
    print(n, end=" ")

if 1 in l10:
    print('1 is in list',end='\n')

n = 12
if n in l10:
    l10.remove(n)
    print('12 is in list')
else:
    print('12 is not in the list')

cels_list = [15, 20, 25, 30]

fahr_list = []
for c in cels_list:
    x = c * 1.8 + 32.0
    fahr_list.append(x)
print(fahr_list)

# a sorting application
a_list = []
while True:
    str1 = input('Enter a name: ')
    if str1 == '': # If string is empty,
        break
    a_list.append(str1)
a_list.sort()
print('Here is the alpha sorted list...')
for str1 in a_list:
    print(str1)
