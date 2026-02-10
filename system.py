import json
from bus import Bus
from passenger import Passenger

FILE = "data.json"


class BusManagementSystem:

    def __init__(self):
        self.data = {"buses": [], "passengers": []}
        self.load_data()

    # ---------------- File Handling ----------------
    def load_data(self):
        try:
            with open(FILE, "r") as f:
                self.data = json.load(f)
        except:
            self.save_data()

    def save_data(self):
        with open(FILE, "w") as f:
            json.dump(self.data, f, indent=4)

    # ---------------- Bus Operations ----------------
    def add_bus(self):
        try:
            bus_id = input("Bus ID: ")
            route = input("Route: ")
            schedule = input("Schedule: ")
            seats = int(input("Total Seats: "))

            bus = Bus(bus_id, route, schedule, seats)
            self.data["buses"].append(bus.to_dict())
            self.save_data()

            print("✅ Bus added successfully!")
        except ValueError:
            print("❌ Invalid input!")

    def view_buses(self):
        print("\n--- Bus List ---")
        for b in self.data["buses"]:
            print(b)

    def delete_bus(self):
        bus_id = input("Enter Bus ID to delete: ")
        self.data["buses"] = [b for b in self.data["buses"] if b["bus_id"] != bus_id]
        self.save_data()
        print("✅ Bus deleted.")

    # ---------------- Passenger Operations ----------------
    def book_ticket(self):
        name = input("Passenger Name: ")
        bus_id = input("Bus ID: ")

        for bus in self.data["buses"]:
            if bus["bus_id"] == bus_id:
                if bus["booked"] < bus["seats"]:
                    passenger = Passenger(name, bus_id)
                    self.data["passengers"].append(passenger.to_dict())
                    bus["booked"] += 1
                    self.save_data()
                    print("🎟 Ticket booked!")
                    return
                else:
                    print("❌ Bus full!")
                    return

        print("❌ Bus not found!")

    def view_passengers(self):
        print("\n--- Passenger List ---")
        for p in self.data["passengers"]:
            print(p)
