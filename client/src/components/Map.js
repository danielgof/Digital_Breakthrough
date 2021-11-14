import React, { useState } from "react"
import { GoogleMap, useLoadScript, Marker } from "@react-google-maps/api"
import { ServerAPI_POST } from "../libs/ServerAPI"

const mapContainerStyle = {
    width : "700px",
    height : "400px"
}
const center = {
    lat : 55.163427100804874,
    lng : 61.438366276611305
}

const libraries = ["places"]

const Map = () => {
	const [markers, setMarkers] = useState([])
	const [badGuys, setBadGuys] = useState(undefined)

	const {isLoaded, loadError} = useLoadScript({
		googleMapsApiKey : "AIzaSyC9rMgJMXpXLbA-pb8uB2heVbxXRN60_xc",
		libraries
	})
    if (loadError) return "Error loading maps"
    if (!isLoaded) return "Loading Maps"

	const handleFind = () => {
		ServerAPI_POST({
			url : "/find",
			sendObj : {markers},
			onDataReceived : (data) => {
				setBadGuys(data.badGuys)
			}
		})
	}

	return (
		<div className="container-fluid px-0">
			<div className="row">
				<div className="col-auto">
					<GoogleMap 
						mapContainerStyle={mapContainerStyle} 
						zoom={11} 
						center={center}
						onClick={(e) => {
							if (markers.length < 4) {
								setMarkers([...markers, { lat : e.latLng.lat(), lng : e.latLng.lng(), time : new Date() }])
								console.log(e.latLng.lat(), e.latLng.lng())
							}
						}}
					>  
						{markers.map(marker => (
							<Marker key={marker.time.toISOString()} position={{ lat : marker.lat, lng : marker.lng }}/>)
							)}
					</GoogleMap>
					<div className="mb-3 mt-1">
						<input type="button" className="btn btn-warning" value="Отчистить метки" onClick={() => {setMarkers([])}} />
						<input type="button" className="btn btn-warning mx-3" value="Найти нарушителей" onClick={handleFind} />
					</div>
				</div>
				<div className="col">
					{
						(badGuys === undefined) ? (
							<p> Ожидаем . . . </p>
						) : (
							<div>
								{(badGuys.length === 0) ? (
									<p> Нарушители не обнаружены </p>
								) : (
									<div>
										<h4> Предполагаемые нарушители: </h4>
										<div className="container-fluid px-0">
											
											<div className="row">
												<div className="col">
													<h5>Название</h5>
												</div>
												<div className="col">
													<h5>Адресс</h5>
												</div>
											</div>
												{badGuys.map((guy, i) => (
													<div key={i} className="row mb-4">
														<div className="col">
															{guy.name}
														</div>
														<div className="col">
															{guy.address}
														</div>
													</div>
												))}
										</div>
									</div>
								)
							}
							</div>
						)
					}
				</div>
			</div>
		</div>
	)
}

export default Map
