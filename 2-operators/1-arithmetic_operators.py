#-------------
#Arithmetic Operators
#-------------
#[1] + addition
#[2] - subtraction
#[3] * multiplication
#[4] / division
#[5] // floor division
#[6] % modulus
#[7] ** exponentiation
#[8] = assignment
#[9] += addition assignment
#[10] -= subtraction assignment
#[11] *= multiplication assignment
#[12] /= division assignment
#[13] //= floor division assignment
#[14] %= modulus assignment
#[15] **= exponentiation assignment

a = 10
b = 3

print(a + b) #13
print(a - b) #7
print(a * b) #30
print(a / b) #3.3333333333333335
print(a // b) #3
print(a % b) #1
print(a ** b) #1000

a = 10
a += 5
print(a) #15

a = 10
a -= 5
print(a) #5

a = 10
a *= 5
print(a) #50

a = 10
a /= 5
print(a) #2.0

a = 10
a //= 5
print(a) #2

a = 10
a %= 5
print(a) #0

a = 10
a **= 5
print(a) #100000

a = 10
a = a + 5
print(a) #15