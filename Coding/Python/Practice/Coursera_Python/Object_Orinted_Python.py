class Data:
    def __init__(self,x):
        self.x=x
        print("Constructor values are : ",self.x)
    def party(self):
        self.x=self.x+1
        print("Party having value: ",self.x)
    def __del__(self):
        print("Destructor done")

data=Data(10)
data.party()
data.party()
data=Data(20)
print("New object values is : ",data.x)
