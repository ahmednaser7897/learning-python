#-------------
#Assignment Operators
#-------------

#[1] = assignment
#[2] += addition assignment
#[3] -= subtraction assignment
#[4] *= multiplication assignment
#[5] /= division assignment
#[6] //= floor division assignment
#[7] %= modulus assignment
#[8] **= exponentiation assignment
#[9] &= bit and assignment
#[10] |= bit or assignment
#[11] ^= bit xor assignment
#[12] >>= right shift assignment
#[13] <<= left shift assignment

# Var one [Operator]= Var two
x = 10
y = 20
z=x+y
print(z) #30
x += y
print(x) #30
x -= y
print(x) #0
x *= y
print(x) #0
x /= y
print(x) #0.0
x //= y
print(x) #0
x %= y
print(x) #0
x **= y
print(x) #0
x &= y
print(x) #0
x |= y
print(x) #20
x ^= y
print(x) #20
x >>= y
print(x) #0
x <<= y
print(x) #0

