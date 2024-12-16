from numpy import arange
from scipy.optimize import line_search
from matplotlib import pyplot as plt

# objective function
def objective(x):
    return (-5.0 + x)**2.0

# gradient for the objective function
def gradient(x):
    return 2.0 * (x - 5.0)  # Исправленный градиент

# define the starting point (остается прежним)
point = 5.0  # Начальная точка
# define the direction to move (уменьшено)
direction = 0.1  # Меньшее направление

# print the initial conditions
print('start=%.1f, direction=%.1f' % (point, direction))

# perform the line search
result = line_search(objective, gradient, point, direction)

# summarize the result
alpha = result[0]

# Проверка на наличие значения alpha
if alpha is not None:
    print('Alpha: %.3f' % alpha)
    print('Function evaluations: %d' % result[1])

    # define objective function minima
    end = point + alpha * direction

    # evaluate objective function minima
    print('f(end) = f(%.3f) = %.3f' % (end, objective(end)))

    # define range
    r_min, r_max = -10.0, 20.0  # Новый диапазон для графика

    # prepare inputs
    inputs = arange(r_min, r_max, 0.1)

    # compute targets
    targets = [objective(x) for x in inputs]

    # plot inputs vs objective
    plt.plot(inputs, targets, '--', label='objective')
    # plot start and end of the search
    plt.plot([point], [objective(point)], 's', color='g', label='start')
    plt.plot([end], [objective(end)], 's', color='r', label='end')
    plt.legend()
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Line Search on Convex Function')
    plt.grid()
    plt.show()
else:
    print("Line search did not find a suitable alpha.")
# Не сойдется
