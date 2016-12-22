# Pylinear
A lightweight python package for solving linear algebra problems

## Usage

### Vector

#### Create and print vectors:

Example:

```python
>>> v1 = vector.Vector([1,2,3])
>>> v2 = vector.Vector([6,5,4])
>>> print(v1, v2)
Vector: (1, 2, 3) Vector: (6, 5, 4)
```

#### Addition and subtraction: + and -

Example:

```python
>>> v = v1 + v2
>>> print(v)
Vector: (7, 7, 7)

>>> v = v1 + 3
>>> print(v)
Vector: (4, 5, 6)

>>> v = v1 - v2
>>> print(v)
Vector: (-5, -3, -1)
```

#### Multiplication: *

Example:

```python
>>> v = v1 * 3
>>> print(v)
Vector: (3, 6, 9)
```

#### Division: /

Example:

```python
>>> v = v1 / 3
>>> print(v)
Vector: (0.3333333333333333, 0.6666666666666666, 1.0)
```

#### Dot product: *

Example:

```python
>>> v = v1 * v2
>>> print(v)
28
```

#### Cross product: **

Example:

```python
>>> v = v1 ** v2
>>> print(v)
Vector: (-7, 14, -7)
```

#### Get magnitude: Vector.mag()

Example:

```python
>>> v1.mag()
3.7416573867739413
```

#### Get cosine similarity: Vector.sim()

Example:

```python
>>> v1.sim(v2)
0.8528028654224418
```

#### Get angle: Vector.angle()

Example:

```python
>>> v1.angle(v2)
0.5494672447576273
>>> v1.angle(v2, degree = True)
62.96430821058771
```

#### Checking for parallelism and orthogonality: Vector.parallel() and Vector.orthogonal()

Example:

```python
>>> v1.parallel(v2)
False

>>> v1.orthogonal(v2)
False
```

#### Vector projection: Vector.projectTo()

Example:

```python
>>> v = v1.projectTo(v2)
>>> print(v)
Vector: (2.1818181818181817, 1.8181818181818181, 1.4545454545454544)
```

### Line

#### Initialization: Line(normal vector, constant term)

Example:

```python
>>> import line
>>> l1 = line.Line([1,2],3)
>>> l2 = line.Line([1,2],4)
>>> l3 = line.Line([2,4],6)

>>> print(l1)
x_1 + 2x_2 = 3
```

#### Checking for parallelism: Line.parallel(Line)

Example:

```python
>>> l1.parallel(l3)
True
```
#### Checking for equality: ==

Example:

```python
>>> l1 == l2
False
>>> l1 == l3
True
```

### Plane

#### Initialization: Plane(normal vector, constant term)

Example:

```python
>>> p1 = Plane([1,2,3],4)
>>> p2 = Plane([2,4,6],8)
```

#### Checking for parallelism: Plane.parallel(Plane)

Example:

```python
>>> p1.parallel(p2)
True
```
#### Checking for equality: ==

Example:

```python
>>> p1 == p2
True
```

