def sets():
    set_1 = {1,3,5,8}
    set_2 = {2,4,5,6,7,8,9}
    simetrica = set_1 | set_2
    print(simetrica)
    inters = simetrica - set_2
    print(inters)
    print('esto funciono')
sets()    
