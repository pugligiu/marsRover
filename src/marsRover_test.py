import unittest
from unittest import mock
import marsRover


class testChangeOrientation(unittest.TestCase):
	"""Test suite for marsRover.changeOrientation"""

	def test_change_orientation_N(self):
		"""Orientation changed in North"""
		orientation = 'W'
		spin = 'R'
		res = marsRover.changeOrientation(orientation, spin)
		self.assertEqual(res, 'N')


	def test_change_orientation_E(self):
		"""Orientation changed in East"""
		orientation = 'N'
		spin = 'R'
		res = marsRover.changeOrientation(orientation, spin)
		self.assertEqual(res, 'E')

	def test_change_orientation_S(self):
		"""Orientation changed in South"""
		orientation = 'E'
		spin = 'R'
		res = marsRover.changeOrientation(orientation, spin)
		self.assertEqual(res, 'S')

	def test_change_orientation_W(self):
		"""Orientation changed in West"""
		orientation = 'S'
		spin = 'R'
		res = marsRover.changeOrientation(orientation, spin)
		self.assertEqual(res, 'W')


class testMove(unittest.TestCase):
	"""Test suite for marsRover.move"""

	def test_move_up(self):
		"""Move North"""
		x = 1
		y = 1
		orientation = 'N'
		res_x, res_y = marsRover.move(x, y, orientation)
		self.assertEqual((res_x , res_y), (x, y+1))

	def test_move_right(self):
		"""Move East"""
		x = 1
		y = 1
		orientation = 'E'
		res_x, res_y = marsRover.move(x, y, orientation)
		self.assertEqual((res_x, res_y), (x+1, y))

	def test_move_down(self):
		"""Move South"""
		x = 1
		y = 1
		orientation = 'S'
		res_x, res_y = marsRover.move(x, y, orientation)
		self.assertEqual((res_x, res_y), (x, y-1))

	def test_move_left(self):
		"""Move West"""
		x = 1
		y = 1
		orientation = 'W'
		res_x, res_y = marsRover.move(x, y, orientation)
		self.assertEqual((res_x, res_y), (x-1, y))


class testCalcFinalPos(unittest.TestCase):
	"""Test suite for marsRover.calcFinalPos"""

	def test_invalid_conditions(self):
		"""Testing exceptions raised for wrong data value"""

		with self.assertRaisesRegexp(ValueError, "Invalid starting point"):
			x = 1
			maxX = 2
			y = 2
			maxY = 1
			orientation = 'E'
			commands = "MMM"
			marsRover.calcFinalPos(x,maxX,y,maxY,orientation,commands)

		with self.assertRaisesRegexp(ValueError, "Invalid orientation value"):
			x = 1
			maxX = 2
			y = 1
			maxY = 2
			orientation = 'G'
			commands = "MMM"
			marsRover.calcFinalPos(x,maxX,y,maxY,orientation,commands)

		with self.assertRaisesRegexp(ValueError, "Out of border limits"):
			x = 1
			maxX = 3
			y = 2
			maxY = 3
			orientation = 'E'
			commands = "MMMM"
			marsRover.calcFinalPos(x,maxX,y,maxY,orientation,commands)

		with self.assertRaisesRegexp(ValueError, "Invalid command value"):
			x = 1
			maxX = 3
			y = 2
			maxY = 3
			orientation = 'E'
			commands = "MMGM"
			marsRover.calcFinalPos(x,maxX,y,maxY,orientation,commands)

	def test_scenarios(self):
		"""Testing some working scenarios"""

		# Simple test case 1
		x = 1
		maxX = 5
		y = 2
		maxY = 5
		orientation = 'N'
		commands = 'LMLMLMLMM'
		res_x, res_y, res_orientation = marsRover.calcFinalPos(x, maxX, y, maxY, orientation, commands)
		exp_x, exp_y, exp_orientation = 1, 3, 'N'
		self.assertEqual((res_x, res_y, res_orientation), (exp_x, exp_y, exp_orientation))

		# Simple test case 2
		x = 3
		maxX = 5
		y = 3
		maxY = 5
		orientation = 'E'
		commands = 'MMRMMRMRRM'
		res_x, res_y, res_orientation = marsRover.calcFinalPos(x, maxX, y, maxY, orientation, commands)
		exp_x, exp_y, exp_orientation = 5, 1, 'E'
		self.assertEqual((res_x, res_y, res_orientation), (exp_x, exp_y, exp_orientation))

		# Empty commands
		x = 3
		maxX = 5
		y = 3
		maxY = 5
		orientation = 'E'
		commands = ''
		res_x, res_y, res_orientation = marsRover.calcFinalPos(x, maxX, y, maxY, orientation, commands)
		exp_x, exp_y, exp_orientation = 3, 3, 'E'
		self.assertEqual((res_x, res_y, res_orientation), (exp_x, exp_y, exp_orientation))

		# Edge position
		x = 0
		maxX = 5
		y = 0
		maxY = 5
		orientation = 'E'
		commands = 'MMMMMLMMMMM'
		res_x, res_y, res_orientation = marsRover.calcFinalPos(x, maxX, y, maxY, orientation, commands)
		exp_x, exp_y, exp_orientation = 5, 5, 'N'
		self.assertEqual((res_x, res_y, res_orientation), (exp_x, exp_y, exp_orientation))


if __name__ == '__main__':
	unittest.main(verbosity=2)