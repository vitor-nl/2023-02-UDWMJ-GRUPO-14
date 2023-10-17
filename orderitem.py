from product import Product
from order import Order

class Orderitem (Product, Order):
    def __init__(self, name, descripit, date_fabrication, is_active, category):
        super().__init__(name, descripit, date_fabrication, is_active, category)
    def __init__(self, total_price, status, first_name, last_name, address, cell_phone, email, gender):
        return super().__init__(total_price, status, first_name, last_name, address, cell_phone, email, gender)