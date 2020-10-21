import sympy
from sympy import Matrix

# define starting point
START_POINT = (-2.7, 3.0)
# define function for evaluation
FUNC_EXPRESSION = "(1-x)^2 + 100*(y-x*x)^2"
# Epsilon as an exit condition
EPSILON = 10 ** -8
# Destination (we are looking for minimum)
DEST = 0
# Maximum number of iterations
ITER_MAX = 1000
# Alpha coefficient
DEFAULT_ALPHA = 1


def newton_iterate(alpha, starting_vector, n_iterations=ITER_MAX, f_expr=FUNC_EXPRESSION, destination=DEST,
                   epsilon=EPSILON):
    starting_vector = sympy.Matrix(starting_vector)

    # compute bounds for exit condition
    lower_bound = destination - epsilon
    upper_bound = destination + epsilon

    # get symbols from sympy
    x, y = sympy.symbols("x y")
    f = sympy.sympify(f_expr)

    gradient = Matrix([f.diff(e) for e in [x, y]])  # compute gradient vector
    hessian = Matrix([[f.diff(p1).diff(p2) for p1 in [x, y]] for p2 in [x, y]])  # compute Hessian
    hessian = hessian.inv()  # Invert hessian for usage of algorithm
    results = list()
    for i in range(0, n_iterations):
        sub_inp = dict(zip([x, y], starting_vector))
        value_at_point = f.subs(sub_inp).doit()
        results.append(sympy.N(value_at_point))
        if lower_bound <= value_at_point <= upper_bound:
            break
        starting_vector = starting_vector - alpha * hessian.subs(sub_inp) * gradient.subs(sub_inp)
    return results


result_0 = newton_iterate(DEFAULT_ALPHA, START_POINT)
print(f"Total number of iterations: {len(result_0)}")
print(f"Result of f(x,y): {sympy.N(result_0[-1]):.8f}")

result_1 = newton_iterate(0.9, START_POINT)
result_2 = newton_iterate(0.5, START_POINT)
result_3 = newton_iterate(0.3, START_POINT)
from matplotlib import pyplot as plt

plt.scatter([1, 0.9, 0.5, 0.3], [len(result_0), len(result_1), len(result_2), len(result_3)])
plt.title("Metoda Newtona. Liczba iteracji w zależności od alpha")
plt.xlabel("Wspołczynnik alpha")
plt.ylabel("Liczba iteracji")
plt.show()
