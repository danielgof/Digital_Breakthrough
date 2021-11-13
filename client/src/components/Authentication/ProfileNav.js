import React, { useContext } from 'react'
import { Link, useNavigate } from 'react-router-dom'
import { loadUserInfo, LoginContext } from '../../contexts/LoginContext'
import { ServerAPI_POST } from '../../libs/ServerAPI'
import InspectorNav from './InspectorNav'
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
			<div>
				<Link to=""> Профиль </Link>
			</div>
			{
				loginContext.level === 0 ? (
					<UserNav />
				) : (
					<InspectorNav />
				)
			}
			<div>
				<input type="button" className="btn btn-dark" value="Logout" onClick={handeleLogout} />
			</div>
		</div>
	)
}

export default ProfileNav
