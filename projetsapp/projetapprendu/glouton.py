def glouton():
    billet500 = 0
    billet200 = 0
    billet100 = 0
    billet50 = 0
    billet20 = 0
    billet10 = 0
    billet5 = 0
    piece2 = 0
    piece1 = 0
    while arendre != 0:
        
        if arendre >= 500:
            arendre -= 500
            billet500 += 1
            
        elif arendre >= 200:
            arendre -= 200
            billet200 += 1
            
        elif arendre >= 100:
            arendre -= 100
            billet100 += 1
            
        elif arendre >= 50:
            arendre -= 50
            billet50 += 1
            
        elif arendre >= 20:
            arendre -= 20
            billet20 += 1
            
        elif arendre >= 10:
            arendre -= 10
            billet10 += 1
            
        elif arendre >= 5:
            arendre -= 5
            billet5 += 1
            
        elif arendre >= 2:
            arendre -= 2
            piece2 += 1
            
        elif arendre >= 1:
            arendre -= 1
            piece1 += 1

    print(billet500, billet200, billet100, billet50, billet20, billet10, billet5, piece2, piece1)   