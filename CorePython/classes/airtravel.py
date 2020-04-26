""" Model for aircraft flights"""


class Test:
    pass


class Flight:

    def __init__(self, number, aircraft):
        if not number[:2].isalpha():
            raise ValueError(f"Invalid flight no {number[:2]}")
        if not number[:2].isupper():
            raise ValueError(f"Invalid flight no {number[:2]}")
        if not (number[2:].isdigit() and int(number[2:]) <= 9999):
            raise ValueError(f"Invalid route no {number[2:]}")
        self._number = number
        self._aircraft = aircraft
        rows, seats = aircraft.seating_plan()
        self._seats = [None] + [{letter: None for letter in seats} for _ in rows]

    def aircraft_model(self):
        return self._aircraft.model()

    def number(self):
        return self._number

    def airline(self):
        return self._number[:2]

    def alloacte_seats(self, seat, passenger):
        pass
    # if seat not in
    # seat already allocated
    # find the seat from the seat list and map
    # update the map

    def reallocate_seats(self,f,to):
        pass

    def make_borading_card_printer(self):
        pass
        # use generator and string format





class AirCraft:
    def __init__(self, registration, model, num_rows, num_seats_per_row):
        self._reregistration = registration
        self._model = model
        self._num_rows = num_rows
        self._num_seats_per_row = num_seats_per_row

    def registration(self):
        return self._reregistration

    def model(self):
        return self._model

    def seating_plan(self):
        return (range(1, self._num_rows + 1),
                "ABCDEFGHJK"[:self._num_seats_per_row])

def make_flight():
    pass
    #return Flight()

def main():
    make_flight()
    # make  air craft as base class
    # move init, registration and num_seats available method in base class
    # create two fifrent sub classes for aircraft

class AirBus739(AirCraft):
    pass