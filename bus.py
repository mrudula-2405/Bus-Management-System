class Bus:
    def __init__(self, bus_id, route, schedule, seats):
        self.bus_id = bus_id
        self.route = route
        self.schedule = schedule
        self.seats = seats
        self.booked = 0

    def to_dict(self):
        return self.__dict__
