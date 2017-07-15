#3-8

trip = ['paris','australia','newyork','french','japan']

print('原始顺序'+str(trip))
print('\nsorted排序'+str(sorted(trip)))
print('再次打印'+str(trip))
print('\nsorted排序reverse'+str(sorted(trip,reverse=True)))
print('再次打印'+str(trip))

trip.reverse()
print('\n使用reverse()'+str(trip))
print('再次打印'+str(trip))

trip.reverse()
print('\nagain使用reverse()'+str(trip))
print('再次打印'+str(trip))

trip.sort()
print('\nsort()'+str(trip))
print('再次打印'+str(trip))

#3-9 len()
lnu=len(trip)
print('\n'+str(lnu))


