import math

def angle(v1, v2, degree = False):
	if str(type(v1)) != "<class 'vector.Vector'>" or str(type(v2)) != "<class 'vector.Vector'>":
		raise Exception("The parameters must be vectors")
	a = math.acos(v1.sim(v2))
	if degree:
		return a * (360/math.pi)
	return a

def parallel(v1, v2):
	if str(type(v1)) != "<class 'vector.Vector'>" or str(type(v2)) != "<class 'vector.Vector'>":
		raise Exception("The parameters must be vectors")
	u1 = v1.unit()
	u2 = v2.unit()
	if u1==u2 or (u1+u2).mag()==0: return True
	return False

def orthogonal(v1, v2, error=0.0001):
	if str(type(v1)) != "<class 'vector.Vector'>" or str(type(v2)) != "<class 'vector.Vector'>":
		raise Exception("The parameters must be vectors")
	return v1*v2<=error

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

	def __pow__(self, other):
		if str(type(other)) == "<class 'vector.Vector'>":
			try:
				assert self.dimension == 3 and other.dimension==3
			except Exception:
				raise AssertionError("The length of the vectors must be the 3")
			x1,y1,z1 = self.coordinates
			x2,y2,z2 = other.coordinates
			return Vector([y1*z2-y2*z1, z1*x2-z2*x1, x1*y2-x2*y1])

		else:
			raise TypeError("The parameter must be vector")

	def mag(self):
		return sum(n**2 for n in self.coordinates)**0.5

	def unit(self):
		m = self.mag()
		return self / m

	def sim(self, other):
		if str(type(other)) != "<class 'vector.Vector'>":
			raise Exception("The parameter must be vector")			
		return (self*other)/(self.mag()*other.mag())

	def angle(self, other, degree = False):
		if str(type(other)) != "<class 'vector.Vector'>":
			raise Exception("The parameter must be vector")
		a = math.acos(self.sim(other))
		if degree:
			return a * (360/math.pi)
		return a

	def parallel(self, other):
		if str(type(other)) != "<class 'vector.Vector'>":
			raise Exception("The parameter must be vector")
		u1 = self.unit()
		u2 = other.unit()
		if u1==u2 or (u1+u2).mag()==0: return True
		return False

	def orthogonal(self, other, error=0.0001):
		if str(type(other)) != "<class 'vector.Vector'>":
			raise Exception("The parameter must be vector")
		return self*other <= error

	def projectTo(self, other):
		if str(type(other)) != "<class 'vector.Vector'>":
			raise Exception("The parameter must be vector")
		u = other.unit()
		return u * (self * u)