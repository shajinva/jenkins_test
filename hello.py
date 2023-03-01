class Hello_Name():
    
    def __init__(self,name,age):
        self.name = name
        self.age = age        
        
    def run_hello(self):
        print("my name is", self.name)
        
    def run_age(self):
       print("my age is :" , self.age)
        
obj =  Hello_Name("shajin",45)

obj.run_hello()  
obj.run_age()     
            
        
        
        
    
    
        
        
        