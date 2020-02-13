from .enviroment_elements import Tyre, Track, Undergrounds

undergrounds = {
	"tarmac": Undergrounds(id="tarmac", name="Tarmac", abrasion=1, dry=0.75),
	"mud": Undergrounds(id="mud", name="Light Mud", abrasion=1.2, wet=0.5, mud=0.6),
	"heavymud": Undergrounds(id="mud", name="Heavy Mud", abrasion=1.3, wet=0.7, mud=0.4, heavymud=0.5),
}

tyres = {
	"hardslick": Tyre("hardslick", "Hard slicks",
					  dry=0.8, wet=0.4, mud=0.2, gravel=0.4, distance=20000),
	"softslick": Tyre("softslick", "Soft slicks",
					  dry=1, wet=0.6, mud=0.3, gravel=0.6, distance=8000),
	"rainslick": Tyre("rainslick", "Rain slicks",
					  dry=0.5, wet=0.4, mud=0.6, gravel=0.4, distance=6000),
	"softmud": Tyre("softmud", "Soft Muds/Tarmac",
					dry=0.7, wet=0.6, mud=0.8, gravel=0.4, heavymud=0.3, distance=6300),
	"hardmud": Tyre("hardmud", "Hard Muds/Tarmac",
					dry=0.55, wet=0.5, mud=0.6, gravel=0.2, distance=15000),
	"heavymud": Tyre("heavymud", "Heavy Muds",
					dry=0.2, wet=0.7, mud=0.7, gravel=0.6, heavymud=0.6, distance=10000),
}

tracks = {
	"germanyhs": Track("germanyhs", "Hohensülzen, Germany", undergroundDict={
		undergrounds["tarmac"]: 0.7,
		undergrounds["mud"]: 0.3
	},
					  length=3500, straights=0.2, corners=0.8),
	"germanyhslong": Track("germanyhslong", "Hohensülzen, Germany", undergroundDict={
		undergrounds["tarmac"]: 0.7,
		undergrounds["mud"]: 0.3
	}, testOnly=False,
					  length=7800, straights=0.2, corners=0.8),
	"germanybh": Track("germanybh", "Buxtehude, Germany", undergroundDict={
		undergrounds["tarmac"]: 0.4,
		undergrounds["mud"]: 0.6
	},
					  length=4500, straights=0.7, corners=0.3),
	"germanybhlong": Track("germanybhlong", "Buxtehude, Germany", undergroundDict={
		undergrounds["tarmac"]: 0.4,
		undergrounds["mud"]: 0.6
	}, testOnly=True,
					  length=12000, straights=0.7, corners=0.3),
}
