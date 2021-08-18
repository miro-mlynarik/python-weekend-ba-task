
class Trip:
    """Class for the complete trip consisting of a combination of flights between A -> B."""
    def __init__(self, origin: str, destination: str, bags_count: int = 0, roundtrip: bool = False):
        self.origin = origin
        self.destination = destination
        self.bags_count = bags_count
        self.roundtrip = roundtrip
        self.flights = []

    def __str__(self) -> str:
        return (
            f"Trip({self.first_departure}-[{','.join([f.flight_no for f in self.flights])}]: " +
            f"{' -> '.join([f.origin + '->' + f.destination for f in self.flights])} " +
            f"~ {self.travel_time} " +
            f"@ {self.stops} stops for {self.total_price} EUR with {self.bags_count} bags " +
            f"({self.bags_allowed} allowed))"
        )

    @property
    def stops(self):
        return len(self.flights) - 1

    @property
    def total_price(self):
        return sum(f.base_price + self.bags_count * f.bag_price for f in self.flights)

    @property
    def travel_time(self):
        return self.last_arrival - self.first_departure

    @property
    def last_destination(self):
        return self.flights[-1].destination

    @property
    def last_arrival(self):
        return self.flights[-1].arrival

    @property
    def first_origin(self):
        return self.flights[0].origin

    @property
    def first_departure(self):
        return self.flights[0].departure

    @property
    def bags_allowed(self):
        return min(f.bags_allowed for f in self.flights)
