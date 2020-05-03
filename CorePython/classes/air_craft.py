# class example


class Flight:
    def __init__(self, number, aircraft):
        if not number[:2].isalpha():
            raise ValueError("Invalid Flight code")
        if not number[:2].isupper():
            raise ValueError("Invalid Flight code")
        if not number[2:].isdigit():
            raise ValueError("Invalid Flight Route number")
        if not int(number[2:]) <= 9999:
            raise ValueError("Invalid Flight Route number")

        self._number = number
        self._aircraft = aircraft
        rows, seats = self._aircraft.seats()
        self._seating = [None] + [{letter: None for letter in seats} for _ in rows]

    def flight_no(self):
        return self._number

    def aircraft_model(self):
        return self._aircraft.model()

    def no_available_seats(self):
        return sum(sum(1 for s in row.values() if s is None) for row in self._seating if row is not None)

    def allocate_seat(self, seat, passenger):
        row, letter = self._parse_seats(seat)
        if self._seating[row][letter] is None:
            self._seating[row][letter] = passenger
        else:
            print(f"Seat {seat} is already occupied")

    def _parse_seats(self, seat):
        rows, seats = self._aircraft.seats()
        letter = seat[-1]
        try:
            row = int(seat[:-1])
        except ValueError:
            raise ValueError("Seat row not exist")

        if row not in rows:
            raise ValueError("Seat Row not exist")
        if letter not in seats:
            raise ValueError("Seat Not exist")
        return row, letter

    def make_boarding_cards(self, card_printer):
        for passenger, seat in sorted(self._passenger_seats()):
            card_printer(passenger, seat, self.flight_no(), self.aircraft_model())

    def _passenger_seats(self):
        rows, seats = self._aircraft.seats()
        for row in rows:
            for seat in seats:
                passenger = self._seating[row][seat]
                if passenger is not None:
                    yield passenger, f"{row}{seat}"


class AirCraft:

    def __init__(self, registration):
        self._registration = registration

    def get_registration(self):
        return self._registration

    def seats(self):
        rows, seats = self.seating_plan()
        return rows, seats


class AirbusA319(AirCraft):
    def model(self):
        return "Airbus A319"

    def seating_plan(self):
        return range(1, 23), "ABCDEF"


class Boeing777(AirCraft):
    def model(self):
        return "Boeing 777"

    def seating_plan(self):
        return range(1, 56), "ABCDEGHJK"


def card_printer(passenger, seat, flight_number, aircraft):
    output = (
        f"| Name: {passenger}"
        f"  Flight: {flight_number}"
        f"  Seat: {seat}"
        f"  Aircraft: {aircraft}"
        f" |"
    )
    banner = '+' + '-' * (len(output) - 2) + '+'
    border = '|' + ' ' * (len(output) - 2) + '|'
    lines = [banner, border, output, border, banner]
    card = '\n'.join(lines)
    print(card)
    print()


def main():
    f = Flight("BA758", AirbusA319("G-EUPT"))
    f.allocate_seat("12A", "Guido van Rossum")
    f.allocate_seat("15F", "Bjarne Stroustrup")
    f.allocate_seat("15E", "Anders Hejlsberg")
    f.allocate_seat("1C", "John McCarthy")
    f.allocate_seat("1D", "Richard Hickey")

    print(f"Aircraft Model {f.aircraft_model()}")
    print(f"No available seats {f.no_available_seats()}")
    f.make_boarding_cards(card_printer)

    g = Flight("AF72", Boeing777("F-GSPS"))
    g.allocate_seat('55K', 'Larry Wall')
    g.allocate_seat('33G', 'Yukihiro Matsumoto')
    g.allocate_seat('4B', 'Brian Kernighan')
    g.allocate_seat('4A', 'Dennis Ritchie')


if __name__ == '__main__':
    main()
