import React, { useEffect, useState } from 'react'
import { useNavigate } from 'react-router';
import { ServerAPI_GET } from '../../libs/ServerAPI';
import cs from './Messages.module.css'

const Messages = ({title, url}) => {
	const navigate = useNavigate()
	const [messages, setMessages] = useState();

	useEffect(() => {
		ServerAPI_GET({
			url : url,
			onDataReceived : (data) => {
				setMessages(data.messages)
				console.log(data.messages)
			}
		})
	}, [])

	const handleRowClick = (id) => {
		navigate(`../messages/${id}`)
	}

	return (
		<div>
			<h1 className="mb-4"> {title} </h1>
			{
				(messages === undefined) ? (
					<p> Loading... </p>
				) : (
					<div>
						<table className="table table-dark table-striped table-hover">
							<thead>
								<tr>
									<th> Пользователь	</th>
									<th> Дата  			</th>
									<th> Запрос 		</th>
									<th> Коментарий		</th>
								</tr>
							</thead>
							<tbody>
								{
									messages.map(message => (
										<tr key={message.id} className={cs.trSelect} onClick={() => {handleRowClick(message.id)}}>
											<td> {message.email} 	</td>
											<td> {message.date} 	</td>
											<td> {message.message} 	</td>
											<td> {message.comment} 	</td>
										</tr>
									))
								}
							</tbody>
						</table>
					</div>
				)
			}
		</div>
	)
}

export default Messages
