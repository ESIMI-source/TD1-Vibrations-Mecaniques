# Solution de l'Exercice 4

Cet exercice modélise un bâtiment comme un système à un degré de liberté (1DDL) et demande de déterminer plusieurs paramètres vibratoires à partir de données expérimentales.

**Données fournies :**
*   Force latérale $P = 10 \text{ T}$ (tonnes) = $10 \times 1000 \text{ kg} \times 9.81 \text{ m/s}^2 = 98100 \text{ N}$ (en supposant $g \approx 9.81 \text{ m/s}^2$)
*   Déplacement horizontal statique $x_{st} = 3 \text{ cm} = 0.03 \text{ m}$
*   Après 3 cycles complets, le temps est de $1 \text{ s}$ et l'amplitude est de $1 \text{ cm} = 0.01 \text{ m}$

## 1. Détermination de la période pseudo-périodique $T_D$

On nous dit qu'après 3 cycles complets, le temps est de $1 \text{ s}$.

La période pseudo-périodique $T_D$ est le temps pour un cycle complet.

$$T_D = \frac{\text{Temps total}}{\text{Nombre de cycles}} = \frac{1 \text{ s}}{3 \text{ cycles}} = \frac{1}{3} \text{ s} \approx 0.333 \text{ s}$$

## 2. Détermination du Taux d'amortissement $\xi$

Nous avons l'amplitude après 3 cycles ($x_3 = 1 \text{ cm}$) et nous pouvons déduire l'amplitude initiale $x_0$ à partir du déplacement statique et de la nature de l'excitation. Cependant, l'énoncé indique que le câble d'attache est coupé, ce qui suggère une vibration libre amortie. Le déplacement statique de 3 cm est le déplacement initial avant que le câble ne soit coupé et que le système ne commence à vibrer librement. Donc, $x_0 = 3 \text{ cm}$.

Pour un système en vibration libre amortie, le rapport des amplitudes successives est donné par le décrément logarithmique $\delta$ :

$$\frac{x_n}{x_{n+N}} = e^{N \delta}$$

Où $N$ est le nombre de cycles entre les amplitudes $x_n$ et $x_{n+N}$.

Ici, nous avons $x_0 = 3 \text{ cm}$ et $x_3 = 1 \text{ cm}$ (après 3 cycles, donc $N=3$).

$$\frac{x_0}{x_3} = e^{3 \delta}$$

$$\frac{3}{1} = e^{3 \delta} \implies 3 = e^{3 \delta}$$

Prendre le logarithme naturel des deux côtés :

$$\ln(3) = 3 \delta \implies \delta = \frac{\ln(3)}{3} \approx \frac{1.0986}{3} \approx 0.3662$$

Le décrément logarithmique $\delta$ est également lié au taux d'amortissement $\xi$ par la relation :

$$\delta = \frac{2\pi \xi}{\sqrt{1 - \xi^2}}$$

Pour de faibles amortissements (ce qui est souvent le cas pour les bâtiments), $\sqrt{1 - \xi^2} \approx 1$, donc $\delta \approx 2\pi \xi$.

En utilisant l'approximation pour de faibles amortissements :

$$\xi \approx \frac{\delta}{2\pi} = \frac{0.3662}{2\pi} \approx 0.0583$$

Pour une solution plus précise, nous devons résoudre l'équation complète :

$$0.3662 = \frac{2\pi \xi}{\sqrt{1 - \xi^2}}$$

Élevons au carré les deux côtés :

$$(0.3662)^2 = \frac{(2\pi \xi)^2}{1 - \xi^2}$$

$$0.1341 = \frac{39.4784 \xi^2}{1 - \xi^2}$$

$$0.1341 (1 - \xi^2) = 39.4784 \xi^2$$

$$0.1341 - 0.1341 \xi^2 = 39.4784 \xi^2$$

$$0.1341 = (39.4784 + 0.1341) \xi^2$$

$$0.1341 = 39.6125 \xi^2$$

$$\xi^2 = \frac{0.1341}{39.6125} \approx 0.003385$$

$$\xi = \sqrt{0.003385} \approx 0.05818$$

Le taux d'amortissement est $\xi \approx 0.0582$.

## 3. Détermination de la période propre du bâtiment $T_0$

La période pseudo-périodique $T_D$ est liée à la période propre non amortie $T_0$ par la relation :

$$T_D = \frac{T_0}{\sqrt{1 - \xi^2}}$$

Nous avons $T_D = 1/3 \text{ s}$ et $\xi \approx 0.05818$.

$$T_0 = T_D \sqrt{1 - \xi^2} = \frac{1}{3} \sqrt{1 - (0.05818)^2}$$

$$T_0 = \frac{1}{3} \sqrt{1 - 0.003385} = \frac{1}{3} \sqrt{0.996615}$$

$$T_0 = \frac{1}{3} \times 0.9983 \approx 0.3327 \text{ s}$$

## 4. Détermination de la Pulsation propre du bâtiment $\omega_0$

La pulsation propre $\omega_0$ est liée à la période propre $T_0$ par la relation :

$$\omega_0 = \frac{2\pi}{T_0}$$

$$\omega_0 = \frac{2\pi}{0.3327} \approx 18.88 \text{ rad/s}$$

## 5. Détermination de la rigidité $K$

La rigidité $K$ peut être déterminée à partir du déplacement statique $x_{st}$ et de la force statique $P$ :

$$K = \frac{P}{x_{st}}$$

$$K = \frac{98100 \text{ N}}{0.03 \text{ m}} = 3270000 \text{ N/m}$$

## 6. Détermination de la masse du bâtiment $M$

La masse $M$ peut être déterminée à partir de la rigidité $K$ et de la pulsation propre $\omega_0$ :

$$\omega_0 = \sqrt{\frac{K}{M}} \implies \omega_0^2 = \frac{K}{M} \implies M = \frac{K}{\omega_0^2}$$

$$M = \frac{3270000 \text{ N/m}}{(18.88 \text{ rad/s})^2} = \frac{3270000}{356.4544} \approx 9173.6 \text{ kg}$$

**Résumé des résultats :**
*   $T_D \approx 0.333 \text{ s}$
*   $\xi \approx 0.0582$
*   $T_0 \approx 0.3327 \text{ s}$
*   $\omega_0 \approx 18.88 \text{ rad/s}$
*   $K = 3.27 \times 10^6 \text{ N/m}$
*   $M \approx 9173.6 \text{ kg}$
