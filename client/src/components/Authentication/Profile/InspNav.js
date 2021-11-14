import React from 'react'
import { Link } from 'react-router-dom'

const InspNav = () => {
	return (
		<div>
			<div className="mb-1">
				<Link to="newmessages"> Новые запросы </Link>
			</div>	
			<div className="mb-1">
				<Link to="procmessages"> Запросы в обработке </Link>
			</div>	
			<div className="mb-1">
				<Link to="endmessages"> Завершенные запросы </Link>
			</div>	
		</div>
	)
}

export default InspNav
