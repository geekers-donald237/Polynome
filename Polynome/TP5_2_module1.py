def polyCalcul(p,x):
    resultat = 0;
    for i in range(len(p)):
        resultat+=p[i]*(x**i);
    return resultat 


def poly_ceof(p):
    degre_max = 0;
    for i in range(len(p)):
        if(p[i] != 0):
            degre_max = i
    return degre_max;


def poly_add(p1,p2):
    resulat , min_p = list(p2),list(p1)
    if(len(p1) > len(p2)):
        resulat ,min_p = list(p1),list(p2)
    for i in range (len(min_p)):
        resulat[i]+=min_p[i];
    
    return tuple(resulat);        
    

def poly_chaine(p):
    resultat = " "
    if(len(p)>0):
        if(p[0] != 0):
            resultat += str(p[0])
        for i in range(1,len(p)):
            resultat += " + " + str(p[i]) + "x^"+str(i)
            
    return resultat;        
            
            
def poly_simplifie(p):
    resultat = ()
    degre_max = poly_ceof(p)   
    for i in range (degre_max+1):
        resultat += (p[i],)
    return resultat ;        
                
                

if __name__ == '__main__':
    p1 = (7,2.3,-9.12,0,7.9)
    p2 = (23.4,1.1,11.3,0,0,4,12,85,0,0,0)
    print("\n\n")
    print("Evaluation de p1 :",polyCalcul(p1,1))
    print("\n")
    print("Evaluation de p2 :",polyCalcul(p2,1))
    print("\n")
    print("Degre max de p1 :" ,poly_ceof(p1))
    print("\n")
    print("Degre max de p2 :" ,poly_ceof(p2))
    print("\n")
    print("Addition de p1 et p2 :",poly_chaine(poly_add(p1,p2)))
    print("\n")
    print("La chaine p1 est :",poly_chaine(p1))
    print("\n")
    print("La chaine p2 est :",poly_chaine(p2))
    print("\n")
    print("p1 simplifie est :",poly_chaine(poly_simplifie(p1)))
    print("\n")
    print("p2 simplifie est :",poly_chaine(poly_simplifie(p2)))
    