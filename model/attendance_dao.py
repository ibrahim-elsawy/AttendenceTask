import sqlite3
from configparser import ConfigParser
from contextlib import closing


config = ConfigParser()
config.read('config.ini')
db_path = config['DB']['dir']



def get_attendance_dao(emp_code:str, date):
	with closing(sqlite3.connect(db_path)) as connection:
		with closing(connection.cursor()) as cursor: 
			rows = cursor.execute("SELECT ActionTime, Action FROM Attendance A\
				INNER JOIN AttendanceActions AK ON A.Id=AK.AttendanceId\
				WHERE A.employee=? AND A.day=?;",(emp_code,date,),).fetchall();
	
	return rows;


def get_all_attendance_dao(emp_code:str):
	with closing(sqlite3.connect(db_path)) as connection:
		with closing(connection.cursor()) as cursor: 
			rows = cursor.execute("SELECT day, ActionTime, Action FROM Attendance A\
						INNER JOIN AttendanceActions AK ON A.Id=AK.AttendanceId\
						WHERE A.employee=?\
						GROUP BY AK.Action, A.day ORDER BY A.day;",(emp_code,),).fetchall();

	return rows;