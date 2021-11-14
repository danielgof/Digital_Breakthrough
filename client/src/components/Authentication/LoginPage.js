import React, { useState } from 'react'
import { Link, useNavigate  } from "react-router-dom";
import { loadUserInfo } from '../../contexts/LoginContext'
import { ServerAPI_POST } from '../../libs/ServerAPI'
import getClassName from "../../libs/GetCSS"
import cs from './Auth.module.css'

const LoginPage = () => {
	const navigate 						= useNavigate();
	const [email, 		setEmail] 		= useState("");
	const [password, 	setPassword] 	= useState("");
	const [message, 	setMessage] 	= useState(undefined)

	const handleSubmit = (e) => {
		e.preventDefault()
		ServerAPI_POST({
			url : "/login",
			sendObj : {
				email : email,
				password : password,
			},
			handleStatus : (res) => {
				if (res.status === 422)
				{
					console.log("Status", res.status)
					setMessage(res.data.message)
				}
				else if (res.isOk)
				{
					loadUserInfo()
					navigate("/profile")
				}
			}
		})
	}

	return (
		<div className={getClassName([cs.form, "mt-5"])} >
			{ message && <h3> {message} </h3> }
			<form onSubmit={handleSubmit} className="g-3">
				<div className="mb-3">
					<label htmlFor="email" 		className="form-label"> Email address </label>
					<input type="email" 		className="form-control" id="email" 	required value={email} 		onChange={(e) => { setEmail(e.target.value) }} />
				</div>
				<div className="mb-3">
					<label htmlFor="password" 	className="form-label"> Password </label>
					<input type="password" 		className="form-control" id="password" required value={password} 	onChange={(e) => { setPassword(e.target.value) }} />
				</div>
				<div className="mb-3">
					<Link to="/register"> Нет аккаунта? Зарегистрируйтесь! </Link>
				</div>
				<input type="submit" className="btn btn-primary" value="Login" />
			</form>
		</div>
	)
}

export default LoginPage
