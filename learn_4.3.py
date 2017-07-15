#range() list()

for value in range(2,3):
    print(value)

num1 = list(range(3,11))
print(num1)

num2 = list(range(2,11,2))
print(num2)

squares = []
for num3 in range(1,11):
    square = num3**2
    squares.append(square)
    print(squares)
print(squares)

print('min: '+str(min(squares)))
print('max: '+str(max(squares)))
print('sun: '+str(sum(squares)))

#4.3.4
print('列表解析')
new_list = [num4**3 for num4 in range(1,11)]
print(new_list)
