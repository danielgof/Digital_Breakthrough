import React, { useEffect, useState } from 'react'
import { ServerAPI_GET } from '../../libs/ServerAPI';

const MyMessages = () => {
	const [messages, setMessages] = useState();
	const messageStateText = ["Ожидает обработки", "В обработке", "Обработана", "Отклонена"]

	useEffect(() => {
		ServerAPI_GET({
			url : "/messages",
			onDataReceived : (data) => {
				setMessages(data.messages)
				console.log(data.messages)
			}
		})
	}, [])

	return (
		<div>
			{
				(messages === undefined) ? (
					<p> Loading... </p>
				) : (
					<div>
						<table className="table table-dark table-striped">
							<thead>
								<tr>
									<th> Дата  			</th>
									<th> Запрос 		</th>
									<th> Статус			</th>
									<th> Коментарий		</th>
								</tr>
							</thead>
							<tbody>
								{
									messages.map(message => (
										<tr key={message.id}>
											<td> {message.date} 					</td>
											<td> {message.message} 					</td>
											<td> {messageStateText[message.state]} 	</td>
											<td> {message.comment} 					</td>
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

export default MyMessages
