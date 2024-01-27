#__init__(name)

#name nomli fayl yaratilsin va uni nomini 
#saqlovchi self.name xususiyat yarating;
class uqtuvchi:
    def init(self, nomi):
        self.nomi = nomi          
        pass

    def ishlashi(self):
        with open(f"{self.nomi}", "r") as fayl:
            return fayl.read()
    
    def yozish(self, matn):
        with open(f"{self.nomi}", "w") as fayl:
            fayl.write(matn)
 
    print(file.uqish())
      