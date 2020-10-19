import sympy
from sympy import Matrix

# define starting point
X0 = 4
Y0 = 4
# define function for evaluation
FUNC_EXPRESSION = "(1-x)^2 + 100*(y-x*x)^2"


x, y = sympy.symbols("x y")

f = sympy.sympify(FUNC_EXPRESSION)

# r = f.subs({x: 1, y: 1})
# print(r)

starting_vector = sympy.Matrix([X0, Y0])
gradient = Matrix([f.diff(e) for e in [x, y]])
hessian = Matrix([[f.diff(p1).diff(p2) for p1 in [x, y]] for p2 in [x, y]])
hessian = hessian.inv()

for i in range(0, 100):
    sub_inp = dict(zip([x, y], starting_vector))
    starting_vector = starting_vector - 0.2 * hessian.subs(sub_inp) * gradient.subs(sub_inp)
    print(starting_vector)

print(starting_vector)

# sympy.plotting.plot3d(f, (x, -1, 1), (y, -1, 1))

# sympy.plotting.plot3d(F)
