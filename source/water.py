import math

DAYS_IN_A_MONTH = 30

class Water:

    def water_used(accomadation, water_quota):
        water_allotted_a_month = (accomadation * water_quota) * DAYS_IN_A_MONTH
        return water_allotted_a_month

    def water_cost(water_used, cost):
        total_cost = float(water_used) * float(cost)
        return math.ceil(total_cost)
