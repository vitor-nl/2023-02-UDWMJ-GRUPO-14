from TRABALHO.client import Client
from TRABALHO.socialnetwork import Socialnetwork

class Client_socialnetwork(Client, Socialnetwork):
    def __init__(self, first_name, last_name, address, cell_phone, email, gender):
        super()._init_(first_name, last_name, address, cell_phone, email, gender)
    def __init__ (self, name, description):
        super().__init__(name, description)