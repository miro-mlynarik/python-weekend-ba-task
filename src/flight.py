from datetime import datetime
from typing import TextIO, List
import csv


class Flight:
    """Class for the individual flight with scheduled date, time, origin and destination."""
    def __init__(self, flight_no: str, origin: str, destination: str, departure: datetime,
                 arrival: datetime, bags_allowed: int, base_price: float, bag_price: float):
        self.flight_no = flight_no
        self.origin = origin
        self.destination = destination
        self.departure = departure
        self.arrival = arrival
        self.bags_allowed = bags_allowed
        self.base_price = base_price
        self.bag_price = bag_price

    def __str__(self) -> str:
        string = \
            f"Flight({self.origin} -> {self.destination} @ {self.departure} ~ {self.travel_time})"
        return string

    @property
    def travel_time(self):
        return self.arrival - self.departure

    def to_dict(self):
        return dict(flight_no=self.flight_no, origin=self.origin, destination=self.destination,
                    departure=self.departure.strftime("%Y-%m-%dT%H:%M:%S"),
                    arrival=self.arrival.strftime("%Y-%m-%dT%H:%M:%S"), base_price=self.base_price,
                    bag_price=self.bag_price, bags_allowed=self.bags_allowed)


class FlightInputDataset:
    """Class storing input flights dataset from which combinations will be generated."""
    def __init__(self, csvfile: TextIO):
        self.csvfile = csvfile

    def get_flights(self) -> List[Flight]:
        """Get list of Flight objects from csv file."""
        flights = []
        with open(self.csvfile, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                flights.append(
                    Flight(
                        flight_no=row['flight_no'],
                        origin=row['origin'],
                        destination=row['destination'],
                        departure=datetime.strptime(row['departure'], "%Y-%m-%dT%H:%M:%S"),
                        arrival=datetime.strptime(row['arrival'], "%Y-%m-%dT%H:%M:%S"),
                        bags_allowed=int(row['bags_allowed']),
                        base_price=float(row['base_price']),
                        bag_price=float(row['bag_price'])
                    )
                )

        return flights
