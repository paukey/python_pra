#
players = ['charles','martina','michael','florence','eli']
print(players[0:3])
print(players[1:4])
print(players[-3:])

players_new = players[:]
players_new.append('fun')
print(players)
print(players_new)

for pla in players_new:
    print(pla)

