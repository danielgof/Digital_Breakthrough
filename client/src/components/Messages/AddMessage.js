import React, { useState } from 'react'
import cs from "./Messages.module.css"
import { ServerAPI_POST } from '../../libs/ServerAPI'

const UserAddMessage = () => {
	const [address, setAddress] = useState("")
	const [text, setText] = useState("")
	const [message, setMessage] = useState(undefined)

	const handleSubmit = (e) => {
		e.preventDefault()

		ServerAPI_POST({
			url : "/messages",
			sendObj : {
				address : address,
				text : text
			},
			handleStatus: (res) => {
				if (res.status === 422) {
					setMessage(res.data.message)
				}
				else if (res.isOk) {
					setMessage(res.data.message)
					setAddress("")
					setText("")
				}
				else {
					setMessage("Ошибка сервера, повторите позже!")
				}
			}
		})
	}

	return (
		<div className={cs.form} >
			<h1> Создание запроса </h1>
			{ message && <h3 className="mt-3"> {message} </h3> }
			<form onSubmit={handleSubmit} className="g-3 mt-3">
				<div className="mb-3">
					<label htmlFor="address"	className="form-label"> Адрес </label>
					<input type="text" 			className="form-control" id="address" 	value={address} 	onChange={(e) => { setAddress(e.target.value) }} 	required />
				</div>
				<div className="mb-3">
					<label htmlFor="text"		className="form-label"> Текст запроса </label>
					<textarea		className="form-control" id="text" 		value={text} 		onChange={(e) => { setText(e.target.value) }} 		required />
				</div>
				<input type="submit" className="btn btn-primary" value="Отправить" />
			</form>
		</div>
	)
}

export default UserAddMessage
