class Observer:
    def update(self, message: str):
        pass




class CatalogProxy(Observer):
    def __init__(self, catalog: Catalog):
        super().__init__()
        self.catalog = catalog

    def send_newsletter(self):
        latest_vehicles = self.catalog.get_latest_vehicles(5)
        message = f"Latest vehicles: {latest_vehicles}"
        self.notify(message)