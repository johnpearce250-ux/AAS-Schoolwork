class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
    
    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
    
    def list_items(self):
        return self.items
    
    def __len__(self):
        return len(self.items)
    
    def __getitem__(self, index):
        return self.items[index]
    
    def __contains__(self, item):
        return item in self.items
    
    def __iter__(self):
        return iter(self.items)
    
cart=Cart()
cart.add_item('Laptop')
print(len(cart))  # Output: 1
print('Laptop' in cart)  # Output: True
