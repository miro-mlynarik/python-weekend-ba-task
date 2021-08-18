import argparse


class Args:
    """Class for reading and validating program's input arguments."""
    def __init__(self):
        args = self.parse_args()
        self.validate_args(args)

        self.csvfile = args.csvfile
        self.origin = args.origin
        self.destination = args.destination
        self.bags = args.bags
        self.roundtrip = args.roundtrip
        self.stops = args.stops
        self.stay = args.stay

    def parse_args(self) -> argparse.Namespace:
        parser = argparse.ArgumentParser()
        parser.add_argument("csvfile", type=str, help="Flights dataset in csv format")
        parser.add_argument("origin", type=str, help="Origin airport code")
        parser.add_argument("destination", type=str, help="Destination airport code")
        parser.add_argument("--bags", type=int, default=0, help="Number of bags")
        parser.add_argument("--roundtrip", action="store_true", default=False, help="Return trip")
        parser.add_argument("--stops", type=int, default=4, help="Maximum number of stops")
        parser.add_argument("--stay", type=int, default=3, help="Number of nights in destination")
        args = parser.parse_args()

        return args

    def validate_args(self, args: argparse.Namespace):
        if not args.csvfile.endswith('csv'):
            raise ValueError('Failed to read csv file provided in the first argument.')
        if len(args.origin) != 3:
            raise ValueError('Origin argument must have length 3.')
        if len(args.destination) != 3:
            raise ValueError('Destination argument must have length 3.')
        if args.bags < 0:
            raise ValueError('Bags argument must be non-negative.')
        if args.stops < 0:
            raise ValueError('Stops argument must be non-negative.')
        if args.stay < 0:
            raise ValueError('Stay argument must be non-negative.')

    def switch_route(self):
        self.origin, self.destination = self.destination, self.origin
