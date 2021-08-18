#! /usr/bin/env python3

import copy
import json
from datetime import timedelta
from typing import List

from args import Args
from trip import Trip
from booking import Booking
from flight import Flight, FlightInputDataset


def generate_first_legs(flights: List[Flight], args: Args) -> List[Trip]:
    """Generate first leg for each potential trip to get initial undone list."""
    first_legs = [f for f in flights if f.origin == args.origin and f.bags_allowed >= args.bags]
    undone = []
    for f in first_legs:
        trip = Trip(origin=args.origin, destination=args.destination,
                    bags_count=args.bags, roundtrip=args.roundtrip)
        trip.flights.append(f)
        undone.append(trip)

    return undone


def separate_done(undone: List[Trip], done: List[Trip]):
    """Move trips from undone to done list if they are done already after last extension."""
    out_done, out_undone = done, []
    for trip in undone:
        if trip.last_destination == args.destination:
            out_done.append(trip)
        else:
            out_undone.append(trip)

    return out_undone, out_done


def extend_undone(trip: Trip, flights: List[Flight]) -> List[Trip]:
    """Extend one undone trip by one connecting flight resulting in a list of trips."""
    extended = []
    for f in flights:
        extended_trip = copy.deepcopy(trip)
        if (f.origin == trip.last_destination
                and f.departure - trip.last_arrival <= timedelta(hours=6)
                and f.departure - trip.last_arrival >= timedelta(hours=1)
                and f.bags_allowed >= trip.bags_count
                and f.destination not in [f.origin for f in trip.flights]):
            extended_trip.flights.append(f)
            extended.append(extended_trip)
    return extended


def find_combinations(args, flights):
    """Find combinations for oneway trip using given input arguments and flights."""
    # print_args(args)
    stops = 0
    while stops <= args.stops:
        if stops == 0:
            undone, done = generate_first_legs(flights, args), []
            undone, done = separate_done(undone, done)
        else:
            to_extend, undone = undone, []
            for trip in to_extend:
                extended = extend_undone(trip, flights)
                undone.extend(extended)
            undone, done = separate_done(undone, done)
        # if stops == args.stops:
        #     print_trips(undone, done, stops)
        stops += 1

    return done


def to_json(bookings, args):
    """Serialize indentified bookings/combinations to JSON format."""
    bookings_dict = [booking.to_dict(args) for booking in bookings]
    return json.dumps(bookings_dict, default=str, indent=4)


if __name__ == '__main__':
    args = Args()
    flights = FlightInputDataset(csvfile=args.csvfile).get_flights()

    if not args.roundtrip:
        done_oneway = find_combinations(args, flights)
        bookings = [Booking([trip]) for trip in done_oneway]
    else:
        done_oneway = find_combinations(args, flights)
        args.switch_route()
        done_return = find_combinations(args, flights)

        bookings = []
        for idx, trip_oneway in enumerate(done_oneway):
            for idx2, trip_return in enumerate(done_return):
                if (trip_return.first_departure.date() -
                        trip_oneway.last_arrival.date() == timedelta(days=args.stay)):
                    bookings.append(Booking([trip_oneway, trip_return]))

    bookings.sort(key=lambda x: x.total_price)
    print(to_json(bookings, args))
