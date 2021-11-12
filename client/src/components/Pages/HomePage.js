import React from 'react'
import cs from "./Home.module.css"
import getClassName from "../../libs/GetCSS"
import AuthButton from '../Authentication/AuthButton'

const HomePage = () => {
	return (
		<div className={getClassName([cs.headerBg, "container-fluid px-0"])}>
			<div className={getClassName([cs.headerRow, "row align-items-start justify-content-end mx-0"])}>
				<div className={getClassName([cs.login, "col-auto mx-4 mt-4"])}>
					<AuthButton />
				</div>
			</div>
			<div className={getClassName([cs.headerRow, "row align-items-center justify-content-center mx-0"])}>
				<div className={getClassName([cs.headerText, "col-auto"])}>
						Поиск неучтенных предприятий,<br /> загрязняющих воздух
				</div>
			</div>
		</div>
	)
	//Наша задача - устранить экологические проблемы!
}

export default HomePage
