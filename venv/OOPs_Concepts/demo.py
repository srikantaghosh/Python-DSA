class Product:
    quantity =200
    ## Construcion
    def __init__(self,name,price):
        self.name = name
        self.price =price


p1 = Product('Mac',1200)
print(p1.name, p1.price)


