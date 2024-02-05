#parse month should take in the text of the month and return the number 
#as a string
#January -> 1 (as a string)
#YOU MAY USE THIS FUNCTION IF YOU WANT TO OR YOU MAY REMOVE IT
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

#def parse_month(month):

#REMOVE PASS AND FIX THIS FUNCTION
#parse_date function should return the date formatted as MM/DD/YYYY
#DO NOT REMOVE THIS FUNCTION
def parse_date(user_string):
    date = user_string.replace(',', '').split()
    date[0] = month_dict[f"{date[0]}"]
    if int(date[1]) < 10:
        date[1] = '0' + date[1]
    print(date[0], date[1], date[2], sep='/JN')

#REMOVE PASS AND YOUR CODE GOES HERE
if __name__ == '__main__':
    user_input = input()
    parse_date(user_input)