#single inheritance
class briyani:
    def ingredients(self):
        ing = ["oil","spices","rice","water","tomato","onion","ginger garlic paste",
               "Mint leaves","masala","curd","ghee"]
        print("🥘🍲   Ingredients   🥘🍲\n")
        for i in ing:
            print("==> ",i)
    def recipe(self):
        print("\n🧑‍🍳 Steps to Cook 🧑‍🍳\n")
        print("Step 1 : oil / ghee then roast the spices")
        print("Step 2 : ginger garlic paste , onion , tomato , masala")
        print("Step 3 : after 5mins add water and rice")
        print("Step 4 : after 20mins add lemon and ready to serve")

class chickenbriyani(briyani):
    def addedingredients(self):
        print("Addtional Ingredient : Chicken")

b = briyani()
b.ingredients()
b.recipe()

c=chickenbriyani()
c.ingredients()
c.addedingredients()
c.recipe()

#hierarchical inheritance
class vegbriyani(briyani):
    def addedingredients(self):
        print("Addtional Ingredient : Vegetables")

class mushroombriyani(briyani):
    def addedingredients(self):
        print("Addtional Ingredient : Mushroom")

m=mushroombriyani()
m.ingredients()
m.addedingredients()
m.recipe()

#multiple inheritance

class dress:
    def women(self):
        print("Tops and Tunics \nSaree \nBlouse \nShirts \n")
    def men(self):
        print("Shirt \nPants \nT-shirt \n")

class homeAppliances:
    def homedecors(self):
        print("Curtains \nMat \nKitchen Utilites \n")
    def electronics(self):
        print("Mobile \nTV \n")
    def furnitures(self):
        print("Chairs \nTables \n")
        
class accessories:
    def footware(self):
        print("Shoes \nFlats \nHeels \nSandals \nFlipflops \ncrocs \n")
    def jewellry(self):
        print("Chains \nBangles \nEarrings \nRings \nAnklets \n")
        
class meesho(dress,homeAppliances,accessories):
    def title(self):
        print(" Welcome to Meesho ")

m=meesho()
m.title()
m.women()
m.men()
m.homedecors()
m.electronics()
m.furnitures()
m.footware()

'''#multilevel inheritance

class GP:
    def GPskills(self):
        print("Drawing")

class P(GP):
    def Pskills(self):
        print("Driving")

class C(P):
    def Cskills(self):
        print("Cooking")

gp = GP()
gp.GPskills()

p = P()
p.GPskills()
p.Pskills()

c = C()
c.GPskills()
c.Pskills()
c.Cskills()'''


class phone:
    def commonuse(self):
        print("Communication")

class Type1(phone):
    def model1(self):
        print("Button phone")

class Type2(phone):
    def model2(self):
        print("Smart phone")

class sim(Type1,Type2):
    def simcard(self):
        print("Insert sim card for communication")

p = phone()
p.commonuse()

t1 = Type1()
t1.commonuse()
t1.model1()


t2 = Type2()
t2.commonuse()
t2.model2()

s = sim()
s.commonuse()
s.model1()
s.model2()
s.simcard()

m.jewellry()




