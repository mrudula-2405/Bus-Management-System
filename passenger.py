class Passenger:
    def __init__(self, name, bus_id):
        self.name = name
        self.bus_id = bus_id

    def to_dict(self):
        return self.__dict__
