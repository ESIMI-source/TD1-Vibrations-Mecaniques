# Solution de l'Exercice 3

Cet exercice concerne un système non amorti soumis à une force périodique impaire $p(t)$, représentée sur la figure 2 du TD. Nous devons utiliser les séries de Fourier pour déterminer la réponse en régime permanent et étudier les possibilités de résonance.

L'équation du mouvement pour un système non amorti à 1DDL est :

$$m\ddot{x} + kx = p(t)$$

Ou, en divisant par $m$ et en utilisant $\omega_0^2 = k/m$ :

$$\ddot{x} + \omega_0^2 x = \frac{p(t)}{m}$$

## 1. Décomposition de la force $p(t)$ en série de Fourier

La force $p(t)$ est une fonction périodique impaire. Pour une fonction impaire, les coefficients $a_n$ de la série de Fourier sont nuls, et la série ne contient que des termes en sinus :

$$p(t) = \sum_{n=1}^{\infty} b_n \sin(n\Omega t)$$

Où $\Omega = 2\pi/T$ est la pulsation fondamentale et $T$ est la période de $p(t)$. D'après la figure 2, la période $T$ est $2T_0$ (où $T_0$ est la demi-période de la force carrée). Donc $\Omega = 2\pi/(2T_0) = \pi/T_0$.

Les coefficients $b_n$ sont donnés par :

$$b_n = \frac{2}{T} \int_{0}^{T} p(t) \sin(n\Omega t) dt$$

Pour la fonction $p(t)$ donnée (une onde carrée impaire) :
*   $p(t) = P_0$ pour $0 < t < T/2$
*   $p(t) = -P_0$ pour $T/2 < t < T$

En considérant la période $T = 2T_0$ :

$$b_n = \frac{2}{2T_0} \left[ \int_{0}^{T_0} P_0 \sin(n\frac{\pi}{T_0} t) dt + \int_{T_0}^{2T_0} (-P_0) \sin(n\frac{\pi}{T_0} t) dt \right]$$

$$b_n = \frac{P_0}{T_0} \left[ \left[ -\frac{T_0}{n\pi} \cos(n\frac{\pi}{T_0} t) \right]_{0}^{T_0} - \left[ -\frac{T_0}{n\pi} \cos(n\frac{\pi}{T_0} t) \right]_{T_0}^{2T_0} \right]$$

$$b_n = \frac{P_0}{T_0} \frac{T_0}{n\pi} \left[ -(\cos(n\pi) - \cos(0)) + (\cos(2n\pi) - \cos(n\pi)) \right]$$

$$b_n = \frac{P_0}{n\pi} \left[ -\cos(n\pi) + 1 + 1 - \cos(n\pi) \right]$$

$$b_n = \frac{P_0}{n\pi} [2 - 2\cos(n\pi)]$$

On sait que $\cos(n\pi) = (-1)^n$. Donc :

$$b_n = \frac{2P_0}{n\pi} [1 - (-1)^n]$$

*   Si $n$ est pair, $1 - (-1)^n = 1 - 1 = 0$, donc $b_n = 0$.
*   Si $n$ est impair, $1 - (-1)^n = 1 - (-1) = 2$, donc $b_n = \frac{4P_0}{n\pi}$.

Par conséquent, la série de Fourier pour $p(t)$ est :

$$p(t) = \sum_{n=1,3,5,...}^{\infty} \frac{4P_0}{n\pi} \sin(n\Omega t)$$

## 2. Réponse du système en régime permanent

Pour chaque composante harmonique de la force $p(t)$, la réponse en régime permanent $x_n(t)$ est donnée par :

$$x_n(t) = X_n \sin(n\Omega t)$$

Où $X_n$ est l'amplitude de la réponse pour la $n$-ième harmonique. Pour un système non amorti, l'amplitude est :

$$X_n = \frac{b_n/m}{\omega_0^2 - (n\Omega)^2}$$

En substituant $b_n$ :

$$X_n = \frac{4P_0/(n\pi m)}{\omega_0^2 - (n\Omega)^2}$$

La réponse totale en régime permanent est la somme de toutes les réponses harmoniques :

$$x(t) = \sum_{n=1,3,5,...}^{\infty} \frac{4P_0/(n\pi m)}{\omega_0^2 - (n\Omega)^2} \sin(n\Omega t)$$

## 3. Possibilités de résonance

La résonance se produit lorsque le dénominateur de l'amplitude $X_n$ s'approche de zéro, c'est-à-dire lorsque la pulsation d'une composante de la force externe est égale à la pulsation propre du système :

$$\omega_0^2 - (n\Omega)^2 = 0 \implies \omega_0 = n\Omega$$

En d'autres termes, la résonance se produit si la pulsation propre du système $\omega_0$ est égale à une harmonique impaire de la pulsation fondamentale de la force excitatrice $n\Omega$ (où $n=1, 3, 5, ...$).

Si $\omega_0 = \Omega$, il y aura résonance avec la première harmonique de la force.
Si $\omega_0 = 3\Omega$, il y aura résonance avec la troisième harmonique de la force, et ainsi de suite.

Dans ces cas, l'amplitude de la réponse tendra vers l'infini (pour un système non amorti), ce qui est une situation dangereuse en ingénierie. Pour un système amorti, l'amplitude serait grande mais finie.
