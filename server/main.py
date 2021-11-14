from flask import Flask, jsonify, make_response, request, abort
from flask_login import LoginManager, login_user, login_required, current_user, login_fresh
from flask_login.utils import logout_user
from werkzeug.security import check_password_hash, generate_password_hash
import datetime

from RedisLogin import RedisLogin
from authentication import User
from DBlib import DataBase

f = open('local.config', 'r')
isDocker = f.read(1) == "1"
redishost = "localhost"
if isDocker:
	redishost = "redis"
print(redishost)

DB = DataBase("lanhelen.asuscomm.com", "daniel", "Daniel123!", "chel_bd")
RL = RedisLogin(host=redishost)

app = Flask(__name__)
app.secret_key = "my super duper puper secret key!"


login_manager = LoginManager(app)
@login_manager.user_loader
def load_user(user_id):
	return User().FromDB(user_id, RL)
	

@app.route("/login", methods=["POST"])
def login():
	if not request.json:
		abort(400)
	
	email 		= request.json.get("email")
	password	= request.json.get("password")
	
	if email and password:
		user = User().FromDB(email, RL)
		if user.IsExists():
			if check_password_hash(user.GetPassword(), password):
				cookieDuration = datetime.timedelta(seconds = 10)
				login_user(user, remember=True, duration=cookieDuration)
				return jsonify({ "isAuth" : True })

	return make_response(jsonify({ "message" : "Wrong email or password!" }), 422)


@app.route("/islogin", methods=["GET"])
def islogin():
	return jsonify({ "isAuth" : current_user.get_id() != None })


@app.route("/profileinfo", methods=["GET"])
def porfileInfo():
	curr_id = current_user.get_id()
	if curr_id != None:
		user = User().FromDB(curr_id, RL)
		if user.IsExists():
			return jsonify({ 
				"isAuth" : True, 
				"email" : user.GetEmail(), 
				"name" : user.GetName(), 
				"registration_date" : user.GetRegDate(),
				"level" : user.GetLevel()  
			})

	return jsonify({ "isAuth" : False })


@app.route("/logout", methods=["POST"])
@login_required
def logout():
	logout_user()
	return jsonify({ "message" : "User Logout!" })


@app.route("/register", methods=["POST"])
def register():
	if not request.json:
		abort(400)

	email = 	request.json.get("email")
	password1 = request.json.get("password1")
	password2 = request.json.get("password2")
	name = 		request.json.get("name", "")

	if not (email or password1 or password2):
		print("test1")
		return (make_response(jsonify({ "message" : "Please, fill all fields" }), 422))
	elif password1 != password2:
		print("test2")
		return (make_response(jsonify({ "message" : "Passwords are not equal" }), 422))
	else:
		hashPwd = generate_password_hash(password1)
		print(str(datetime.datetime.now().date()))
		RL.AddUser(email, {
			"password"			: hashPwd,
			"name"				: name, 
			"registration_date" : str(datetime.datetime.now().date()),
			"level" 			: 1 if email == "insp@mail.ru" else 0
		})

	return make_response(jsonify({ "message" : "User Registered!" }), 201)


@app.route("/messages", methods=["GET"])
@login_required
def get_messages():
	email = current_user.GetEmail()
	messages = DB.GetTableJson("messages", where=f"email='{email}'")
	
	return jsonify({ "messages" : messages })


@app.route("/messages", methods=["POST"])
@login_required
def post_message():
	if not request.json:
		abort(400)

	email 	= current_user.GetEmail()
	address = request.json.get("address")
	message	= request.json.get("text")

	if not (address or message):
		return make_response(jsonify({ "message" : "Fill all fields!" }), 422)
	
	DB.AddTableElement("messages", {
		"email" : email,
		"address" : address,
		"state" : 0,
		"message" : message,
		"date" : str(datetime.datetime.now().date())
	})

	return jsonify({ "message" : "Запрос отправлен!" })

@app.route("/messages", methods=["PATCH"])
@login_required
def patch_message():
	if not request.json:
		abort(400)

	id = request.json.get("id")
	comment = request.json.get("comment")
	state	= request.json.get("state")

	if not id:
		make_response(jsonify({ "message" : "No message id!" }), 400)

	if not comment and not state:
		make_response(jsonify({ "message" : "No fields to change!" }), 400)
	
	data = {}
	if comment != None:
		data.update({ "comment" : comment })
	if state != None:
		state = max(min(state, 3), 0)
		data.update({ "state" : state })

	DB.UpdateTableElement("messages", data, f"id='{id}'")

	return jsonify({ "message" : "Запрос отправлен!" })


@app.route("/messages/new", methods=["GET"])
@login_required
def get_messagesNew():
	if not current_user.IsInspector():
		return make_response(jsonify({ "message" : "Forbidden!" }), 403)

	messages = DB.GetTableJson("messages", where="state='0'")
	
	return jsonify({ "messages" : messages })


@app.route("/messages/proc", methods=["GET"])
@login_required
def get_messagesProc():
	if not current_user.IsInspector():
		return make_response(jsonify({ "message" : "Forbidden!" }), 403)

	messages = DB.GetTableJson("messages", where="state='1'")
	
	return jsonify({ "messages" : messages })


@app.route("/messages/end", methods=["GET"])
@login_required
def get_messagesEnd():
	if not current_user.IsInspector():
		return make_response(jsonify({ "message" : "Forbidden!" }), 403)

	messages = DB.GetTableJson("messages", where="state>'1'")
	
	return jsonify({ "messages" : messages })


@app.route("/messages/<id>", methods=["GET"])
@login_required
def get_message(id):
	if not current_user.IsInspector():
		return make_response(jsonify({ "message" : "Forbidden!" }), 403)

	messages = DB.GetTableJson("messages", where=f"id='{id}'")

	if len(messages) == 0:
		return make_response(jsonify({ "message" : "Can't find message!" }), 404)
	
	return jsonify({ "message" : messages[0] })


@app.route("/find", methods=["POST"])
@login_required
def find():
	if not request.json:
		abort(400)

	if not current_user.IsInspector():
		return make_response(jsonify({ "message" : "Forbidden!" }), 403)

	markers = request.json.get("markers")

	if not markers:
		return make_response(jsonify({ "message" : "Нет точки отсчета!" }), 422)

	if len(markers) == 0:
		return make_response(jsonify({ "message" : "Нет точки отсчета!" }), 422)
		
	print(markers)
	
	badGuys = [{"name" : "name bla1", "address" : "test address 1"}, {"name" : "test name two",  "address" : "some long address here!!!"}]

	return jsonify({ "badGuys" : badGuys })


if __name__ == "__main__":
    app.run(port = 3444, debug = True)