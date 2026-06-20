# Exercice 1 — Vibrations libres amorties d’un système à un degré de liberté

## 1. Mise en équation et paramètres caractéristiques

On considère un système mécanique élémentaire constitué d’une masse $`m`$, d’un ressort de raideur $`k`$ et d’un amortisseur visqueux de coefficient $`c`$. Le déplacement de la masse, repéré par rapport à sa position d’équilibre statique, est noté $`x(t)`$.

L’équation différentielle du mouvement, obtenue par application du principe fondamental de la dynamique, s’écrit :

```math
m\ddot{x} + c\dot{x} + kx = 0
```

On introduit la pulsation propre non amortie $`\omega_0 = \sqrt{k/m}`$ et le facteur d’amortissement réduit $`\xi = \dfrac{c}{2m\omega_0}`$. L’équation précédente se réduit alors à la forme canonique :

```math
\ddot{x} + 2\xi\omega_0\dot{x} + \omega_0^2 x = 0
```

Le paramètre $`\xi`$ est adimensionnel. Sa valeur détermine la nature du régime vibratoire. On distingue :

- $`0 < \xi < 1`$ : régime sous-amorti ;
- $`\xi = 1`$ : régime critique ;
- $`\xi > 1`$ : régime sur-amorti.

## 2. Résolution par l’équation caractéristique

La solution de l’équation différentielle est cherchée sous la forme exponentielle :

```math
x(t) = e^{rt}
```

En substituant cette expression dans l’équation canonique, on obtient l’équation caractéristique :

```math
r^2 + 2\xi\omega_0 r + \omega_0^2 = 0
```

Le discriminant associé vaut :

```math
\Delta = 4\omega_0^2(\xi^2 - 1)
```

Les racines sont donc :

```math
r_{1,2} = -\xi\omega_0 \pm \omega_0\sqrt{\xi^2 - 1}
```

La nature de ces racines dépend du signe de $`\xi^2 - 1`$ :

- si $`0 < \xi < 1`$, les racines sont complexes conjuguées ;
- si $`\xi = 1`$, elles sont réelles et doubles ;
- si $`\xi > 1`$, elles sont réelles et distinctes.

## 3. Régime sous-amorti

Dans le cas $`0 < \xi < 1`$, le mouvement reste oscillatoire mais son amplitude décroît avec le temps. On introduit la pseudo-pulsation :

```math
\omega_d = \omega_0\sqrt{1-\xi^2}
```

La solution générale s’écrit alors :

```math
x(t) = e^{-\xi\omega_0 t}\bigl(A\cos(\omega_d t) + B\sin(\omega_d t)\bigr)
```

où $`A`$ et $`B`$ sont déterminées à partir des conditions initiales.

Caractéristiques du régime sous-amorti :

- oscillations pseudo-périodiques ;
- enveloppe exponentielle décroissante $`e^{-\xi\omega_0 t}`$ ;
- fréquence amortie inférieure à la pulsation propre non amortie.

## 4. Régime critique

Dans le cas $`\xi = 1`$, l’équation caractéristique admet une racine double. On a :

```math
(r + \omega_0)^2 = 0
```

La racine double est :

```math
r_{1,2} = -\omega_0
```

La solution générale de l’équation différentielle est alors :

```math
x(t) = (A + Bt)e^{-\omega_0 t}
```

Ce régime présente les propriétés suivantes :

- racine double de l’équation caractéristique ;
- absence totale d’oscillation ;
- retour à l’équilibre le plus rapide sans dépassement.

## 5. Régime sur-amorti

Dans le cas $`\xi > 1`$, les racines de l’équation caractéristique sont réelles et distinctes. On définit :

```math
\omega_d = \omega_0\sqrt{\xi^2 - 1}
```

Les racines deviennent :

```math
r_1 = -\xi\omega_0 + \omega_d
```

```math
r_2 = -\xi\omega_0 - \omega_d
```

La solution générale peut s’écrire sous forme exponentielle :

```math
x(t) = C_1 e^{r_1 t} + C_2 e^{r_2 t}
```

ou encore sous forme hyperbolique :

```math
x(t) = e^{-\xi\omega_0 t}\bigl(A\cosh(\omega_d t) + B\sinh(\omega_d t)\bigr)
```

Caractéristiques du régime sur-amorti :

- deux racines réelles distinctes de l’équation caractéristique ;
- réponse non oscillatoire ;
- retour monotone vers l’équilibre ;
- réponse plus lente que dans le régime critique.

## 6. Détermination des constantes dans le régime critique

Pour le régime critique, la solution est :

```math
x(t) = (A + Bt)e^{-\omega_0 t}
```

En utilisant la condition initiale $`x(0) = x_0`$, on obtient :

```math
A = x_0
```

La dérivée temporelle vaut :

```math
\dot{x}(t) = e^{-\omega_0 t}\left[B - \omega_0(A + Bt)\right]
```

En imposant la condition initiale $`\dot{x}(0) = \dot{x}_0`$, on obtient :

```math
\dot{x}_0 = B - \omega_0 A
```

d’où :

```math
B = \dot{x}_0 + \omega_0 x_0
```

Finalement, la solution critique s’écrit :

```math
x(t) = e^{-\omega_0 t}\left[x_0(1+\omega_0 t) + \dot{x}_0 t\right]
```

## 7. Détermination des constantes dans le régime sur-amorti

Pour le régime sur-amorti, on utilise la forme :

```math
x(t) = e^{-\xi\omega_0 t}\bigl(A\cosh(\omega_d t) + B\sinh(\omega_d t)\bigr)
```

La condition initiale $`x(0) = x_0`$ donne immédiatement :

```math
A = x_0
```

La dérivée de la solution est :

```math
\dot{x}(t) =
e^{-\xi\omega_0 t}
\Big[
(-\xi\omega_0 A + \omega_d B)\cosh(\omega_d t)
+
(-\xi\omega_0 B + \omega_d A)\sinh(\omega_d t)
\Big]
```

En évaluant cette relation en $`t = 0`$, on obtient :

```math
\dot{x}_0 = -\xi\omega_0 A + \omega_d B
```

Comme $`A = x_0`$, il vient :

```math
B = \dfrac{\dot{x}_0 + \xi\omega_0 x_0}{\omega_d}
```

La solution finale du régime sur-amorti est donc :

```math
x(t) =
e^{-\xi\omega_0 t}
\left[
x_0\cosh(\omega_d t)
+
\dfrac{\dot{x}_0 + \xi\omega_0 x_0}{\omega_d}\sinh(\omega_d t)
\right]
```

## 8. Interprétation physique

L’analyse des trois régimes permet de dégager les observations suivantes :

- dans le régime sous-amorti, le système oscille autour de sa position d’équilibre avec une amplitude décroissante ;
- dans le régime critique, le système revient à l’équilibre sans oscillation et en un temps minimal ;
- dans le régime sur-amorti, le système ne présente pas d’oscillation mais revient plus lentement à l’équilibre.

Un amortissement trop faible laisse subsister des oscillations. Un amortissement trop fort ralentit la dynamique. Le régime critique constitue donc un compromis optimal entre rapidité et stabilité.

## 9. Cas particuliers utiles

### 9.1 Déplacement initial non nul et vitesse initiale nulle

Si $`\dot{x}_0 = 0`$, on obtient :

Régime critique :

```math
x_{\text{crit}}(t) = x_0(1+\omega_0 t)e^{-\omega_0 t}
```

Régime sur-amorti :

```math
x_{\text{sur}}(t) =
x_0 e^{-\xi\omega_0 t}
\left[
\cosh(\omega_d t)
+
\dfrac{\xi\omega_0}{\omega_d}\sinh(\omega_d t)
\right]
```

### 9.2 Déplacement initial nul et vitesse initiale non nulle

Si $`x_0 = 0`$, on obtient :

Régime critique :

```math
x_{\text{crit}}(t) = \dot{x}_0 t e^{-\omega_0 t}
```

Régime sur-amorti :

```math
x_{\text{sur}}(t) =
\dfrac{\dot{x}_0}{\omega_d}e^{-\xi\omega_0 t}\sinh(\omega_d t)
```

## Lien entre les écritures exponentielle et hyperbolique

Dans le régime sur-amorti, les formes exponentielle et hyperbolique sont strictement équivalentes. En développant les fonctions hyperboliques, on retrouve :

```math
x(t) =
\dfrac{1}{2}
\left(
x_0 + \dfrac{\dot{x}_0 + \xi\omega_0 x_0}{\omega_d}
\right)
e^{(-\xi\omega_0 + \omega_d)t}
+
\dfrac{1}{2}
\left(
x_0 - \dfrac{\dot{x}_0 + \xi\omega_0 x_0}{\omega_d}
\right)
e^{(-\xi\omega_0 - \omega_d)t}
```

Cette écriture met en évidence les deux modes exponentiels associés aux deux racines réelles.

## Représentation graphique

La figure suivante illustre l’évolution du déplacement pour l’exercice 1 :

![Solution de l'exercice 1](../Figures/Ex1Sol.png)

*Figure — Illustration associée à l’exercice 1.*

## Synthèse des résultats

| Régime | Condition sur $`\xi`$ | Nature des racines | Forme générale de la solution | Comportement |
|---|---|---|---|---|
| Sous-amorti | $`0 < \xi < 1`$ | Complexes conjuguées | $`e^{-\xi\omega_0 t}\bigl(A\cos(\omega_d t)+B\sin(\omega_d t)\bigr)`$ | Oscillations amorties |
| Critique | $`\xi = 1`$ | Réelle double | $`(A+Bt)e^{-\omega_0 t}`$ | Retour le plus rapide sans oscillation |
| Sur-amorti | $`\xi > 1`$ | Réelles distinctes | $`e^{-\xi\omega_0 t}\bigl(A\cosh(\omega_d t)+B\sinh(\omega_d t)\bigr)`$ | Retour monotone plus lent |

## Points de vigilance

- Ne pas confondre la pseudo-pulsation du régime sous-amorti, $`\omega_d = \omega_0\sqrt{1-\xi^2}`$, avec la quantité définie dans le régime sur-amorti, $`\omega_d = \omega_0\sqrt{\xi^2-1}`$.
- Dans les dérivations, il faut appliquer correctement la règle du produit lors de la dérivation du terme exponentiel.
- Le cas critique $`\xi = 1`$ est un cas particulier correspondant à une racine double ; sa solution ne doit pas être confondue avec celle obtenue pour deux racines distinctes.

## Questions d’approfondissement

1. Pourquoi le régime critique correspond-il au retour le plus rapide à l’équilibre sans oscillation ?
2. Pourquoi le régime sur-amorti est-il plus lent que le régime critique malgré un amortissement plus élevé ?
3. Que devient la solution dans la limite $`\xi \to +\infty`$ ?
4. Comparer les maxima des réponses critiques et sur-amorties pour des conditions initiales identiques.

