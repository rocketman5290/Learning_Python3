input_str1 = input('Hello, Please enter your first name in the prompt:')
print('Users first name:', input_str1)
input_str2 = input('please enter your last name followed by enter:')
print('Users last name:', input_str2)
fss = 'Thank you and hello {} {}, welcome to your first cli app written in python.'
fss = fss.format(input_str1, input_str2)
print(fss)
