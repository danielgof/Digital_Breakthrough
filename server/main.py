from flask import Flask, jsonify, make_response, request, abort
from flask_login import LoginManager, login_user, login_required, current_user, login_fresh
from flask_login.utils import logout_user
from werkzeug.security import check_password_hash, generate_password_hash
import datetime

from RedisLogin import RedisLogin
from authentication import User

RL = RedisLogin()

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
	return jsonify({ "res" : "User Logout!" })


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
			"level" 			: 0 
		})

	return make_response(jsonify({ "message" : "User Registered!" }), 201)


if __name__ == "__main__":
    app.run(port = 3444, debug = True)