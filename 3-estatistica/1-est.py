num_friends = np.array([1,2,3,4,5,6,7,8,9,10,9,8,7,6,5,4,3,2,1])

#numeros de amigos 
len(num_friends)

#maior valor 
num_friends.max()

#menor valor
num_friends.min()

#ordenar 
num_friends.sort()

#media
num_friends.mean()

#mediana


#moda


#dispersão ou amplitude
num_friends.max() - num_friends.mix()

#variancia
variace = np.sum(np.square([x_list-myfriends.mean() for x_list in num_friends]))

#standart deviantion
np.sqrt(np.sum(np.square([x_list-myfriends.mean() for x_list in num_friends])))
#or
num_friends.std()

#covariancia

a = np.array([1,2,3,4,5,6,7,8])
b = np.array([2,4,6,8,10,12,14,18])

np.sum(np.array([x_a - a.mean() for x_a in a]) * np.array([x_b - b.mean() for x_b in b]))



