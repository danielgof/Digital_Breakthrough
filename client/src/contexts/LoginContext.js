import React from 'react'
import { ServerAPI_GET } from '../libs/ServerAPI'

const context = 
{
	isAuth : undefined
}

let callback = () => {}

export const LoginContext = React.createContext(context)

export const setLoginContext = (newContext) => {
	callback(newContext)
}

export const setLoginContextChange = (newCallback) => {
	callback = newCallback
}

export const loadUserInfo = () => {
	ServerAPI_GET({ 
		url:"/profileinfo",
		onDataReceived : (data) => {
			setLoginContext(data)
			console.log(data)
		}
	})
}