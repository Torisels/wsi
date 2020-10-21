import sympy
from sympy import Matrix
from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D

# define starting point as N dimensional vector
starting_point = [0, 5]
# compute number of dimensions
DIM = len(starting_point)
# define function for evaluation
FUNC_EXPRESSION = "(1-x)^2 + 100*(y-x*x)^2"
# Epsilon as an exit condition
EPSILON = 10 ** -8
# Maximum number of iterations
ITER_MAX = 1000
# Alpha coefficient
ALPHA = 0.00001
# Destination (we are looking for minimum)
DEST = 0

lower_bound = DEST - EPSILON
upper_bound = DEST + EPSILON

x, y = sympy.symbols("x y")
f = sympy.sympify(FUNC_EXPRESSION)
starting_vector = sympy.Matrix(starting_point)

gradient = Matrix([f.diff(e) for e in [x, y]])  # compute gradient vector

input_values = list()
xs = list()
ys = list()
zs = list()
sub_inp = dict(zip([x, y], starting_vector))

for i in range(ITER_MAX):
    starting_vector = starting_vector - ALPHA * gradient.subs(sub_inp)

    sub_inp = dict(zip([x, y], starting_vector))
    value_at_point = f.subs(sub_inp).doit()
    xs.append(xi)
    ys.append(yi)
    zs.append(value_at_point)

    if lower_bound <= value_at_point <= upper_bound:
        print(f"Total number of iterations: {i}")
        break

print(zs)
fig = pyplot.figure()
ax = Axes3D(fig)
ax.scatter(xs, ys, zs)
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
fig.show()
