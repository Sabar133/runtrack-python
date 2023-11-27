def tapis1(taille): 
     
    bord="+" 
    for i in range(taille+1): bord +="-" 
    bord+="+" 

    print(bord)
     
    for i in range(taille+1): 
        tapis="" 
        for j in range(taille-i): tapis+="#" 
        tapis+=" " 
        for j in range(i): tapis+="#" 
        print("|" + tapis + "|") 
     
    print(bord) 
  
tapis1(10)