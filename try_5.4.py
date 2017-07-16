#2017年7月16日
#del a[:]
users=['fine','admin','asdasd','may','lol']
for user in users:
    if user == 'admin':
        print('Hello admin!')
    else:
        print('Hello ' + str(user))

no_users=['adfmin']
if no_users:
    del no_users[:]
    print(no_users)
else:
    print('no one')

#
ava_names = ['may','john','make','tommy','jack']
check_names=['may','John','make','tom','jacker']
for check_name in check_names:
    if check_name.lower() in ava_names:
        print('other')
    else:
        print('ok')
        
num=[1,2,3,4,5,6,7,8,9]        
for num1 in num:
    if num1==1:
        print(str(num1)+'st')
    elif num1==2:
        print(str(num1)+'nd')
    elif num1==3:
        print(str(num1)+'rd')
    else:
        print(str(num1)+'st')
        
        
        
        
        
        
        
        
        
        
        
        
