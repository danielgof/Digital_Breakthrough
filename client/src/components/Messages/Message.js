import React, { useEffect, useState } from 'react'
import { Navigate, useNavigate, useParams } from 'react-router';
import { ServerAPI_GET, ServerAPI_PATCH } from '../../libs/ServerAPI';
import getClassName from '../../libs/GetCSS'
import Map from '../Map';

const Message = () => {
	const { id }				= useParams();
	const navigate				= useNavigate();
	const [message, setMessage] = useState();
	const [resp, setResp]		= useState(undefined)

	useEffect(() => {
		ServerAPI_GET({
			url : `/messages/${id}`,
			onDataReceived : (data) => {
				if (data.message.comment === null)
					data.message.comment = ""
				setMessage(data.message)
				console.log(data.message)
			}
		})
	}, [])
	
	const handleClickEdit = () => {
		ServerAPI_PATCH({
			url : "/messages",
			sendObj: {
				id : message.id,
				comment : message.comment,
				state : message.state
			},
			handleStatus: (res) => {
				if (res.isOk) {
					setResp(res.data.message)
					navigate(-1)
				}
				else {
					setResp("Ошибка сервера, попробуйте позже!")
				}
			}
		})
	}

	const handleClickBack = () => {
		navigate(-1)
	}

	return (
		<div>
			{
				(message === undefined) ? (
					<p> Loading... </p>
				) : (
					<div>
						<h3> Номер запроса: {message.id} </h3>
						<h6> Пользователь: </h6>
						<p> {message.email} </p>
						
						<h6> Адрес: </h6>
						<p> {message.address} </p>

						<h6> Дата составления: </h6>
						<p> {message.date} </p>
						<h6> Текст запроса: </h6> 
						<p> {message.message} </p>
						<Map />
						<div className="mb-3">
							<label htmlFor="comment" className="form-label"> Комментарий </label>
							<textarea className="form-control" id="comment" value={message.comment} onChange={(e) => { setMessage({...message, comment : e.target.value}) }} />
						</div>
						<div className="mb-4">
							<h5> Установить стадию проведения </h5>
							<input type="button" className={getClassName(["btn mx-3", message.state === 0 ? "btn-secondary" : "btn-outline-secondary"])} 	value="Не Обработан" 	onClick={() => { setMessage({...message, state : 0}) }} />
							<input type="button" className={getClassName(["btn mx-3", message.state === 1 ? "btn-info" 		: "btn-outline-info"])}			value="В процессе" 		onClick={() => { setMessage({...message, state : 1}) }} />
							<input type="button" className={getClassName(["btn mx-3", message.state === 2 ? "btn-success" 	: "btn-outline-success"])}		value="Обработан" 		onClick={() => { setMessage({...message, state : 2}) }} />
							<input type="button" className={getClassName(["btn mx-3", message.state === 3 ? "btn-danger" 	: "btn-outline-danger"])}		value="Отклонен" 		onClick={() => { setMessage({...message, state : 3}) }} />
						</div>
						{ resp && <h3> {resp} </h3> }
						<div className="mb-5 mt-3">
							<input type="button" className="btn btn-dark mx-2" value="Изменить" 					onClick={handleClickEdit} />
							<input type="button" className="btn btn-dark mx-2" value="Назад(Выйти без изменений)" 	onClick={handleClickBack}/>
						</div>
					</div>
				)
			}
		</div>
	)
}

export default Message
