BEDROOMS = {"2": 3,
            "3": 5}

class Allot:

    def categorize(self, split_input):
        if 'ADD_GUESTS' in split_input:
            category = 'ADDITIONAL'
            accomadation = split_input[1]
            water_ratio = None
        else:
            category = 'GUEST'
            accomadation = BEDROOMS.get(split_input[1])
            water_ratio = split_input[2]
        return category, accomadation, water_ratio
    
    def allotment(self, data, apartment):
        split_input = data.split(' ')
        category, accomadation, water_ratio = self.categorize(split_input)
        apartment.book(accomadation, True, category, water_ratio)
