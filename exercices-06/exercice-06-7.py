# exo 6.7
# Inversez la position des valeurs `bar` et `lorem` puis affichez le résultat

my_list = ['foo', 'bar', 'baz', 'lorem', 'ipsum']

# réponse 6.7
pos1 = my_list.index('bar')
pos3 = my_list.index('lorem')

my_list[pos1], my_list[pos3] = my_list[pos3], my_list[pos1]

print(my_list)