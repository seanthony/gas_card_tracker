from datetime import datetime
from os import system as sys

CARD_VALUE = 25
MILES_TO_CARD = 10 * CARD_VALUE


def valid_date(date):
    return len(date) == 5 and date[2] == '/' and (date[:2] + date[3:]).isdigit() and int(date[:2]) > 0 and int(date[:2]) <= 12 and int(date[3:]) > 0 and int(date[3:]) <= 31


def get_date():
    print("enter the date in the format mm/dd (or q to quit)")
    while True:
        date = input('>>> ').strip()
        if date == 'q':
            exit()
        elif valid_date(date):
            return date
        print('invalid!')


def get_miles():
    print("enter the round trip miles for the date (or q to quit)")
    while True:
        miles = input('>>> ').strip()
        if miles == 'q':
            exit()
        elif miles.isdigit():
            return int(miles)


def calc_mileage(filename):
    with open(filename, 'r') as file:
        file.readline()
        lines = file.readlines()
    if lines:
        miles = lines[-1].split(',')[-1].strip()
        if miles.isdigit():
            return int(miles)
    return 0


def append_line_to_file(filename, new_line):
    with open(filename, 'a') as file:
        file.write(new_line)


def check_redeem_info():
    print('redeem gas card? [y/n]')
    while True:
        choice = input('>>> ').strip().lower()
        if choice == 'y':
            return True
        elif choice == 'n':
            return False
        else:
            print('invalid!')


def make_payment_line(gas_cards_due, new_total):
    payment = gas_cards_due * CARD_VALUE
    new_mileage = new_total - (gas_cards_due * MILES_TO_CARD)
    date = datetime.now().strftime('%m/%d')
    return '{}, paid ${}, {}\n'.format(date, payment, new_mileage)


def update_mileage_tracker(filename, payment_line):
    with open(filename, 'a') as file:
        file.write(payment_line)


def main():
    sys('clear')
    filename = 'mileage_tracker.txt'
    print('welcome to the mileage tracker')
    date = get_date()
    miles = get_miles()
    current_total = calc_mileage(filename)
    new_total = miles + current_total

    new_line = '{}, {}, {}\n'.format(date, miles, new_total)
    append_line_to_file(filename, new_line)

    gas_cards_due = new_total // MILES_TO_CARD
    if gas_cards_due > 0:
        print('you are eligible for {} gas cards.'.format(gas_cards_due))
        if check_redeem_info():
            payment_line = make_payment_line(gas_cards_due, new_total)
            update_mileage_tracker(filename, payment_line)
            print('mileage tracker updated')
        else:
            print('thank you have a nice day!')
    else:
        print('you have {} miles until your next card'.format(
            MILES_TO_CARD - new_total))


if __name__ == "__main__":
    main()
