#2017年7月16日

#if if-else
age = 17
if age > 18:
    print('Old enough')
else:
    print('too young')    

#if-elif-else
#age = 19
#if age < 4:
    #print('$0')
#elif age<18:
    #print('$5')
#else:
    #print('$10')
    
#高效率 适当情况使用elif 代替 else 结尾，避免无效数据
age = 19
if age < 4:
    price = 0
elif age<18:
    price = 5
else:
    price = 10
print('The price is '+str(price))

#只想执行一个代码块，就使用 if-elif-else 结构；
#如果要运行多个代码块，就使用一系列独立的 if 语句

















