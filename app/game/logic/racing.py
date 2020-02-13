from app.game.data.enviroment_data import tracks, tyres
from app.game.data.car_data import allcars

def calcTime(baseTime, absPerf):

	return baseTime * (1/(0.7*absPerf+0.56) + 0.2)/2

def calcAbsPerf(car_multi, tyre_multi):
	return car_multi * tyre_multi


def getResult(trackid, carid, tyreid):
	used_track = tracks[trackid]

	tyre_multi, tyre_used = used_track.getTyrePerformance(tyres[tyreid])
	car_multi = used_track.getCarPerformance(allcars[carid])
	time_base_track = used_track.getTimeBase()
	abs_perf = calcAbsPerf(car_multi, tyre_multi)
	time_taken = calcTime(time_base_track, abs_perf)

	#print(f" {tyreid} {trackid} {carid} track_time {time_base_track}s tyre_perf: {tyre_multi*100:.2f} tyres_used: {tyre_used*100:.2f} car_perf: {car_multi*100:.2f}, ABS: {100*abs_perf}%")

	return time_taken, tyre_used




