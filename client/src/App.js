import React, { useEffect, useState, useContext } from 'react';
import { BrowserRouter, Routes, Route } from "react-router-dom";
import { LoginContext, loadUserInfo, setLoginContextChange } from './contexts/LoginContext';
import HomePage from './components/Pages/HomePage';
import LoginPage from './components/Authentication/LoginPage';
import RegisterPage from './components/Authentication/RegisterPage';
import ProfilePage from './components/Authentication/ProfilePage';
import PageNotFound from './components/PageNotFound';
import "./App.css"

function App() {
	const [loginContext, setLoginContext] = useState(useContext(LoginContext))

	setLoginContextChange((newContext) => {
		setLoginContext(newContext)
	})

	useEffect(() => {
		loadUserInfo();
	}, [])

	return (
		<BrowserRouter>
			<LoginContext.Provider value={loginContext} >
				<div className="App">
					<Routes>
						<Route path="/" 	end	 	element={<HomePage 		/>} />
						<Route path="/login" 		element={<LoginPage		/>} />
						<Route path="/register" 	element={<RegisterPage 	/>} />
						<Route path="/profile" 		element={<ProfilePage 	/>} />
						<Route path="*"				element={<PageNotFound 	/>} />
					</Routes>
				</div>
			</LoginContext.Provider>
		</BrowserRouter>
	);
}

export default App;
