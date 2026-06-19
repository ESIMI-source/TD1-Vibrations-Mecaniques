# Solution de l'Exercice 2

Cet exercice demande de déterminer la fréquence propre d'une masse $M$ suspendue à une structure de rigidité de flexion $EI$ et de longueur $L$, supposée sans masse et sur appuis simples.

Pour déterminer la fréquence propre $\omega_0$, nous avons besoin de la rigidité équivalente $k$ de la structure. La fréquence propre est donnée par la formule :

$$\omega_0 = \sqrt{\frac{k}{M}}$$

La rigidité $k$ est définie comme la force nécessaire pour produire un déplacement unitaire. Dans ce cas, la structure est une poutre sur appuis simples avec une charge concentrée au centre (où la masse $M$ est suspendue).

## 1. Déplacement d'une poutre sur appuis simples avec charge centrale

Pour une poutre sur appuis simples de longueur $L$ soumise à une charge concentrée $F$ en son milieu, le déplacement maximal (flèche) au centre est donné par la formule de la mécanique des matériaux :

$$\delta = \frac{F L^3}{48 EI}$$

Où :
*   $F$ est la force appliquée (dans notre cas, la force due à la masse $M$).
*   $L$ est la longueur de la poutre.
*   $E$ est le module d'Young du matériau de la poutre.
*   $I$ est le moment d'inertie de la section transversale de la poutre.

## 2. Détermination de la rigidité équivalente $k$

La rigidité $k$ est définie comme $k = \frac{F}{\delta}$. En utilisant l'expression du déplacement $\delta$ :

$$k = \frac{F}{\frac{F L^3}{48 EI}} = \frac{48 EI}{L^3}$$

Cette rigidité représente la raideur de la structure au point où la masse est attachée.

## 3. Calcul de la fréquence propre $\omega_0$

Maintenant que nous avons la rigidité équivalente $k$, nous pouvons calculer la pulsation propre $\omega_0$ du système masse-structure :

$$\omega_0 = \sqrt{\frac{k}{M}} = \sqrt{\frac{48 EI}{M L^3}}$$

La fréquence propre $f_0$ est alors :

$$f_0 = \frac{\omega_0}{2\pi} = \frac{1}{2\pi} \sqrt{\frac{48 EI}{M L^3}}$$

Cette formule permet de déterminer la fréquence propre du système. Il est important de noter que cette dérivation suppose que la masse de la poutre est négligeable par rapport à la masse $M$, comme spécifié dans l'énoncé.
