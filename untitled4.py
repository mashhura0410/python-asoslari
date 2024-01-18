#inkapsulyatsiya
class Shaxs:
    __odamlar_soni=0
    def __init__(self, ismi, familyasi, ish_joyi,JSHSHIR):
        self.JSHSHIR = JSHSHIR
        self.ismi = ismi
        self.familyasi = familyasi
        self.ish_joyi = ish_joyi
        
        def change__JSHSHIR(self,new):
            self.__JSHSHIR=new
            
        def get_JSHSHIR(self):
            return self.__JSHSHIR
        
        def get__count(cls):
            return cls.___odamlar_soni
        
        def get__info(self):
            return f"{self.ismi} {self.ish_joyi}"
obj1=Shaxs("Mashhura", "Fayzullayeva", "Tatu filial", 12345678900987) 
obj2=Shaxs("Hilola", "Sadiqova", "Pedakogika", 9876543212346)
            
            
       
       

