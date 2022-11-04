from source.water import Water
from source.calculations import get_ratio_of_number, income_tax_calculation

CORPORATION_COST = 1
BOREWELL_COST = 1.5

tanker_water = [(2,500), (3,1000), (5,1500), (8, 3000)]

class Apartment:

    def __init__(self):
        self.accomadation = 0
        self.guests = 0
        self.monthly_water_quota = 10 #Litres
        self.water_ratio = None
        self.duration = 30 #Days
        self.booked = False

    def book(self, accomadation, booking_status, category, water_ratio):
        if category == 'GUEST' and self.booked is False and self.water_ratio is None:
            self.accomadation = accomadation
            self.water_ratio = water_ratio
            self.booked = booking_status
        elif category == 'ADDITIONAL':
            self.guests += int(accomadation)

    def bills(self):
        water_usage_guests = Water.water_used(self.accomadation, self.monthly_water_quota)
        water_usage_additional = Water.water_used(self.guests, self.monthly_water_quota)
        corporation_water, borewell_water = get_ratio_of_number(water_usage_guests, self.water_ratio)
        corporation_cost = Water.water_cost(corporation_water, CORPORATION_COST)
        borewell_cost = Water.water_cost(borewell_water, BOREWELL_COST)
        total_bill = income_tax_calculation(water_usage_additional, tanker_water)
        print(water_usage_guests + water_usage_additional, total_bill + corporation_cost + borewell_cost)
