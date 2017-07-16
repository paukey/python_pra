#2017年7月16日
#5.4.1
request_shoppings = ['mushroom','green peppers','extra cheese']

for request_shopping in request_shoppings:
    if request_shopping == 'mushroom':
        print('sorry')
    else:
        print('ADD: '+str(request_shopping))

print('all right')

#list 空
request_shop=[]

if request_shop:
    print('NOT NULL')
else:
    print('other')

#多个列表
available_shoppings = ['mushroom','green peppers','extra cheese']
request_shs = ['mushroom','extra cheese','olives']

for request_sh in request_shs:
    if request_sh in available_shoppings:
        print('ADD: '+str(request_sh))
    else:
        print('Sorry , no '+str(request_sh))
print('Finsh!')




























