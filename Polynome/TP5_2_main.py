
from TP5_2_module2 import Polynome
if __name__ == '__main__':
    p1 = ()
    p2 = ()
    p1 = eval(input("entrer votre chaine de monomes separes par des virgules pour le polynome 1 : "))
    p2 = eval(input("entrer votre chaine de monomes separes par des virgules pour le polynome 2 : "))
    
    p1 = Polynome(p1)
    p2 = Polynome(p2)
    
    print("le polynome p1 est :",p1)
    print("le polynome p2 est : {}\n".format(p2))

    print("le degre du polynome p1 est :",(p1.degre()))
    print("le degre du polynome p2 est : {}\n".format((p2.degre())))
    
    p3 = p1+p2
    p3 = Polynome(p3)
    print("La somme de p1 + p2 est egale a : {}\n".format(p3.__str__()))
    
    for i in range(-5,6,1):
        print("l'evaluation de p1 avec la valeur {} donne {}".format(i,p1.evaluer(i)))
        