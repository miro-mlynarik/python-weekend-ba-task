from typing import List
from trip import Trip
from datetime import timedelta


class Booking:
    def __init__(self, trips: List[Trip]):
        self.trips = trips

    def __str__(self):
        if len(self.trips) > 1:
            return (
                f"Booking({self.trips[0]}\n{' '*8}{self.trips[1]}\n{' '*8}for {self.total_price})"
            )
        else:
            return f"Booking({self.trips[0]})"

    @property
    def total_price(self):
        return sum(trip.total_price for trip in self.trips)

    @property
    def travel_time(self):
        return sum([trip.travel_time for trip in self.trips], timedelta(seconds=0))

    @property
    def bags_allowed(self):
        return min(trip.bags_allowed for trip in self.trips)

    @property
    def flights(self):
        flights = []
        for trip in self.trips:
            for flight in trip.flights:
                flights.append(flight)

        return flights

    def to_dict(self, args):
        return dict(flights=[flight.to_dict() for flight in self.flights],
                    bags_allowed=self.bags_allowed, bags_count=args.bags,
                    destination=args.destination, origin=args.origin,
                    total_price=self.total_price, travel_time=self.travel_time)
