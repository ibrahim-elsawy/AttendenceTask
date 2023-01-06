from datetime import datetime, timedelta
from functools import reduce

def calc_shift_time(rows):
	n = len(rows)
	total_diff = []
	if n==0:
		return 0
	if n % 2 != 0:
		# add false row to make the rows even then handle conversion in calc_hours
		rows.append( (0, 0) )
		n += 1
	
	# case when employee has a shift from night and came early before 12 am of this day so there's no checkin in that day 
	if rows[0][1] == 'CheckOut':
		rows = [(0,0)]+rows

	for i in range(0, n, 2):
		total_diff.append(calc_hours(rows[i][0], rows[i+1][0]))

	return str(reduce(lambda x,y : x+y, total_diff))


def calc_hours(checkin, checkout):

	if checkin ==0:
		cout = datetime.strptime(checkout, '%Y-%m-%d %I:%M %p')
		return timedelta(hours=cout.hour,minutes=cout.minute)

	cin = datetime.strptime(checkin, '%Y-%m-%d %I:%M %p')
	if checkout == 0: 
		cout = datetime(cin.year, cin.month, cin.day+1)
	else: 
		cout = datetime.strptime(checkout, '%Y-%m-%d %I:%M %p')
	return cout-cin