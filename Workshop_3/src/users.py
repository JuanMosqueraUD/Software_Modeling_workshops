from catalog import ProxyCatalog
from vehicles import Vehicle

class User:
    def __init__(self, name:str, pasword:str):
        self.name = name
        self.password = pasword


    def search_vehicle(self, catalog: ProxyCatalog, filter:str, filter_value):
        if filter == "price":
            return catalog.get_price_by_range(filter_value)
        if filter == "max_speed":
            return catalog.search_max_speed(filter_value)
        if filter == "combustion_type":
            return catalog.get_type_compustion(filter_value)
        else:
            return catalog.get_all_vehicles()



class UserDecorator():
    def __init__(self, user):
        self.wrapped = user

    def search_vehicle(self, catalog: ProxyCatalog, filter:str, filter_value):
        return self.wrapped.search_vehicle(catalog, filter, filter_value)

class AdminUserDecorator(UserDecorator):
    def __init__(self, user):
        self.wrapped = user

    def create_vehicle(self, catalog: ProxyCatalog):
        pass

    def delete_vehicle(self, catalog: ProxyCatalog):

        pass

