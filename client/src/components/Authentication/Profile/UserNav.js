import React from 'react'
import { Link } from 'react-router-dom'

const UserNav = () => {
	return (
		<div className="mb-1">
			<Link to="mymessages"> Мои запросы </Link>
		</div>
	)
}

export default UserNav
