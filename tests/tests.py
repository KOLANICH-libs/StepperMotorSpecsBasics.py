#!/usr/bin/env python3
import sys
from pathlib import Path
import unittest
import itertools, re

sys.path.insert(0, str(Path(__file__).parent.parent))

from collections import OrderedDict

dict = OrderedDict

import StepperMotorSpecsBasics
from StepperMotorSpecsBasics import *


# FL60SH45-2008AF
motor = {
	"serial": {"current": 1.4, "inductance": 8, "resistance": 3, "torqueHolding": 1.1, "voltage": 4.2},
	"unipolar": {"current": 2, "inductance": 2, "resistance": 1.5, "torqueHolding": 0.78, "voltage": 3},
	"parallel": {"current": 2.8, "inductance": 2, "resistance": 0.75, "torqueHolding": 1.1, "voltage": 2.1},
}


class Tests(unittest.TestCase):
	def testSimple(self):
		s = Spec(**motor["serial"])
		for modeName, spec in motor.items():
			with self.subTest(modeName=modeName):
				mode = getattr(s, modeName)
				for k in spec.keys():
					with self.subTest(k=k):
						v = getattr(mode, k)
						self.assertAlmostEqual(v, spec[k], places=1)


if __name__ == "__main__":
	unittest.main()
