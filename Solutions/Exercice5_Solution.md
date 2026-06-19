# Solution de l'Exercice 5

Cet exercice consiste à analyser le comportement vibratoire d'un bâtiment modélisé comme un système à un degré de liberté (1DDL) soumis à une excitation harmonique.

**Données fournies :**
*   Masse $M = 10000 \text{ Kg}$
*   Rigidité $K = 90000 \text{ N/m}$
*   Coefficient d’amortissement $c = 3000 \text{ N.s/m}$
*   Charge latérale $p(t) = 1000 \sin(3t)$

## 1. Détermination de la Pulsation propre du bâtiment $\omega_0$

La pulsation propre non amortie $\omega_0$ est donnée par la relation :

$$\omega_0 = \sqrt{\frac{K}{M}}$$

En substituant les valeurs données :

$$\omega_0 = \sqrt{\frac{90000 \text{ N/m}}{10000 \text{ Kg}}} = \sqrt{9} = 3 \text{ rad/s}$$

## 2. Détermination du Taux d'amortissement $\xi$

Le taux d'amortissement $\xi$ est défini comme le rapport entre le coefficient d'amortissement $c$ et le coefficient d'amortissement critique $c_c$. Le coefficient d'amortissement critique est $c_c = 2M\omega_0$.

$$\xi = \frac{c}{2M\omega_0}$$

En substituant les valeurs :

$$\xi = \frac{3000 \text{ N.s/m}}{2 \times 10000 \text{ Kg} \times 3 \text{ rad/s}} = \frac{3000}{60000} = 0.05$$

Le taux d'amortissement est de $0.05$, ce qui indique un système sous-amorti ($\xi < 1$).

## 3. Détermination de la Pulsation pseudo-périodique du bâtiment $\omega_d$

Pour un système sous-amorti, la pulsation pseudo-périodique $\omega_d$ est donnée par :

$$\omega_d = \omega_0 \sqrt{1 - \xi^2}$$

En substituant les valeurs de $\omega_0$ et $\xi$ :

$$\omega_d = 3 \text{ rad/s} \times \sqrt{1 - (0.05)^2} = 3 \sqrt{1 - 0.0025} = 3 \sqrt{0.9975} \approx 3 \times 0.99875 \approx 2.99625 \text{ rad/s}$$

## 4. Détermination du Coefficient d’amplification dynamique $D$

La force d'excitation est $p(t) = 1000 \sin(3t)$, donc la pulsation d'excitation est $\Omega = 3 \text{ rad/s}$.

Le rapport de fréquences $r$ est :

$$r = \frac{\Omega}{\omega_0} = \frac{3 \text{ rad/s}}{3 \text{ rad/s}} = 1$$

Le coefficient d'amplification dynamique $D$ est donné par :

$$D = \frac{1}{\sqrt{(1 - r^2)^2 + (2\xi r)^2}}$$

En substituant les valeurs de $r$ et $\xi$ :

$$D = \frac{1}{\sqrt{(1 - 1^2)^2 + (2 \times 0.05 \times 1)^2}} = \frac{1}{\sqrt{(0)^2 + (0.1)^2}} = \frac{1}{\sqrt{0.01}} = \frac{1}{0.1} = 10$$

Le coefficient d'amplification dynamique est $D = 10$.

## 5. Déplacement statique et le déplacement dynamique. Interpréter le résultat trouvé ?

### a. Déplacement statique ($x_{st}$)

Le déplacement statique est le déplacement que le système subirait si la force d'excitation était appliquée statiquement. L'amplitude de la force est $F_0 = 1000 \text{ N}$.

$$x_{st} = \frac{F_0}{K}$$

$$x_{st} = \frac{1000 \text{ N}}{90000 \text{ N/m}} \approx 0.01111 \text{ m} = 1.111 \text{ cm}$$

### b. Déplacement dynamique ($X$)

Le déplacement dynamique (amplitude de la réponse en régime permanent) est le produit du déplacement statique et du coefficient d'amplification dynamique :

$$X = D \times x_{st}$$

$$X = 10 \times 0.01111 \text{ m} = 0.1111 \text{ m} = 11.11 \text{ cm}$$

### c. Interprétation du résultat

Nous constatons que la pulsation d'excitation $\Omega = 3 \text{ rad/s}$ est égale à la pulsation propre non amortie du bâtiment $\omega_0 = 3 \text{ rad/s}$. Cette condition correspond à la **résonance**.

En régime de résonance, même avec un amortissement relativement faible ($\xi = 0.05$), le coefficient d'amplification dynamique est très élevé ($D=10$). Cela signifie que l'amplitude du déplacement dynamique ($11.11 \text{ cm}$) est dix fois supérieure au déplacement statique ($1.111 \text{ cm}$). Une telle amplification peut entraîner des contraintes et des déformations importantes dans la structure, potentiellement dangereuses pour l'intégrité du bâtiment. Ce résultat souligne l'importance de concevoir des structures de manière à éviter que leurs fréquences propres ne coïncident avec les fréquences des excitations externes prévues.
