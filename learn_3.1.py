bicycles = ['trek','cannondale','redline','specialized']
print(bicycles[-1].title())

#
message = "i like " + bicycles[2]
print(message.title())

#3.2
bicycles[0] = "ososos"
print(bicycles)

bicycles.append("asdqwe")
bicycles.append('wsxqaz')
print(bicycles)

bicycles.insert(1,'ccccc')
print(bicycles)

#del
del bicycles[1]
print(bicycles)

#pop()
poped_bicycles = bicycles.pop(0)
print(bicycles)
print(poped_bicycles)

#remove() 每次删除第一个值
removed_bicycle = bicycles.remove('redline')
print(bicycles)

