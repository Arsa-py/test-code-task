from datetime import datetime


print('#'*30)
print('Welcome to Get Commission App')
print('#'*30)
print()


def get_commission(date_str):
    dt = str(input(date_str))
    high_season = range(6, 10, 1)
    xmas_season_dec = 12
    xmas_season_jan = 1
    try:
        # date object
        date_obj = datetime.strptime(dt, '%Y-%m-%d').date()
        mnth = date_obj.month
        print(f'The date you have entered is: {date_obj}')
        # checking if the month belongs to the high season
        if mnth in high_season:
            print(f'The GuestReady commission for {date_obj} is 15%')
            return 0.15
        elif mnth is xmas_season_dec:
            print(f'The GuestReady commission for {date_obj} is 12%')
            return 0.12
        elif mnth is xmas_season_jan:
            print(f'The GuestReady commission for {date_obj} is 13%')
            return 0.13
        else:
            print(f'The GuestReady commission for {date_obj} is 10%')
            return 0.10
    except ValueError as e:
        print(str(e))
        get_commission('Please check your input! Enter the date in YYY-MM-DD format: ')
        return 0

if __name__ == '__main__':
    get_commission("Please enter a date in 'YYYY-MM-DD' format: ")