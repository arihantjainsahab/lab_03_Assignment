#My Python Code

class FlightInfo:
    def __init__(self, id_code, src, dest, fare):
        self.id_code = id_code
        self.src = src
        self.dest = dest
        self.fare = fare

class FlightDatabase:
    def __init__(self):
        self.flight_data = []

    def add_flight(self, flight):
        self.flight_data.append(flight)

    def search_by_location(self, location):
        result = []
        for flight in self.flight_data:
            if flight.src == location or flight.dest == location:
                result.append(flight)
        return result

    def search_from_location(self, location):
        result = []
        for flight in self.flight_data:
            if flight.src == location:
                result.append(flight)
        return result

    def search_between_locations(self, src, dest):
        result = []
        for flight in self.flight_data:
            if flight.src == src and flight.dest == dest:
                result.append(flight)
        return result

def main():
    flight_records = FlightDatabase()

    flight_entries = [
        ("AI161E90", "BLR", "BOM", 5600),
        ("BR161F91", "BOM", "BBI", 6750),
        ("AI161F99", "BBI", "BLR", 8210),
        ("VS171E20", "JLR", "BBI", 5500),
        ("AS171G30", "HYD", "JLR", 4400),
        ("AI131F49", "HYD", "BOM", 3499)
    ]

    for entry in flight_entries:
        flight = FlightInfo(entry[0], entry[1], entry[2], entry[3])
        flight_records.add_flight(flight)

    while True:
        print("Search Options:")
        print("1. Flights for a particular Location")
        print("2. Flights From a Location")
        print("3. Flights between two Locations")
        choice = int(input("Enter your choice (1/2/3): "))

        if choice == 1:
            location = input("Enter the location: ")
            result = flight_records.search_by_location(location)
        elif choice == 2:
            location = input("Enter the source location: ")
            result = flight_records.search_from_location(location)
        elif choice == 3:
            src = input("Enter the source location: ")
            dest = input("Enter the destination location: ")
            result = flight_records.search_between_locations(src, dest)
        else:
            print("Invalid choice!")
            continue

        if result:
            print("Flight ID\tFrom\tTo\tPrice")
            for flight in result:
                print(f"{flight.id_code}\t{flight.src}\t{flight.dest}\t{flight.fare}")
        else:
            print("No flights found for the given criteria.")

        another_search = input("Do you want to perform another search? (yes/no): ")
        if another_search.lower() != "yes":
            break

if __name__ == "__main__":
    main()

