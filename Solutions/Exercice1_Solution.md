# Corrigé de l'exercice 1 : Vibrations libres amorties d’un système à un degré de liberté

## 1. Contexte physique et modélisation

On considère un système mécanique élémentaire constitué d’une masse ponctuelle $m$, reliée à un bâti fixe par un ressort de raideur $k$ et un amortisseur visqueux de coefficient $c$. Le déplacement de la masse est repéré par la coordonnée $x(t)$, mesurée à partir de la position d’équilibre statique.

L’énergie cinétique du système est $T = \frac{1}{2} m \dot{x}^2$, l’énergie potentielle élastique est $V = \frac{1}{2} k x^2$, et la fonction de dissipation de Rayleigh est $D = \frac{1}{2} c \dot{x}^2$. L’application du principe fondamental de la dynamique ou de l’équation de Lagrange conduit à l’équation différentielle du mouvement :

$$
m \ddot{x} + c \dot{x} + k x = 0
\tag{1}
$$

En divisant par la masse $m$ et en introduisant les grandeurs caractéristiques suivantes :

- pulsation propre non amortie : $\omega_0 = \sqrt{\frac{k}{m}}$,
- facteur d’amortissement réduit : $\xi = \frac{c}{2 m \omega_0}$,

l’équation (1) se met sous la forme canonique :

$$
\ddot{x} + 2 \xi \omega_0 \dot{x} + \omega_0^2 x = 0
\tag{2}
$$

Le paramètre $\xi$ est adimensionnel ; sa valeur détermine qualitativement le régime vibratoire. On distingue classiquement les trois cas suivants :

- si $0 < \xi < 1$ : régime sous-amorti (oscillations amorties) ;
- si $\xi = 1$ : régime critique ;
- si $\xi > 1$ : régime sur-amorti (apériodique).

L’objectif de cet exercice est d’établir les expressions du déplacement $x(t)$ pour les deux derniers régimes, en fonction des conditions initiales $x(0) = x_0$ et $\dot{x}(0) = \dot{x}_0$.

---

## 2. Équation caractéristique et structure générale de la solution

Pour résoudre l’équation différentielle linéaire homogène (2), on cherche des solutions de la forme $x(t) = e^{r t}$. La substitution dans (2) fournit l’équation caractéristique :

$$
r^2 + 2 \xi \omega_0 r + \omega_0^2 = 0
\tag{3}
$$

Le discriminant de cette équation du second degré est :

$$
\Delta = 4 \omega_0^2 (\xi^2 - 1)
\tag{4}
$$

Les deux racines sont donc :

$$
r_{1,2} = -\xi \omega_0 \pm \omega_0 \sqrt{\xi^2 - 1}
\tag{5}
$$

La nature de ces racines dépend directement de $\xi$, ce qui justifie l’étude séparée des cas $\xi = 1$ et $\xi > 1$.

---

## 3. Régime critique ($\xi = 1$)

### 3.1. Racines de l’équation caractéristique

Lorsque $\xi = 1$, l’équation caractéristique (3) devient :

$$
r^2 + 2 \omega_0 r + \omega_0^2 = (r + \omega_0)^2 = 0
$$

Le discriminant est nul et la racine est double :

$$
r_{1,2} = -\omega_0
\tag{6}
$$

### 3.2. Forme de la solution générale

Pour une racine double $r$, la solution générale de l’équation différentielle s’écrit :

$$
x(t) = (A + B t) e^{-\omega_0 t}
\tag{7}
$$

où $A$ et $B$ sont des constantes d’intégration à déterminer à l’aide des conditions initiales.

### 3.3. Détermination des constantes

La condition initiale sur le déplacement donne, en évaluant (7) en $t = 0$ :

$$
x(0) = A = x_0
\tag{8}
$$

La vitesse s’obtient en dérivant (7) par rapport au temps :

$$
\dot{x}(t) = B e^{-\omega_0 t} - \omega_0 (A + B t) e^{-\omega_0 t}
= e^{-\omega_0 t} \bigl[ B - \omega_0 (A + B t) \bigr]
\tag{9}
$$

En $t = 0$, on a :

$$
\dot{x}(0) = B - \omega_0 A = \dot{x}_0
$$

Compte tenu de (8), on en déduit :

$$
B = \dot{x}_0 + \omega_0 x_0
\tag{10}
$$

### 3.4. Expression finale du déplacement

En reportant (8) et (10) dans (7), on obtient :

$$
x(t) = \bigl( x_0 + (\dot{x}_0 + \omega_0 x_0) t \bigr) e^{-\omega_0 t}
$$

soit, après réorganisation :

$$
\boxed{ x(t) = e^{-\omega_0 t} \bigl[ x_0 (1 + \omega_0 t) + \dot{x}_0 t \bigr] }
\tag{11}
$$

Cette expression constitue la solution pour le régime critique.

---

## 4. Régime sur-amorti ($\xi > 1$)

### 4.1. Racines et introduction de $\omega_d$

Pour $\xi > 1$, le discriminant (4) est strictement positif. Les deux racines sont réelles et distinctes. On pose :

$$
\omega_d = \omega_0 \sqrt{\xi^2 - 1} > 0
\tag{12}
$$

Les racines (5) s’écrivent alors :

$$
r_1 = -\xi \omega_0 + \omega_d, \qquad r_2 = -\xi \omega_0 - \omega_d
\tag{13}
$$

Ces deux racines sont strictement négatives, car $\xi \omega_0 > \omega_d$ (puisque $\xi > \sqrt{\xi^2 - 1}$ pour tout $\xi > 1$). La solution générale est donc :

$$
x(t) = C_1 e^{r_1 t} + C_2 e^{r_2 t}
= e^{-\xi \omega_0 t} \left( C_1 e^{\omega_d t} + C_2 e^{-\omega_d t} \right)
\tag{14}
$$

### 4.2. Réécriture à l’aide des fonctions hyperboliques

Afin de faciliter l’interprétation physique et l’application des conditions initiales, on exprime la combinaison linéaire d’exponentielles à l’aide des fonctions hyperboliques, définies par :

$$
\cosh u = \frac{e^u + e^{-u}}{2}, \qquad \sinh u = \frac{e^u - e^{-u}}{2}
\tag{15}
$$

On pose alors :

$$
x(t) = e^{-\xi \omega_0 t} \bigl( A \cosh(\omega_d t) + B \sinh(\omega_d t) \bigr)
\tag{16}
$$

Les constantes $A$ et $B$ sont reliées aux constantes $C_1$ et $C_2$ par les relations $A = C_1 + C_2$ et $B = C_1 - C_2$.

### 4.3. Détermination des constantes

La condition $x(0) = x_0$ donne, en évaluant (16) en $t = 0$ :

$$
x_0 = e^0 \bigl( A \cosh(0) + B \sinh(0) \bigr) = A
$$

d’où :

$$
A = x_0
\tag{17}
$$

Pour la vitesse, on dérive (16). On utilise les dérivées usuelles :

$$
\frac{d}{dt} \bigl( \cosh(\omega_d t) \bigr) = \omega_d \sinh(\omega_d t), \qquad
\frac{d}{dt} \bigl( \sinh(\omega_d t) \bigr) = \omega_d \cosh(\omega_d t)
$$

On obtient :

$$
\begin{aligned}
\dot{x}(t) &= -\xi \omega_0 e^{-\xi \omega_0 t} \bigl( A \cosh(\omega_d t) + B \sinh(\omega_d t) \bigr) \\
&\quad + e^{-\xi \omega_0 t} \bigl( A \omega_d \sinh(\omega_d t) + B \omega_d \cosh(\omega_d t) \bigr) \\
&= e^{-\xi \omega_0 t} \Bigl[ (-\xi \omega_0 A + \omega_d B) \cosh(\omega_d t) + (-\xi \omega_0 B + \omega_d A) \sinh(\omega_d t) \Bigr]
\end{aligned}
\tag{18}
$$

En évaluant (18) en $t = 0$, il vient :

$$
\dot{x}(0) = -\xi \omega_0 A + \omega_d B = \dot{x}_0
$$

En substituant $A = x_0$, on trouve :

$$
\omega_d B = \dot{x}_0 + \xi \omega_0 x_0
$$

d’où :

$$
B = \frac{\dot{x}_0 + \xi \omega_0 x_0}{\omega_d}
\tag{19}
$$

### 4.4. Expression finale du déplacement

En reportant (17) et (19) dans (16), on obtient la solution pour le régime sur-amorti :

$$
\boxed{ x(t) = e^{-\xi \omega_0 t} \left[ x_0 \cosh(\omega_d t) + \frac{\dot{x}_0 + \xi \omega_0 x_0}{\omega_d} \sinh(\omega_d t) \right] }
\tag{20}
$$

où $\omega_d = \omega_0 \sqrt{\xi^2 - 1}$.

---

## 5. Commentaires physiques et mathématiques

### 5.1. Comparaison des deux régimes

Dans les deux cas, le terme exponentiel $e^{-\alpha t}$ (avec $\alpha = \omega_0$ pour le cas critique et $\alpha = \xi \omega_0$ pour le cas sur-amorti) assure la décroissance vers zéro lorsque $t \to +\infty$. Le système ne présente aucune oscillation, ce qui distingue ces régimes du cas sous-amorti.

Dans le régime critique, l’absence d’oscillation est associée à une racine double. Mathématiquement, la présence du facteur $(1 + \omega_0 t)$ dans (11) est la signature de cette dégénérescence. Physiquement, l’amortissement critique réalise le retour le plus rapide à la position d’équilibre sans dépassement.

Dans le régime sur-amorti, les deux racines réelles négatives correspondent à deux modes de décroissance exponentielle. Le mode le plus lent (associé à $r_1 = -\xi \omega_0 + \omega_d$) domine aux temps longs. Lorsque $\xi$ augmente, $\omega_d$ se rapproche de $\xi \omega_0$, et le terme dominant $e^{(-\xi \omega_0 + \omega_d)t}$ décroît d’autant plus lentement. Ainsi, un amortissement excessif ralentit paradoxalement le retour à l’équilibre.

### 5.2. Cas particuliers

Les expressions (11) et (20) se simplifient dans deux cas limites fréquents.

- **Déplacement initial non nul, vitesse initiale nulle** ($\dot{x}_0 = 0$). Pour le régime critique :

$$
x(t) = x_0 (1 + \omega_0 t) e^{-\omega_0 t}
$$

Pour le régime sur-amorti :

$$
x(t) = x_0 e^{-\xi \omega_0 t} \left[ \cosh(\omega_d t) + \frac{\xi \omega_0}{\omega_d} \sinh(\omega_d t) \right]
$$

- **Déplacement initial nul, vitesse initiale non nulle** ($x_0 = 0$). Pour le régime critique :

$$
x(t) = \dot{x}_0 t e^{-\omega_0 t}
$$

Pour le régime sur-amorti :

$$
x(t) = \frac{\dot{x}_0}{\omega_d} e^{-\xi \omega_0 t} \sinh(\omega_d t)
$$

### 5.3. Lien entre les deux formulations (exponentielle et hyperbolique)

La formulation hyperbolique (20) est strictement équivalente à la formulation exponentielle (14). En effet, en développant (20) à l’aide des définitions (15), on retrouve :

$$
x(t) = \frac{1}{2} \left( x_0 + \frac{\dot{x}_0 + \xi \omega_0 x_0}{\omega_d} \right) e^{(-\xi \omega_0 + \omega_d)t}
+ \frac{1}{2} \left( x_0 - \frac{\dot{x}_0 + \xi \omega_0 x_0}{\omega_d} \right) e^{(-\xi \omega_0 - \omega_d)t}
$$

Cette écriture fait apparaître explicitement les deux constantes d’intégration $C_1$ et $C_2$.

---

## 6. Représentations graphiques

Afin de visualiser les différences qualitatives entre les régimes, on peut superposer les réponses $x(t)$ pour les trois cas ($0 < \xi < 1$, $\xi = 1$ et $\xi > 1$), pour des conditions initiales identiques, par exemple $x_0 > 0$ et $\dot{x}_0 = 0$.

[Figure 1 : Évolution temporelle du déplacement pour les trois régimes d’amortissement (../Figures/Ex1Sol.png).]
Description sommaire : la courbe correspondant à $\xi < 1$ présente des oscillations d’amplitude décroissante ; la courbe $\xi = 1$ décroît rapidement sans oscillation ; la courbe $\xi > 1$ décroît plus lentement que la précédente et ne présente pas non plus d’oscillation.


