#
wannna = ['amy','mike','john','snow','anna']
print(wannna[-1].title())
changed_name = wannna[1] = 'jun'
removed_name = wannna.remove('anna')
added_name = wannna.append('may')
inserted_name = wannna.insert(0,'gay')
print(wannna)

#
while len(wannna) > 2:
    poped_name = wannna.pop()
    print(poped_name)

while len(wannna) > 0:
    del wannna[0]
    print(wannna)
