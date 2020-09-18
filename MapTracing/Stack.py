#PILA PARA ORDENAMIENTO DE DATOS
class Stack(object):
    def __init__(self):
        self.items = []

    def push(self, date):
        self.items.append(date)
        
    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.items.pop()

    def is_empty(self):
        if len(self.items) == 0:
            return True
        else:
            return False

    def get_Size(self):
        return len(self.items)

    def get_element(self,x):
        return self.items[x]
    
    def get_elements(self):

        if self.is_empty():
            return None
        else:
            return self.items
    
    def destroyer(self,index):
        self.items.pop(index)
