from TRABALHO.client import Client

class Order(Client):
    def __init__(self, total_price, status, first_name, last_name, address, cell_phone, email, gender):
        super().__init__(first_name, last_name, address, cell_phone, email, gender)