from pytz import timezone
from datetime import datetime

# “days”: [
# “date”: “2020-04-03”
# “actions”: [
# { “action”: “CheckOut”, “time”: “2020-04-01T10:05:00.000000+00:00” }
# ]
# ]
#list of dict where each dict has days as keys

def format_all(rows):
	days = []
	# day = rows[0][0]
	current_day = {"date": rows[0][0], "actions": []}
	for i, r in enumerate(rows):

		if r[0] != current_day["date"]: 
			days.append(current_day) 
			current_day = {"date": r[0], "actions": []}
	
		action = {"action":r[2], "time":convert_to_utc(r[1])}
		current_day["actions"].append(action)
	days.append(current_day)
	return days



def convert_to_utc(date:str):
	local = datetime.strptime(date, '%Y-%m-%d %I:%M %p') 
	utc_zone = timezone('UTC') 
	utc = utc_zone.localize(local) 
	return str(utc)
