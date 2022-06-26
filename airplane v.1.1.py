class AirplaneTwoColumns:
    """  Airplane v.1.1"""
    column = '......'

    def __init__(self):
        self.rows = int(input('Enter the number of rows in the airplane. >>> : '))
        self.total_seats = [AirplaneTwoColumns.column for i in range(self.rows)]
        self.count_of_buyers = 0
        self.count_of_tickets = 0
        self.request = 0
        self.count_of_passengers_without_places = 0

    def __str__(self):
        return str(self)

    def empty_places(self):
        return sum([len(list(filter(lambda x: x == '.', a))) for a in self.total_seats])

    def right_input(self, count, side, place):
        if type(count) == int and count in [0, 1, 2, 3] and side in ['left', 'right'] and place in ['aisle', 'window']:
            return True
        else:
            return False

    def seating(self):
        print(f'''
        Just tell us how many seats you need to book, on which side, and also closer to the aisle or to the window?
        The input format should be: "number of places" left(or right) aisle(or window). For example: 2 left aisle.
        0 - Exit
        ''')
        input_tickets = input('>>> : ')
        if input_tickets == '0':
            print(f'{str(self.count_of_tickets)} tickets were purchased for {self.request} requests')
            print('Have a great day!')
            exit()

        if len(input_tickets.split()) == 3:
            count, side, place = input_tickets.split()
            count = int(count)

            if self.right_input(count, side, place):
                self.request += 1
                print(f'Request №{self.request}: places - {count}, side - {side}, preference - {place}')
                counter = 0
                for ind, air in enumerate(self.total_seats):
                    if side == 'left':
                        if place == 'aisle':
                            d = air[3 - count: 3]
                            if d == '.' * count:
                                air = air[:3 - count] + 'V' * count + air[3:]
                                a = [str(ind + 1) + str(chr(m + 64 + 1)) for m, n in enumerate(air[0:3]) if n == 'V']
                                air = air[:3 - count] + 'X' * count + air[3:]
                                self.total_seats[ind] = air
                                st = ' '.join(a)
                                print(f'Passengers can take seats: {st}')
                                self.count_of_tickets += count
                                return self.total_seats, self.count_of_tickets, self.request, self.count_of_passengers_without_places

                            counter += 1
                            if counter == len(self.total_seats):
                                print('Cannot fulfill passengers requirements')
                                self.count_of_passengers_without_places += count
                                return self.total_seats, self.count_of_tickets, self.request, self.count_of_passengers_without_places

                        if place == 'window':
                            d = air[: count]
                            if d == '.' * count:
                                air = 'V' * count + air[count:3] + air[3:]
                                a = [str(ind + 1) + str(chr(m + 64 + 1)) for m, n in enumerate(air[0:3]) if n == 'V']
                                air = 'X' * count + air[count:3] + air[3:]
                                self.total_seats[ind] = air
                                st = ' '.join(a)
                                print(f'Passengers can take seats: {st}')
                                self.count_of_tickets += count
                                return self.total_seats, self.count_of_tickets, self.request, self.count_of_passengers_without_places

                            counter += 1
                            if counter == len(self.total_seats):
                                print('Cannot fulfill passengers requirements')
                                self.count_of_passengers_without_places += count
                                return self.total_seats, self.count_of_tickets, self.request, self.count_of_passengers_without_places

                    if side == 'right':
                        if place == 'aisle':
                            d = air[3: 3 + count]
                            if d == '.' * count:
                                air = air[:3] + 'V' * count + air[3 + count:]
                                a = [str(ind + 1) + str(chr(m + 64 + 4)) for m, n in enumerate(air[3:]) if n == 'V']
                                air = air[:3] + 'X' * count + air[3 + count:]
                                self.total_seats[ind] = air
                                st = ' '.join(a)
                                print(f'Passengers can take seats: {st}')
                                self.count_of_tickets += count
                                return self.total_seats, self.count_of_tickets, self.request, self.count_of_passengers_without_places

                            counter += 1
                            if counter == len(self.total_seats):
                                print('Cannot fulfill passengers requirements')
                                self.count_of_passengers_without_places += count
                                return self.total_seats, self.count_of_tickets, self.request, self.count_of_passengers_without_places

                        if place == 'window':
                            d = air[-count:]
                            if d == '.' * count:
                                air = air[:3] + air[3: -count] + 'V' * count
                                a = [str(ind + 1) + str(chr(m + 64 + 4)) for m, n in enumerate(air[3:]) if n == 'V']
                                air = air[:3] + air[3: -count] + 'X' * count
                                self.total_seats[ind] = air
                                st = ' '.join(a)
                                print(f'Passengers can take seats: {st}')
                                self.count_of_tickets += count
                                return self.total_seats, self.count_of_tickets, self.request, self.count_of_passengers_without_places

                            counter += 1
                            if counter == len(self.total_seats):
                                print('Cannot fulfill passengers requirements')
                                self.count_of_passengers_without_places += count
                                return self.total_seats, self.count_of_tickets, self.request, self.count_of_passengers_without_places
            else:
                self.seating()
        else:
            self.seating()

def main():
    airplane = AirplaneTwoColumns()
    choice = None
    print('Welcome!')
    while choice != '0':
        print \
            (f'''
            Empty places: {airplane.empty_places()} 
            0 - Exit
            1 - Order a ticket
            ''')
        choice = input('>>> : ')
        print()
        if choice == '0':
            print(f'{str(airplane.count_of_tickets)} tickets were purchased for {airplane.request} requests')
            print('Have a great day!')
        elif choice == '1':
            airplane.seating()
            print('Please look at the plan of the airplane after ordering tickets:')
            [print(i[:3], '_', i[3:]) for i in airplane.total_seats]
        else:
            print('Please try again.')


main()
