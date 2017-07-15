#日期
#切片
players = ['charles','martina','michael','florence','eli']
print(players[1:3])
print(players[:3])
print(players[2:])
print(players[-1:])

#遍历
print('遍历前三人大写首字母')
for player in players[:3]:
    print(player.title())

#复制列表
my_foods = ['rice','pizza','cake']
friend_foods = my_foods[1:]
my_foods.append('ice cream')
friend_foods.insert(1,'milk')
print('\nMy foods are: '+ str(my_foods))
print('My friend\'s foods are:'+str(friend_foods))




