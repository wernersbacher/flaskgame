from app.game.data.enviroment_data import tracks, tyres
from app.game.data.car_data import allcars

def getResult(trackid, carid, tyreid):

	tyre_multi, tyre_used = tracks[trackid].getTyrePerformance(tyres[tyreid])
	car_multi = tracks[trackid].getCarPerformance(allcars[carid])
	time_base_track = tracks[trackid].getTimeBase()
	abs_perf = car_multi * tyre_multi

	print(f" {tyreid} {trackid} {carid} track_time {time_base_track}s tyre_perf: {tyre_multi*100:.2f} tyres_used: {tyre_used*100:.2f} car_perf: {car_multi*100:.2f}, ABS: {100*abs_perf}%")


