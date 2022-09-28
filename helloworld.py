def convert(inches) :
    cent = inches * 2.54
    print(float(inches),
          'inches equal',
          cent,
          'centimeters.')
    return cent

convert(50)
a,b,c = 1,2,3
convert(a)
convert(b)
convert(c)

def quad(a, b, c):
    determ = (b * b - 4 * a * c) ** 0.5
    x = (-b + determ ) / (2 * a)
    return x

def quad_test(phi):
    return ((phi * phi) - 1) == phi

#execute above quadratic function to get golden ratio
print(quad(1, -1, -1))
#execute test function which tests accuracy of GRatio
print(quad_test(quad(1, -1, -1)))

print(quad(3,-3,-3))
print(quad_test(quad(3,-3,-3)))
