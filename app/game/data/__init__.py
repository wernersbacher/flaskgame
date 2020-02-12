from app.game.data.enviroment_data import tracks, tyres
from app.game.data.car_data import allcars

if __name__ == "__main__":

	multi, tyre_used = tracks["germany1"].getTyrePerformance(tyres["softslick"])
	car_multi = tracks["germany1"].getCarPerformance(allcars["buggy1"])
	print(f"softslick germany1 buggy1 {multi:.2f} {tyre_used:.2f} {car_multi:.4f}")

	multi, tyre_used = tracks["germany1"].getTyrePerformance(tyres["hardslick"])
	car_multi = tracks["germany1"].getCarPerformance(allcars["buggy2"])
	print(f"hardslick germany1 buggy2 {multi:.2f} {tyre_used:.2f} {car_multi:.4f}")

	multi, tyre_used = tracks["germany2"].getTyrePerformance(tyres["softslick"])
	car_multi = tracks["germany2"].getCarPerformance(allcars["buggy1"])
	print(f"softslick germany2 buggy1 {multi:.2f} {tyre_used:.2f} {car_multi:.4f}")

	multi, tyre_used = tracks["germany2"].getTyrePerformance(tyres["hardslick"])
	car_multi = tracks["germany2"].getCarPerformance(allcars["buggy2"])
	print(f"hardslick germany2 buggy2 {multi:.2f} {tyre_used:.2f} {car_multi:.4f}")
