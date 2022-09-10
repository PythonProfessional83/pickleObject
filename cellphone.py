# cellphone.py
'''
Simple class Cellphone with decorators.
'''
class Cellphone:
    def __init__(self, manufacturer, model, price):
        self.manufacturer = manufacturer
        self.model = model
        self. price = price
    
    @property
    def manuFacturer(self):
        return self.manufacturer
    
    @manuFacturer.setter
    def manuFacturer(self, manufacturer):
        self.manufacturer = manufacturer
    
    @property
    def moDel(self):
        return self.model
    
    @moDel.setter
    def moDel(self, model):
        self.model = model
    
    @property
    def priCe(self):
        return self.price
    
    @priCe.setter
    def priCe(self, price):
        self.price = price