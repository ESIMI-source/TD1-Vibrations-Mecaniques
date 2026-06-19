# Rappels Théoriques sur les Vibrations Mécaniques

Ce document regroupe les concepts fondamentaux et les équations clés nécessaires à la résolution des exercices de vibrations mécaniques.

## 1. Système à un Degré de Liberté (1DDL)

Un système à un degré de liberté est un système dont la configuration peut être décrite par une seule coordonnée généralisée. L'équation générale du mouvement pour un système 1DDL est :

$$m\ddot{x} + c\dot{x} + kx = F(t)$$

Où :
*   $m$ est la masse du système.
*   $c$ est le coefficient d'amortissement visqueux.
*   $k$ est la rigidité du système.
*   $x$ est le déplacement.
*   $F(t)$ est la force externe appliquée.

## 2. Vibrations Libres Non Amorties

Lorsque $c=0$ et $F(t)=0$, l'équation du mouvement devient :

$$m\ddot{x} + kx = 0$$

La solution est de la forme $x(t) = A \cos(\omega_0 t - \phi)$, où $\omega_0$ est la pulsation propre non amortie, donnée par :

$$\omega_0 = \sqrt{\frac{k}{m}}$$

La période propre $T_0$ est $T_0 = \frac{2\pi}{\omega_0}$.

## 3. Vibrations Libres Amorties

Lorsque $F(t)=0$, l'équation du mouvement est :

$$m\ddot{x} + c\dot{x} + kx = 0$$

Pour analyser ce système, on introduit :

*   Le **taux d'amortissement** $\xi$ :
    $$\xi = \frac{c}{c_c} = \frac{c}{2m\omega_0} = \frac{c}{2\sqrt{mk}}$$
    Où $c_c = 2m\omega_0$ est l'amortissement critique.

*   La **pulsation propre non amortie** $\omega_0 = \sqrt{\frac{k}{m}}$.

La nature de la réponse dépend de la valeur de $\xi$ :

### a. Amortissement Faible (Sous-amorti) : $\xi < 1$

La solution est de la forme :

$$x(t) = e^{-\xi \omega_0 t} (A \cos(\omega_d t) + B \sin(\omega_d t))$$

Où $\omega_d$ est la **pulsation pseudo-périodique** :

$$\omega_d = \omega_0 \sqrt{1 - \xi^2}$$

La période pseudo-périodique $T_d = \frac{2\pi}{\omega_d}$.

### b. Amortissement Critique : $\xi = 1$

La solution est de la forme :

$$x(t) = (A + Bt) e^{-\omega_0 t}$$

Avec les conditions initiales $x(0) = x_0$ et $\dot{x}(0) = \dot{x}_0$, on obtient :

$$x(t) = e^{-\omega_0 t} [x_0 (1 + \omega_0 t) + \dot{x}_0 t]$$

### c. Amortissement Fort (Sur-amorti) : $\xi > 1$

La solution est de la forme :

$$x(t) = e^{-\xi \omega_0 t} (A e^{\omega_d t} + B e^{-\omega_d t})$$

Où $\omega_d = \omega_0 \sqrt{\xi^2 - 1}$.

Avec les conditions initiales $x(0) = x_0$ et $\dot{x}(0) = \dot{x}_0$, on obtient :

$$x(t) = e^{-\xi \omega_0 t} [x_0 \cosh(\omega_d t) + \frac{\dot{x}_0 + x_0 \xi \omega_0}{\omega_d} \sinh(\omega_d t)]$$

## 4. Vibrations Forcées

Lorsque $F(t) \neq 0$, le système est soumis à une excitation externe. La solution générale est la somme de la solution homogène (transitoire) et de la solution particulière (régime permanent).

### a. Force Harmonique

Si $F(t) = F_0 \sin(\Omega t)$, la réponse en régime permanent est de la forme $x_p(t) = X \sin(\Omega t - \phi)$.

Le **coefficient d'amplification dynamique** $D$ est défini comme :

$$D = \frac{X}{x_{st}} = \frac{1}{\sqrt{(1 - r^2)^2 + (2\xi r)^2}}$$

Où $x_{st} = F_0/k$ est le déplacement statique et $r = \Omega/\omega_0$ est le rapport de fréquences.

### b. Force Périodique Générale (Séries de Fourier)

Pour une force périodique $F(t)$ de période $T$, on peut la décomposer en série de Fourier :

$$F(t) = a_0 + \sum_{n=1}^{\infty} (a_n \cos(n\Omega t) + b_n \sin(n\Omega t))$$

Où $\Omega = 2\pi/T$ est la pulsation fondamentale. La réponse du système est alors la somme des réponses à chaque composante harmonique.

La résonance se produit lorsque la fréquence d'une composante de la force externe est proche de la pulsation propre du système.
