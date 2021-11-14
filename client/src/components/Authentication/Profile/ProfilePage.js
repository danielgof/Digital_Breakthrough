import React from 'react'
import { Routes, Route } from "react-router-dom";
import MyMessages from '../../Messages/MyMessages';
import NewMessages from '../../Messages/NewMessages';
import ProcMessages from '../../Messages/ProcMessages';
import EndMessages from '../../Messages/EndMessages';
import ProfileNav from './ProfileNav'
import ProfileInfo from './ProfileInfo'
import PageNotFound from '../../PageNotFound'
import AddMessage from '../../Messages/AddMessage';
import Message from '../../Messages/Message';

const ProfilePage = () => {
	return (
		<div className="container-fluid mt-5">
			<div className="row">
				<div className="col-auto px-5">
					<ProfileNav />
				</div>
				<div className="col">
					<Routes>
						<Route path="" 	end	 			element={<ProfileInfo	/>} />
						<Route path="mymessages" 		element={<MyMessages	/>} />
						<Route path="newmessages" 		element={<NewMessages 	/>} />
						<Route path="procmessages" 		element={<ProcMessages 	/>} />
						<Route path="endmessages" 		element={<EndMessages 	/>} />
						<Route path="addmessage" 		element={<AddMessage 	/>} />
						<Route path="messages/:id" 		element={<Message		/>} />
						<Route path="*"					element={<PageNotFound 	/>} />
					</Routes>
				</div>
				
			</div>
		</div>
	)
}

export default ProfilePage
