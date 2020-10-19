import sympy
from sympy import Matrix

# define starting point as N dimensional vector
starting_point = [4, 4]
# compute number of dimensions
DIM = len(starting_point)
# define function for evaluation
FUNC_EXPRESSION = "(1-x)^2 + 100*(y-x*x)^2"
# Epsilon as an exit condition
EPSILON = 10 ** -8
# Maximum number of iterations
ITER_MAX = 1000
# Alpha coefficient
ALPHA = 0.2
# Destination (we are looking for minimum)
DEST = 0

lower_bound = DEST - EPSILON
upper_bound = DEST + EPSILON

x, y = sympy.symbols("x y")
f = sympy.sympify(FUNC_EXPRESSION)
starting_vector = sympy.Matrix(starting_point)

gradient = Matrix([f.diff(e) for e in [x, y]])  # compute gradient vector
hessian = Matrix([[f.diff(p1).diff(p2) for p1 in [x, y]] for p2 in [x, y]])  # compute Hessian
hessian = hessian.inv()  # Invert hessian

input_values = list()

for i in range(ITER_MAX):
    sub_inp = dict(zip([x, y], starting_vector))
    value_at_point = f.subs(sub_inp).doit()
    if lower_bound <= value_at_point <= upper_bound:
        break
    starting_vector = starting_vector - ALPHA * hessian.subs(sub_inp) * gradient.subs(sub_inp)
    input_values.append(starting_vector)

print(input_values)


