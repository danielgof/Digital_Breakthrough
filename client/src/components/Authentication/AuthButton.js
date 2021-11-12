import React, { useContext, useEffect } from 'react'
import { Link  } from "react-router-dom";
import { LoginContext } from '../../contexts/LoginContext';
import getClassName from '../../libs/GetCSS';
import profileLogo from './profile40.png'
import cs from './Auth.module.css'

const AuthButton = () => {
	const loginContext = useContext(LoginContext)

	return (
		<div>
			{
			loginContext.isAuth === undefined ? (
				<div>Loading... </div>
			) : (
				loginContext.isAuth ? (
					<div>
						<Link to="/profile">  
							<img src={profileLogo} alt="logo" className={cs.logo}/>
						</Link>
					</div>
				) : (
					<div>
						<Link to="/login"> <input type="button" className={getClassName([cs.AuthButton, "btn btn-dark"])} value="Войти" /> </Link>
					</div>
				)
			)
			}
		</div>
	)
}

export default AuthButton
