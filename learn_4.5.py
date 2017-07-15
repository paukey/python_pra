#2017年7月15日

#元组tuple()不能修改,但是可以给存储元组的变量赋值  list[]支持修改
dimensions=(200,40)
for dimension in dimensions:
    print('原始元组'+str(dimension))

print('\n')    

dimensions=(100,100)
for dimension in dimensions:
    print('重新赋值后'+str(dimension))




