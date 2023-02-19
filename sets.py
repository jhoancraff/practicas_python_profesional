#para combinar los elementos
mi_set_1 = {1,3,5}
mi_set_2 = {2,4,5}

mi_set_3 = mi_set_1 | mi_set_2
print(mi_set_3)

# para quedarme con los elementos que estan repetidos

set_1 = {6,0,3}
set_2 = {6,9,3}

set_3 = set_1 & set_2
print(set_3)

# para combinar y restas los elementos repetidos de un set a otro

cet_1 = {5,6,7}
cet_2 = {3,4,5}

cet_3 = cet_1 - cet_2
print(cet_3)

# para quedarme con todos los sets menos los repetidos

ret_1 = {5,6,7}
ret_2 =  {3,4,5}

ret = ret_1 ^ ret_2
print(ret)