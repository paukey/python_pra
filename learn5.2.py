#2017年7月15日

#5.1
cars = ['audi','bmw','subaru','toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

#5.2
#条件测试
car_test = 'Audi'
car_test.lower()=='audi'

request_topping = 'mushrooms'
if request_topping != 'anchovies':
    print('\nHold the anchovies!')

#and or
#要判断特定的值是否已包含在列表中，可使用关键字 in
#要判断特定的值 未 包含在列表中，可使用关键字 not in
name=['amy','mike','john']
user = 'may'

if user not in name:
    print('\nI can\'t found!')

#布尔表达式
