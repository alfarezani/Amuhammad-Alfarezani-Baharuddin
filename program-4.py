print('============= NOT =============')
a = True
c = not a
print('a adalah', a)
print('------ c = not a ------NOT')
print('c adalah', c)

print('============= OR =============')
a = True
b = True
c = a or b
print(a, 'OR', b, 'menjadi', c)

a = True
b = False
c = a or b
print(a, 'OR', b, 'menjadi', c)

a = False
b = True
c = a or b
print(a, 'OR', b, 'menjadi', c)

a = False
b = False
c = a or b
print(a, 'OR', b, 'menjadi', c)

print('============= AND =============')
a = True
b = True
c = a and b
print(a, 'AND', b, 'menjadi', c)

a = True
b = False
c = a and b
print(a, 'AND', b, 'menjadi', c)

a = False
b = True
c = a and b
print(a, 'AND', b, 'menjadi', c)

a = False
b = False
c = a and b
print(a, 'AND', b, 'menjadi', c)

print('============= XOR =============')
a = True
b = True
c = a ^ b
print(a, '^', b, 'menjadi', c)

a = True
b = False
c = a ^ b
print(a, '^', b, 'menjadi', c)

a = False
b = True
c = a ^ b
print(a, '^', b, 'menjadi', c)

a = False
b = False
c = a ^ b
print(a, '^', b, 'menjadi', c)
