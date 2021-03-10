# 3. Leap Year
#    a. I/P -> Year, ensure it is a 4 digit number.
#    b. Logic -> Determine if it is a Leap Year.
#    c. O/P -> Print the year is a Leap Year or not.

# Check weather a year is leap year or not
def is_leap_year(year_):
    if year_ % 4 == 0:
        if year_ % 100 == 0:
            if year_ % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


if __name__ == '__main__':
    try:
        year = input('Enter a year : ')
        # Check the year is valid or not
        if len(year) == 4:
            if is_leap_year(int(year)):
                print(year, ' is a Leap Year')
            else:
                print(year, ' is not a leap year')
        else:
            print('Please enter a valid year!')
    except Exception as e:
        print(e)
