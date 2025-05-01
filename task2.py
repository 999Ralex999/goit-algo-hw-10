import random
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

def f(x):
    return x ** 2

# Метод Монте-Карло для обчислення інтеграла
def monte_carlo_integrate(func, a, b, num_samples=100000):
    count = 0
    for _ in range(num_samples):
        x = random.uniform(a, b)
        y = random.uniform(0, b ** 2)
        if y <= func(x):
            count += 1
    area = (b - a) * (b ** 2)
    return area * (count / num_samples)

a, b = 0, 2

mc_result = monte_carlo_integrate(f, a, b)

quad_result, _ = quad(f, a, b)

print("\n=== Завдання 2 ===")
print(f"Результат методу Монте-Карло: {mc_result:.6f}")
print(f"Результат quad(): {quad_result:.6f}")

# Побудова графіка
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

fig, ax = plt.subplots()
ax.plot(x, y, 'r', linewidth=2)

ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('f(x) = x^2, інтегрування від 0 до 2')

plt.grid()
plt.show()
