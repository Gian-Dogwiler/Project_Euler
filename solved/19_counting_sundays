months = {'january': 31, 'february': 28, 'march': 31, 'april': 30, 'may': 31, 'june': 30, 'july': 31, 'august': 31, 'september': 30, 'october': 31, 'november': 30, 'december': 31}
days = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
months_ordered = ['january','february','march','april','may','june','july','august','september','october','november','december']
starting_year = 1901
end_year = 2001
current_month = 'january'
current_day = 'monday'
num_sundays = 0
current_day_index = 0

def checkLeapYear(year: int):
    if (year % 4 == 0):
        return True
    else:
        return False

def getNumberOfDays(current_month: str, current_year: int):
    if checkLeapYear(current_year) and current_month == 'february':
        return 29
    else:
        return months[current_month]

while starting_year != end_year:

    num_days = getNumberOfDays(current_month, starting_year)
    rest_days = num_days - (7-current_day_index)
    rest_days = rest_days % 7
    current_day = days[rest_days-1]
    print(current_day)
    
    # calculate next month
    current_month_index = months_ordered.index(current_month)
    if current_month_index == 11:
        # switch to next year
        starting_year += 1
        current_month = 'january'
        current_day_index = days.index(current_day)
        current_day = days[current_day_index]
        if current_day == 'sunday':
            num_sundays += 1
            print(str(starting_year) + str(current_month))
    else:
        current_month = months_ordered[current_month_index + 1]
        current_day_index = days.index(current_day)
        current_day = days[current_day_index]
        if current_day == 'sunday':
            num_sundays += 1
            print(str(starting_year) + str(current_month))

print(num_sundays)