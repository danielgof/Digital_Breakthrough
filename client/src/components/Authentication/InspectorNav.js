import React from 'react'
import { Link } from 'react-router-dom'

const InspectorNav = () => {
	return (
		<div>
			<div>
				<Link to=""> Новые запросы </Link>
			</div>	
			<div>
				<Link to=""> Запросы в обработке </Link>
			</div>	
			<div>
				<Link to=""> Завершенные запросы </Link>
			</div>	
		</div>
	)
}

export default InspectorNav
