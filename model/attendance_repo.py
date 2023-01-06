from model.attendance_dao import get_all_attendance_dao, get_attendance_dao
from utils.diff_datetime import calc_shift_time
from utils.format_attendance import format_all


def get_attendance_repo(emp_code:str, date):
	rows = get_attendance_dao(emp_code, date)
	delta_time = calc_shift_time(rows)

	attend = True if delta_time else False

	return {"attended": attend, "duration": delta_time}


def get_all_attendance(emp_code:str):
	rows = get_all_attendance_dao(emp_code)
	return format_all(rows)