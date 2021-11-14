import React, { useContext } from 'react'
import { Link, useNavigate } from 'react-router-dom'
import { loadUserInfo, LoginContext } from '../../../contexts/LoginContext'
import { ServerAPI_POST } from '../../../libs/ServerAPI'
import InspNav from './InspNav'
import UserNav from './UserNav'

const ProfileNav = () => {
	const navigate 		= useNavigate();
	const loginContext 	= useContext(LoginContext)	

	const handeleLogout = () => {
		ServerAPI_POST({ 
			url:"/logout",
			handleStatus: (res) => {
				if (res.isOk)
				{
					loadUserInfo()
					navigate("/")
				}
			}
		})
	}

	return (
		<div>
			<div className="mb-1">
				<Link to="/profile"> Профиль </Link>
			</div>
			{
				loginContext.level === "1" ? (
					<InspNav />
				) : (
					<UserNav />
				)
			}
			<div className="mb-1">
				<Link to="addmessage"> Создать запрос </Link>
			</div>
			<div className="mt-3">
				<input type="button" className="btn btn-dark" value="Logout" onClick={handeleLogout} />
			</div>
		</div>
	)
}

export default ProfileNav
