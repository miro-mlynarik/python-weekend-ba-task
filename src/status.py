
def print_trips(undone, done, stops, only_done=True):
    print(f"\nDone trips with max {stops} stops: {len(done)}")
    [print(i) for i in done]
    if not only_done:
        print(f"Undone trips with max {stops} stops: {len(undone)}")
        [print(i) for i in undone]


def print_bookings(result):
    print(f"\nFinal bookings to be exported: {len(result)}")
    [print(trip) for trip in result]


def print_args(args):
    print(f"Args:\nO&D: {args.origin}-{args.destination}\nBAG: {args.bags}\n" +
          f"RET: {args.roundtrip}\nSTOPS: {args.stops}\nSTAY: {args.stay}")
