import React from 'react'
import Messages from './Messages';

const NewMessages = () => {
	return (
		<div>
			<Messages title="Эти запросы ожидают обработки" url="/messages/new" />
		</div>
	)
}

export default NewMessages
