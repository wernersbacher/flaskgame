from .enviroment_elements import Tyre, Track, Undergrounds

undergrounds = {
	"tarmac": Undergrounds(id="tarmac", name="Tarmac", abrasion=1, dry=0.8),
	"mud": Undergrounds(id="mud", name="Mud", abrasion=1.3, dry=0.3, mud=0.7),
}

tyres = {
	"hardslick": Tyre("hardslick", "Hard slicks",
					  dry=0.8, wet=0.4, mud=0.2, gravel=0.4, distance=20000),
	"softslick": Tyre("softslick", "Soft slicks",
					  dry=1, wet=0.6, mud=0.4, gravel=0.6, distance=8000),
	"rainslick": Tyre("rainslick", "Rain slicks",
					  dry=0.5, wet=0.4, mud=0.6, gravel=0.4, distance=5000),
	"mud": Tyre("rainslick", "Mud slicks",
					dry=0.5, wet=0.4, mud=1, gravel=0.4, distance=15000),
}

tracks = {
	"germany1": Track("germany1", undergroundDict={
		undergrounds["tarmac"]: 0.7,
		undergrounds["mud"]: 0.3
	},
					  length=5000, straights=0.1, corners=0.9),
	"germany2": Track("germany2", undergroundDict={
		undergrounds["tarmac"]: 0.7,
		undergrounds["mud"]: 0.3
	},
					  length=16000, straights=0.6, corners=0.4),
}
