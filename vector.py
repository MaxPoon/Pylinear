import math

def angle(v1, v2, degree = False):
	if str(type(v1)) != "<class 'vector.Vector'>" or str(type(v2)) != "<class 'vector.Vector'>":
		raise Exception("The parameters must be vectors")
	if degree:
		return v1.mag()*v2.mag()/(v1*v2) * (360/math.pi)
	return v1.mag()*v2.mag()/(v1*v2)

class Vector(object):
	def __init__(self, coordinates):
		try:
			if not coordinates:
				raise ValueError
			self.coordinates = tuple(coordinates)
			self.dimension = len(coordinates)

		except ValueError:
			raise ValueError('The coordinates must be nonempty')

		except TypeError:
			raise TypeError('The coordinates must be an iterable')


	def __str__(self):
		return 'Vector: {}'.format(self.coordinates)


	def __eq__(self, v):
		return self.coordinates == v.coordinates

	def __add__(self, other):
		if str(type(other)) == "<class 'vector.Vector'>":
			try:
				assert self.dimension == other.dimension
			except Exception:
				raise AssertionError("The length of the vectors must be the same")
			newList = [self.coordinates[i]+other.coordinates[i] for i in range(self.dimension)]
			return Vector(newList)
		if str(type(other)) == "<class 'int'>" or str(type(other)) == "<class 'float'>":
			newList = [self.coordinates[i]+other for i in range(self.dimension)]
			return Vector(newList)

	def __sub__(self, other):
		if str(type(other)) == "<class 'vector.Vector'>":
			try:
				assert self.dimension == other.dimension
			except Exception:
				raise AssertionError("The length of the vectors must be the same")
			newList = [self.coordinates[i]-other.coordinates[i] for i in range(self.dimension)]
			return Vector(newList)
		if str(type(other)) == "<class 'int'>" or str(type(other)) == "<class 'float'>":
			newList = [self.coordinates[i]-other for i in range(self.dimension)]
			return Vector(newList)

	def __mul__(self, other):
		if str(type(other)) == "<class 'vector.Vector'>":
			try:
				assert self.dimension == other.dimension
			except Exception:
				raise AssertionError("The length of the vectors must be the same")
			newList = [self.coordinates[i]*other.coordinates[i] for i in range(self.dimension)]
			return sum(newList)
		if str(type(other)) == "<class 'int'>" or str(type(other)) == "<class 'float'>":
			newList = [self.coordinates[i]*other for i in range(self.dimension)]
			return Vector(newList)

	def __truediv__(self, other):
		if str(type(other)) == "<class 'vector.Vector'>":
			try:
				assert self.dimension == other.dimension
			except Exception:
				raise AssertionError("The length of the vectors must be the same")
			newList = [self.coordinates[i]/other.coordinates[i] for i in range(self.dimension)]
			return Vector(newList)
		if str(type(other)) == "<class 'int'>" or str(type(other)) == "<class 'float'>":
			newList = [self.coordinates[i]/other for i in range(self.dimension)]
			return Vector(newList)

	def mag(self):
		return sum(n**2 for n in self.coordinates)**0.5

	def unit(self):
		m = self.mag()
		return self / m

	def angle(self, other, degree = False):
		if str(type(other)) != "<class 'vector.Vector'>":
			raise Exception("The parameter must be vector")
		if degree:
			return self.mag()*other.mag()/(self*other) * (360/math.pi)
		return self.mag()*other.mag()/(self*other)