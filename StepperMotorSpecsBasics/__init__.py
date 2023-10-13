import typing
from enum import IntEnum
from math import sqrt
from warnings import warn

warn("We have moved from M$ GitHub to https://codeberg.org/KOLANICH-libs/StepperMotorSpecsBasics.py , read why on https://codeberg.org/KOLANICH/Fuck-GuanTEEnomo .")

SQRT2 = sqrt(2)
SQRT2_INV = 1.0 / SQRT2


class DrivingModeInt(IntEnum):
	"""To be used for serialization purposes"""

	unknown = 0
	serial = 1
	unipolar = 2
	parallel = 3


modeNames = set(el.name for el in DrivingModeInt)


class Spec:
	"""Used to specify some specifications of a motor in a normal form"""

	__slots__ = ("current", "inductance", "resistance", "torqueHolding", "voltage")

	def __init__(self, current: float, inductance: float, resistance: float, torqueHolding: float, voltage: float):
		self.current = current
		self.inductance = inductance
		self.resistance = resistance
		self.torqueHolding = torqueHolding
		self.voltage = voltage

	@property
	def serial(self) -> "DrivingMode":
		return BipolarSerialDrivingMode(self)

	@property
	def unipolar(self) -> "DrivingMode":
		return UnipolarDrivingMode(self)

	@property
	def parallel(self) -> "DrivingMode":
		return BipolarParallelDrivingMode(self)

	def __getitem__(self, k: typing.Union[str, int, DrivingModeInt]):
		if isinstance(k, str):
			if k in modeNames:
				k = getattr(DrivingModeInt, str)
			else:
				raise ValueError(k, modeNames)

		if not isinstance(k, int):
			raise ValueError(k)

		k = DrivingModeInt(k)

		return getattr(self, k.name)


class DrivingMode:
	"""Used to get parameters corresponding to certain driving mode"""

	__slots__ = ("spec",)

	CODE = DrivingModeInt.unknown

	def __init__(self, spec: Spec):
		self.spec = spec

	CURRENT_RATIO = None
	INDUCTANCE_RATIO = None
	RESISTANCE_RATIO = None
	VOLTAGE_RATIO = None
	HOLDING_TORQUE_RATIO = None

	@property
	def current(self) -> float:
		return self.spec.current * self.__class__.CURRENT_RATIO

	@property
	def inductance(self) -> float:
		return self.spec.inductance * self.__class__.INDUCTANCE_RATIO

	@property
	def resistance(self) -> float:
		return self.spec.resistance * self.__class__.RESISTANCE_RATIO

	@property
	def torqueHolding(self) -> float:
		return self.spec.torqueHolding * self.__class__.HOLDING_TORQUE_RATIO

	@property
	def voltage(self) -> float:
		return self.spec.voltage * self.__class__.VOLTAGE_RATIO


class BipolarSerialDrivingMode(DrivingMode):
	"""Bipolar serial driving mode: full windings are used, subwindings are connected serially.
	Advantage: increased torque.
	Disadvantage: decreased speed.
	"""

	__slots__ = ()

	CODE = DrivingModeInt.serial
	HOLDING_TORQUE_RATIO = VOLTAGE_RATIO = RESISTANCE_RATIO = INDUCTANCE_RATIO = CURRENT_RATIO = 1.0  # by definition


class UnipolarDrivingMode(DrivingMode):
	"""Unipolar driving mode: half of a winding is used.
	Advantage: increased speed due to lower self-inductance.
	Disadvantage: decreased torque, worse winding utilization.
	"""

	__slots__ = ()

	CODE = DrivingModeInt.unipolar
	CURRENT_RATIO = SQRT2
	INDUCTANCE_RATIO = 0.25  # N/2 turns, but inductance ~ N**2
	RESISTANCE_RATIO = 0.5  # half of the coil is utilized
	VOLTAGE_RATIO = SQRT2_INV
	HOLDING_TORQUE_RATIO = SQRT2_INV


class BipolarParallelDrivingMode(DrivingMode):
	"""Bipolar parallel driving mode: full windings are used, subwindings are connected parallely.
	Advantage: combines torque of serial mode with speed of unipolar mode.
	Disadvantage: requires higher current to utilize the advandage, worse energy efficiency.
	"""

	__slots__ = ()

	CODE = DrivingModeInt.parallel
	CURRENT_RATIO = 2
	RESISTANCE_RATIO = INDUCTANCE_RATIO = 0.25  # 2 halves of windings connected parallely
	VOLTAGE_RATIO = 0.5
	HOLDING_TORQUE_RATIO = 1
