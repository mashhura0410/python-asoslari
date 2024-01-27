class uqtuvchi:
    def init(self, ismi, fani, maktabi, sinfi,):
        self.ismi=ismi
        self.fani=fani
        self.maktabi=maktabi
        self.sinfi=sinfi
        pass

    def ishlashi(self):
        with open(f"{self.fani}", "r") as fayl:
            return fayl.read()
    
    

