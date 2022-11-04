import sys
from source.allot import Allot
from source.apartment import Apartment

allot = Allot()
apartment = Apartment()

def main():
    input_file = sys.argv[1]
    with open(input_file, 'r') as file:
        data = file.read().split('\n')
    for input in data:
        if input.startswith('ALLOT_WATER'):
            allot.allotment(input, apartment)
        elif input.startswith('ADD_GUESTS'):
            allot.allotment(input, apartment)
        elif input.startswith('BILL'):
            apartment.bills()

if __name__ == "__main__":
    main()