import numpy as np
import matplotlib.pyplot as plt

def amplification_factor(r, xi):
    return 1 / np.sqrt((1 - r**2)**2 + (2 * xi * r)**2)

# Paramètres
r = np.linspace(0, 3, 1000)
xi_values = [0.05, 0.1, 0.2, 0.5]

plt.figure(figsize=(10, 6))

for xi in xi_values:
    D = amplification_factor(r, xi)
    plt.plot(r, D, label=f'xi = {xi}')

plt.axvline(1.0, color='red', linestyle='--', label='Résonance (r=1)')
plt.title('Coefficient d\'amplification dynamique D en fonction de r')
plt.xlabel('Rapport de fréquences r = Omega / omega0')
plt.ylabel('Facteur d\'amplification D')
plt.legend()
plt.grid(True)
plt.yscale('log') # Utilisation d'une échelle logarithmique pour mieux voir les pics
plt.savefig('Simulations/amplification_plot.png')
plt.show()
