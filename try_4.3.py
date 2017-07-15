#2017年7月15日
for num5 in range(1,21):
    print(num5)
print('\n')
#list_large = [num6 for num6 in range(1,1000001)]
#for num7 in list_large:
    #print(num7)
#print(min(list_large))
#print(max(list_large))
#print(sum(list_large))

list_odd=[]
for num8 in range(1,21,2):
    list_odd.append(num8)
    print(num8)
print(list_odd)

list_3=[]
for num9 in range(3,34,3):
    list_3.append(num9)
    print(num9)
print(list_3)

list_tri = [num10**3 for num10 in range(1,11)]
print(list_tri)
