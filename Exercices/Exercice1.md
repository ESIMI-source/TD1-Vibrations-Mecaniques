# Exercice 1

Démontrer que le déplacement d’un système à amortissement critique et sur amorti avec déplacement initial $x_0$ et vitesse initiale $\dot{x}_0$ est donné par :

*   Pour $\xi = 1$ (amortissement critique) :
    $$x(t) = e^{-\omega_0 t} [x_0 (1 + \omega_0 t) + \dot{x}_0 t]$$

*   Pour $\xi > 1$ (amortissement sur-amorti) :
    $$x(t) = e^{-\xi \omega_0 t} [x_0 \cosh(\omega_d t) + \frac{\dot{x}_0 + x_0 \xi \omega_0}{\omega_d} \sinh(\omega_d t)]$$

Où $\omega_d = \omega_0 \sqrt{\xi^2 - 1}$ est la pulsation ou fréquence pseudo-périodique, et $\omega_0$ est la pulsation ou fréquence naturelle du système libre non amorti.
