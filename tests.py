from datetime import datetime, timedelta
import unittest
from app import create_app, db
from app.models import User
from config import Config

from app.game.logic import racing

class TestConfig(Config):
	TESTING = True


class RacingTests(unittest.TestCase):
	def setUp(self):
		self.app = create_app(TestConfig)
		self.app_context = self.app.app_context()
		self.app_context.push()

	def tearDown(self):
		self.app_context.pop()

	def test_racing_tyres(self):

		#testing germanyhs with 70% tarmac, 30% mud, comparing the times
		softslick, _ = racing.getResult(trackid="germanyhs", carid="buggy1", tyreid="softslick")
		hardslick, _ = racing.getResult(trackid="germanyhs", carid="buggy1", tyreid="hardslick")
		rainslick, _ = racing.getResult(trackid="germanyhs", carid="buggy1", tyreid="rainslick")
		softmud, _ = racing.getResult(trackid="germanyhs", carid="buggy1", tyreid="softmud")
		hardmud, _ = racing.getResult(trackid="germanyhs", carid="buggy1", tyreid="hardmud")
		heavymud, _ = racing.getResult(trackid="germanyhs", carid="buggy1", tyreid="heavymud")
		self.assertEqual(True, softslick < hardslick)
		self.assertEqual(True, hardslick < rainslick)
		self.assertEqual(True, softslick < softmud)
		self.assertEqual(True, softslick < hardmud)
		self.assertEqual(True, softslick < heavymud)

		# testing germanyhs with 70% tarmac, 30% mud, comparing the times LOOONG
		softslick, _ = racing.getResult(trackid="germanyhslong", carid="buggy1", tyreid="softslick")
		hardslick, _ = racing.getResult(trackid="germanyhslong", carid="buggy1", tyreid="hardslick")
		rainslick, _ = racing.getResult(trackid="germanyhslong", carid="buggy1", tyreid="rainslick")
		softmud, _ = racing.getResult(trackid="germanyhslong", carid="buggy1", tyreid="softmud")
		hardmud, _ = racing.getResult(trackid="germanyhslong", carid="buggy1", tyreid="hardmud")
		heavymud, _ = racing.getResult(trackid="germanyhslong", carid="buggy1", tyreid="heavymud")
		self.assertEqual(True, softslick > hardslick)
		self.assertEqual(True, hardslick < rainslick)
		self.assertEqual(True, softslick > hardmud)

		# testing germanybh with 40% tarmac, 60% mud, comparing the times
		softslick, _ = racing.getResult(trackid="germanybh", carid="buggy1", tyreid="softslick")
		hardslick, _ = racing.getResult(trackid="germanybh", carid="buggy1", tyreid="hardslick")
		rainslick, _ = racing.getResult(trackid="germanybh", carid="buggy1", tyreid="rainslick")
		softmud, _ = racing.getResult(trackid="germanybh", carid="buggy1", tyreid="softmud")
		hardmud, _ = racing.getResult(trackid="germanybh", carid="buggy1", tyreid="hardmud")
		heavymud, _ = racing.getResult(trackid="germanybh", carid="buggy1", tyreid="heavymud")
		self.assertEqual(True, softslick < hardslick)
		self.assertEqual(True, hardslick > rainslick)
		self.assertEqual(True, softslick > softmud)
		self.assertEqual(True, softmud < hardmud)

	def test_racing_car(self):
		buggy1, _ = racing.getResult(trackid="germanyhs", carid="buggy1", tyreid="softslick")
		buggy2, _ = racing.getResult(trackid="germanyhs", carid="buggy2", tyreid="softslick")
		self.assertEqual(True, buggy1 > buggy2)


		buggy1, _ = racing.getResult(trackid="germanybh", carid="buggy1", tyreid="softslick")
		buggy2, _ = racing.getResult(trackid="germanybh", carid="buggy2", tyreid="softslick")
		self.assertEqual(True, buggy1 < buggy2)



if __name__ == '__main__':
	unittest.main(verbosity=2)
