import numpy as np
import matplotlib.pyplot as plt

def simulate_vibrations(xi, omega0, x0, v0, t_max, n_points=1000):
    t = np.linspace(0, t_max, n_points)
    
    if xi < 1: # Sous-amorti
        wd = omega0 * np.sqrt(1 - xi**2)
        A = x0
        B = (v0 + xi * omega0 * x0) / wd
        x = np.exp(-xi * omega0 * t) * (A * np.cos(wd * t) + B * np.sin(wd * t))
        label = f'Sous-amorti (xi={xi})'
    elif xi == 1: # Critique
        A = x0
        B = v0 + omega0 * x0
        x = np.exp(-omega0 * t) * (A + B * t)
        label = f'Critique (xi={xi})'
    else: # Sur-amorti
        wd = omega0 * np.sqrt(xi**2 - 1)
        A = x0
        B = (v0 + xi * omega0 * x0) / wd
        x = np.exp(-xi * omega0 * t) * (A * np.cosh(wd * t) + B * np.sinh(wd * t))
        label = f'Sur-amorti (xi={xi})'
        
    return t, x, label

# Paramètres
omega0 = 3.0
x0 = 1.0
v0 = 0.0
t_max = 10.0

plt.figure(figsize=(10, 6))

# Simulation pour différents xi
for xi in [0.2, 1.0, 2.0]:
    t, x, label = simulate_vibrations(xi, omega0, x0, v0, t_max)
    plt.plot(t, x, label=label)

plt.axhline(0, color='black', lw=1)
plt.title('Vibrations Libres pour différents taux d\'amortissement')
plt.xlabel('Temps (s)')
plt.ylabel('Déplacement x(t)')
plt.legend()
plt.grid(True)
plt.savefig('Simulations/amortissement_plot.png')
plt.show()
