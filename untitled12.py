class avtomobillar:
    
    def avto_info(self, kompaniya, model, rangi, karobka, yili, narxi,): 
        
        self.model = model
        self.rangi = rangi
        self.karobka = karobka
        self.yili = yili
        self.narxi =narxi
        return 
        
    avto1 = avto_info("GM","Malibu", "Qora", "Avtomat",2022)
    avto2 = avto_info("GM","Gentra", "Qizil", "Avtomat",2023, 85000) 
    avtolar = [avto1, avto2]

   

