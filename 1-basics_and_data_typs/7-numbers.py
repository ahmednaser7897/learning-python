#-------------
#Numbers
#-------------

#Integer
print(type(1))#<class 'int'>
#Float
print(type(1.0))#<class 'float'>
#Complex
print(type(1+2j))#<class 'complex'>
complexNumber=1+2j
print(type(complexNumber))#<class 'complex'>
print("rael part is {}".format(complexNumber.real))#rael part is 1.0
print("imaginary part is {}".format(complexNumber.imag))#imaginary part is 2.0

#[1] you cant converst from int to float and complex
#[2] you cant convert from float to int and complex
#[3] you cant not convert from complex to int or float

number=1
print(type(number))#<class 'int'>
print(float(number))#1.0
print(complex(number))#1+0j
number=1.0

print(type(number))#<class 'float'>
print(int(number))#1

print(complex(number))#1+0j

number=1+2j
print(type(number))#<class 'complex'>
#print(float(number))#TypeError: float() argument must be a string or a real number, not 'complex'
#print(int(number))##TypeError: float() argument must be a string or a real number, not 'complex'
