from flask import Flask, jsonify, request, Response

from model.attendance_repo import get_all_attendance, get_attendance_repo

app = Flask(__name__)


@app.route('/api/check', methods=['GET'])
def get_attendance(): 
	try:
		req = request.get_json() 
		if len(req['emp_code'])==0 or len(req['date'])==0:
			return Response("Enter valid format...", status=400)
		data = get_attendance_repo(req['emp_code'], req['date'])
		return jsonify(data)
	except:
		return Response(status=400)



@app.route('/api/history', methods=['GET'])
def get_history(): 
	try:
		req = request.get_json() 
		if len(req['emp_code'])==0:
			return Response("please enter valid emp_code...", status=400)
		data = get_all_attendance(req['emp_code'])
		return jsonify({"days":data})
	except:
		return Response(status=400)

# waitress-serve waitress_server:app
if __name__ == '__main__': 
	app.run(port=5000)
