class student:
    def personalDetails(self,name,age,mobile,mailid):
        print(f"Name :{name}, \nAge  :{age}, \nPhone :{mobile},
              \nMail id :{mailid}")

    def courseDetails(self,course,fees,duration,month):
        print(f"Course :{course}, \nFees :{fees},
              \nDuration :{duration}, \nRegistered :{month}")
s = student()
s.personalDetails("Mounika",22,9384542020,"m@gmail.com")
s.courseDetails("Python",15900,"64 Hours","January")

class Mobile:
    def spec(self):
        print("Brand     : Vivo")
        print("Series    : y71")
        print("Color     : Black , Aqua")
        
    def offers(self):
        print(" ------- Offer 1 ------- ")
        print("RAM      : 16GB")
        print("Internal : 256GB")
        print("Price    : Rs.55,000")
        print("Offer %  : 20%")

        print(" ------- Offer 2 ------- ")
        print("RAM      : 8GB")
        print("Internal : 128GB")
        print("Price    : Rs.25,000")
        print("Offer %  : 12%")

        print(" ------- Offer 3 ------- ")
        print("RAM      : 4GB")
        print("Internal : 64GB")
        print("Price    : Rs.15,000")
        print("Offer %  : 4%")

m = Mobile()
m.spec()
m.offers()






        
