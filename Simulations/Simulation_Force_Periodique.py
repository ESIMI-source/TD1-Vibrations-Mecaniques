import numpy as np
import matplotlib.pyplot as plt

def square_wave_fourier(t, P0, T, n_harmonics):
    Omega = 2 * np.pi / T
    p = np.zeros_like(t)
    for n in range(1, n_harmonics + 1, 2):
        bn = 4 * P0 / (n * np.pi)
        p += bn * np.sin(n * Omega * t)
    return p

def system_response(t, P0, T, n_harmonics, m, omega0):
    Omega = 2 * np.pi / T
    x = np.zeros_like(t)
    for n in range(1, n_harmonics + 1, 2):
        bn = 4 * P0 / (n * np.pi)
        amplitude = (bn / m) / (omega0**2 - (n * Omega)**2)
        x += amplitude * np.sin(n * Omega * t)
    return x

# Paramètres
P0 = 1000.0
T = 2.0
m = 1000.0
omega0 = 5.0
t = np.linspace(0, 6, 1000)

# Calcul de la force et de la réponse
p_force = square_wave_fourier(t, P0, T, 50)
x_resp = system_response(t, P0, T, 50, m, omega0)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

ax1.plot(t, p_force, color='red')
ax1.set_title('Force Excitatrice (Onde Carrée Impaire - Série de Fourier)')
ax1.set_ylabel('Force p(t)')
ax1.grid(True)

ax2.plot(t, x_resp, color='blue')
ax2.set_title('Réponse du Système en Régime Permanent')
ax2.set_xlabel('Temps (s)')
ax2.set_ylabel('Déplacement x(t)')
ax2.grid(True)

plt.tight_layout()
plt.savefig('Simulations/force_periodique_plot.png')
plt.show()
