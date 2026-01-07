import numpy as np

# 1. Система диференціальних рівнянь
# y'' + 2x^2*y' + y = x  =>  y'' = x - 2x^2*y' - y
def system_derivatives(x, u):
    u1, u2 = u  # u1 = y, u2 = y'
    du1 = u2
    du2 = x - 2 * (x**2) * u2 - u1
    return np.array([du1, du2])

# 2. Метод прогнозу і корекції (Ейлер + Трапеції)
def predictor_corrector_step(x, u_curr, h):
    # ПРОГНОЗ (Euler)
    f_curr = system_derivatives(x, u_curr)
    u_pred = u_curr + h * f_curr

    # КОРЕКЦІЯ (Trapezoidal)
    f_pred = system_derivatives(x + h, u_pred)
    u_corr = u_curr + (h / 2) * (f_curr + f_pred)
    
    return u_corr

# 3. Розв'язання задачі Коші на інтервалі [0.5, 0.8]
# eta - це наше припущення для y(0.5)
def solve_ivp(eta, h=0.001):
    a, b = 0.5, 0.8
    n_steps = int(round((b - a) / h))
    x = np.linspace(a, b, n_steps + 1)
    
    # Масив для зберігання розв'язку: [y, y']
    u = np.zeros((n_steps + 1, 2))

    # Умова: 2y(0.5) - y'(0.5) = 1
    # Нехай y(0.5) = eta. Тоді y'(0.5) = 2*eta - 1
    u[0] = [eta, 2 * eta - 1]

    for i in range(n_steps):
        u[i + 1] = predictor_corrector_step(x[i], u[i], h)

    # Повертаю значеня на правій межі: [y(0.8), y'(0.8)]
    return u[-1]

# 4. Метод стрільби (шукаємо eta, щоб y(0.8) = 3)
def shooting_method(epsilon=0.0001):
    # Початкові припущення для методу січних
    eta0 = 1.0
    eta1 = 2.5 
    
    # Функція нев'язки (те, що має стати нулем)
    def residual(eta):
        res = solve_ivp(eta)
        y_right = res[0]
        # y(0.8) == 3.0
        return y_right - 3.0

    phi0 = residual(eta0)
    phi1 = residual(eta1)
    
    print(f"{'Iter':<5} | {'eta (y0)':<10} | {'Residual (y_end - 3)':<20}")
    print("-" * 45)

    # Метод січних
    for i in range(20):
        if abs(phi1) < epsilon:
            return eta1
            
        # Формула січних
        eta_next = eta1 - phi1 * (eta1 - eta0) / (phi1 - phi0)
        
        eta0 = eta1
        phi0 = phi1
        eta1 = eta_next
        phi1 = residual(eta1)
        
        print(f"{i+1:<5} | {eta1:<10.6f} | {phi1:<20.6e}")

    return eta1

print("=== Пошук параметра стрільби ===")
best_eta = shooting_method()

# 5. Остаточне розв'язання з знайденим eta
final_res = solve_ivp(best_eta)
y_left = best_eta
dy_left = 2 * best_eta - 1
y_right = final_res[0]

print("\n=== Результати ===")
print(f"Знайдене y(0.5): {y_left:.6f} (Це відповідає результату МСР ~2.17)")
print(f"Обчислене y'(0.5): {dy_left:.6f}")
print("-" * 30)
print(f"Перевірка лівої умови (2y - y'): {2*y_left - dy_left:.6f} (має бути 1.0)")
print(f"Значення на правій межі y(0.8): {y_right:.6f} (має бути 3.0)")