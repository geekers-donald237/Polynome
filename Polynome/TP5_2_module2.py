import TP5_2_module1
class Polynome:
    def __init__(self,tu):
        self.tuple = tu
    
    def __str__(self):
        return TP5_2_module1.poly_chaine(self.tuple)
    
    def __add__(self,other):
        return TP5_2_module1.poly_add(self.tuple,other.tuple)

    def evaluer(self,x):
        return TP5_2_module1.polyCalcul(self.tuple, x)
    
    def degre(self):
        return TP5_2_module1.poly_ceof(self.tuple)
    
    
    
