# Solution de l'Exercice 1

Cet exercice demande de démontrer les expressions du déplacement pour un système à un degré de liberté (1DDL) en vibrations libres amorties, spécifiquement pour les cas d'amortissement critique ($\xi = 1$) et sur-amorti ($\xi > 1$), en fonction des conditions initiales $x(0) = x_0$ et $\dot{x}(0) = \dot{x}_0$.

L'équation différentielle du mouvement pour un système 1DDL en vibrations libres amorties est :

$$m\ddot{x} + c\dot{x} + kx = 0$$

En divisant par la masse $m$ et en introduisant la pulsation propre non amortie $\omega_0 = \sqrt{k/m}$ et le taux d'amortissement $\xi = c/(2m\omega_0)$, l'équation devient :

$$\ddot{x} + 2\xi \omega_0 \dot{x} + \omega_0^2 x = 0$$

La solution de cette équation dépend de la valeur du taux d'amortissement $\xi$.

## Cas 1 : Amortissement Critique ($\xi = 1$)

Lorsque le système est à amortissement critique, le taux d'amortissement $\xi = 1$. L'équation caractéristique de l'équation différentielle est :

$$r^2 + 2\omega_0 r + \omega_0^2 = 0$$

Cette équation a une racine réelle double : $r_{1,2} = -\omega_0$.

La solution générale du déplacement $x(t)$ est alors de la forme :

$$x(t) = (A + Bt) e^{-\omega_0 t}$$

Pour déterminer les constantes $A$ et $B$, nous utilisons les conditions initiales :

1.  **Déplacement initial** : $x(0) = x_0$
    En substituant $t=0$ dans l'expression de $x(t)$ :
    $$x_0 = (A + B \cdot 0) e^{-\omega_0 \cdot 0} \implies x_0 = A$$
    Donc, $A = x_0$.

2.  **Vitesse initiale** : $\dot{x}(0) = \dot{x}_0$
    D'abord, dérivons $x(t)$ par rapport au temps $t$ :
    $$\dot{x}(t) = B e^{-\omega_0 t} - \omega_0 (A + Bt) e^{-\omega_0 t}$$
    $$\dot{x}(t) = e^{-\omega_0 t} [B - \omega_0 (A + Bt)]$$
    En substituant $t=0$ :
    $$\dot{x}_0 = e^0 [B - \omega_0 (A + B \cdot 0)] \implies \dot{x}_0 = B - \omega_0 A$$
    En substituant $A = x_0$ :
    $$\dot{x}_0 = B - \omega_0 x_0 \implies B = \dot{x}_0 + \omega_0 x_0$$

En substituant les valeurs de $A$ et $B$ dans la solution générale :

$$x(t) = (x_0 + (\dot{x}_0 + \omega_0 x_0)t) e^{-\omega_0 t}$$

En réarrangeant les termes :

$$x(t) = e^{-\omega_0 t} [x_0 + \dot{x}_0 t + \omega_0 x_0 t]$$

$$x(t) = e^{-\omega_0 t} [x_0 (1 + \omega_0 t) + \dot{x}_0 t]$$

Ceci démontre la première expression.

## Cas 2 : Amortissement Sur-amorti ($\xi > 1$)

Lorsque le système est sur-amorti, le taux d'amortissement $\xi > 1$. L'équation caractéristique $r^2 + 2\xi \omega_0 r + \omega_0^2 = 0$ a deux racines réelles distinctes :

$$r_{1,2} = -\xi \omega_0 \pm \omega_0 \sqrt{\xi^2 - 1}$$

Pour simplifier, on définit la pulsation $\omega_d = \omega_0 \sqrt{\xi^2 - 1}$. Notez que cette $\omega_d$ est réelle pour $\xi > 1$.

Donc, les racines sont $r_{1,2} = -\xi \omega_0 \pm \omega_d$.

La solution générale du déplacement $x(t)$ est alors de la forme :

$$x(t) = C_1 e^{(-\xi \omega_0 + \omega_d)t} + C_2 e^{(-\xi \omega_0 - \omega_d)t}$$

Cette expression peut être réécrite en utilisant les fonctions hyperboliques $\cosh(u) = (e^u + e^{-u})/2$ et $\sinh(u) = (e^u - e^{-u})/2$ :

$$x(t) = e^{-\xi \omega_0 t} (A \cosh(\omega_d t) + B \sinh(\omega_d t))$$

Pour déterminer les constantes $A$ et $B$, nous utilisons les conditions initiales :

1.  **Déplacement initial** : $x(0) = x_0$
    En substituant $t=0$ dans l'expression de $x(t)$ :
    $$x_0 = e^0 (A \cosh(0) + B \sinh(0)) \implies x_0 = A \cdot 1 + B \cdot 0 \implies x_0 = A$$
    Donc, $A = x_0$.

2.  **Vitesse initiale** : $\dot{x}(0) = \dot{x}_0$
    D'abord, dérivons $x(t)$ par rapport au temps $t$ :
    $$\dot{x}(t) = -\xi \omega_0 e^{-\xi \omega_0 t} (A \cosh(\omega_d t) + B \sinh(\omega_d t)) + e^{-\xi \omega_0 t} (A \omega_d \sinh(\omega_d t) + B \omega_d \cosh(\omega_d t))$$
    $$\dot{x}(t) = e^{-\xi \omega_0 t} [-\xi \omega_0 (A \cosh(\omega_d t) + B \sinh(\omega_d t)) + A \omega_d \sinh(\omega_d t) + B \omega_d \cosh(\omega_d t)]$$
    En substituant $t=0$ :
    $$\dot{x}_0 = e^0 [-\xi \omega_0 (A \cosh(0) + B \sinh(0)) + A \omega_d \sinh(0) + B \omega_d \cosh(0)]$$
    $$\dot{x}_0 = [-\xi \omega_0 (A \cdot 1 + B \cdot 0) + A \omega_d \cdot 0 + B \omega_d \cdot 1]$$
    $$\dot{x}_0 = -\xi \omega_0 A + B \omega_d$$
    En substituant $A = x_0$ :
    $$\dot{x}_0 = -\xi \omega_0 x_0 + B \omega_d$$
    $$\dot{x}_0 + \xi \omega_0 x_0 = B \omega_d$$
    $$B = \frac{\dot{x}_0 + \xi \omega_0 x_0}{\omega_d}$$

En substituant les valeurs de $A$ et $B$ dans la solution générale :

$$x(t) = e^{-\xi \omega_0 t} [x_0 \cosh(\omega_d t) + \frac{\dot{x}_0 + \xi \omega_0 x_0}{\omega_d} \sinh(\omega_d t)]$$

Ceci démontre la deuxième expression. Il est important de noter que la pulsation $\omega_d$ est ici définie comme $\omega_d = \omega_0 \sqrt{\xi^2 - 1}$ pour le cas sur-amorti, ce qui est différent de la pulsation pseudo-périodique pour le cas sous-amorti (où $\omega_d = \omega_0 \sqrt{1 - \xi^2}$).
