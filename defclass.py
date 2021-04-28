class Car(object):
    def __init__(self,brand,model,torque,color,cost):
        self.brand = brand
        self.model = model
        self.torque = torque
        self.color = color
        self.cost = cost

    def getcost(self,model):
        self.cost = self.model*100
        print(self.cost+''+'Lk')

    def getinfo(self,brand,model,color,torque,cost):
        print(self.brand+' '+self.model+' '+'which has '+self.torque+' '+'is in '+self.color+' '+'and costs ₹'+self.cost+' '+'only')      

Ford = Car("BMW","X30","1500","blue","25000000")

print(Ford.getinfo("BMW","X50","2000","blue","30000000"))
           