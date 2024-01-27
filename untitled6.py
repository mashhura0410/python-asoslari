# class bo'yicha yechish
class Text:
    def init(self, nomi):
        self.nomi = nomi          
        pass

    def uqish(self):
        with open(f"{self.nomi}", "r") as fayl:
            return fayl.read()
    
    def yozish(self, matn):
        with open(f"{self.nomi}", "w") as fayl:
            fayl.write(matn)

file = Text("myfile.txt")
file.yozish("Assalom Uzbekistan")
print(file.uqish())