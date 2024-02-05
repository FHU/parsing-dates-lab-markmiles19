#parse month should take in the text of the month and return the number 
#as a string
#January -> 1 (as a string)
#YOU MAY USE THIS FUNCTION IF YOU WANT TO OR YOU MAY REMOVE IT
def parse_month(month):
    month_dict = {
        'January': '01',
        'February': '02',
        'March': '03',
        'April': '04',
        'May': '05',
        'June': '06',
        'July': '07',
        'August': '08',
        'September': '09',
        'October': '10',
        'November': '11',
        'December': '12'
    }

#REMOVE PASS AND FIX THIS FUNCTION
#parse_date function should return the date formatted as MM/DD/YYYY
#DO NOT REMOVE THIS FUNCTION
def parse_date(user_string):
    date = parse_date.replace(',', '').split()

#REMOVE PASS AND YOUR CODE GOES HERE
if __name__ == '__main__':
    user_input = input()
    parse_date(user_input)