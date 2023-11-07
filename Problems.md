# Test Functions

Bellow You'll find the definitions of all the test functions implemented in this package.

## Ackley
***Function name:*** `ackley`

```math
f(x) = -20 e^{-0.2 \sqrt{D^{-1} \sum\nolimits_{i=1}^D x_i^2}} - e^{D^{-1} \sum\nolimits_{i=1}^D \cos(2 \pi x_i)} + 20 + e
```

**Dimensions:** $D$

**Global optimum:** $`f(x^*) = 0`$ for $`x_i^* = 0`$

## Alpine 1
***Function name:*** `alpine1`

```math
f(x) = \sum_{i=1}^{D} \lvert {x_i \sin \left( x_i \right) + 0.1 x_i} \rvert
```

**Dimensions:** $D$

**Global optimum:** $`f(x^*) = 0`$ for $`x_i^* = 0`$

## Alpine 2
***Function name:*** `alpine2`

```math
f(x) = \prod_{i=1}^{D} \sqrt{x_i} \sin(x_i)
```

**Dimensions:** $D$

**Global optimum:** $`f(x^*) = 2.808^D`$ for $`x_i^* = 7.917`$

## Cigar
***Function name:*** `cigar`

```math
f(x) = x_1^2 + 10^6\sum_{i=2}^{D} x_i^2
```

**Dimensions:** $D$

**Global optimum:** $`f(x^*) = 0`$ for $`x_i^* = 0`$

## Cosine Mixture
***Function name:*** `cosine_mixture`

```math
f(x) = -0.1 \sum_{i=1}^D \cos (5 \pi x_i) - \sum_{i=1}^D x_i^2
```

**Dimensions:** $D$

**Global optimum:** $`f(x^*) = -0.1 D`$ for $`x_i^* = 0`$

## Csendes
***Function name:*** `csendes`

```math
f(x) =  \sum_{i=1}^D x_i^6 \left( 2 + \sin \frac{1}{x_i}\right)
```

**Dimensions:** $D$

**Global optimum:** $`f(x^*) = 0`$ for $`x_i^* = 0`$

## Dixon-Price
***Function name:*** `dixon_price`

```math
f(x) = (x_1 - 1)^2 + \sum_{i = 2}^D i (2x_i^2 - x_{i - 1})^2
```

**Dimensions:** $D$

**Global optimum:** $`f(x^*) = 0`$ for $`x_i^* = 2^{- \frac{(2^i - 2)}{2^i}}`$

## Griewank
***Function name:*** `griewank`

```math
f(x) = \sum_{i=1}^D \frac{x_i^2}{4000} - \prod_{i=1}^D \cos(\frac{x_i}{\sqrt{i}}) + 1
```

**Dimensions:** $D$

**Global optimum:** $`f(x^*) = 0`$ for $`x_i^* = 0`$

## Katsuura
***Function name:*** `katsuura`

```math
\prod_{i=1}^D \left(1 + i \sum_{j=1}^{32} \frac{\lvert 2^j x_i - round\left(2^j x_i \right) \rvert}{2^j} \right)
```

**Dimensions:** $D$

**Global optimum:** $`f(x^*) = 1`$ for $`x_i^* = 0`$

## Levy
***Function name:*** `levy`

```math
 \begin{gather}
    \sin^2 (\pi w_1) + \sum_{i = 1}^{D - 1} (w_i - 1)^2 \left( 1 + 10 \sin^2 (\pi w_i + 1) \right) + (w_d - 1)^2 (1 + \sin^2 (2 \pi w_d)),\,\text{where}\\
    w_i = 1 + \frac{x_i - 1}{4},\, \text{for all } i = 1, \ldots, D
  \end{gather}
 
```

**Dimensions:** $D$

**Global optimum:** $`f(x^*) = 0`$ for $`x_i^* = 1`$

## Michalewicz
***Function name:*** `michalewicz`

```math
f(x) = - \sum_{i = 1}^{D} \sin(x_i) \sin^{2m}\left( \frac{ix_i^2}{\pi} \right)
```

**Dimensions:** $D$

**Global optimum:** $`\text{at } D=2,\,f(x^*) = -1.8013`$ for $`x^* = (2.20, 1.57)`$

## Perm 1
***Function name:*** `perm1`

```math
f(x) =  \sum_{i = 1}^D \left( \sum_{j = 1}^D (j^i + \beta) \left( \left(\frac{x_j}{j}\right)^i - 1 \right) \right)^2
```

**Dimensions:** $D$

**Global optimum:** $`f(x^*) = 0`$ for $`x_i^* = i`$

## Perm 2
***Function name:*** `perm2`

```math
f(x) =  \sum_{i = 1}^D \left( \sum_{j = 1}^D (j - \beta) \left( x_j^i - \frac{1}{j^i} \right) \right)^2
```

**Dimensions:** $D$

**Global optimum:** $`f(x^*) = 0`$ for $`x_i^* = \frac{1}{i}`$

## Pinter
***Function name:*** `pinter`

```math
f(x) = \sum_{i=1}^D ix_i^2 + \sum_{i=1}^D 20i \sin^2 A + \sum_{i=1}^D i \log_{10} (1 + iB^2),\, \text{where}
```
```math
\begin{align}
A &= (x_{i-1}\sin(x_i)+\sin(x_{i+1})) \\
B &= (x_{i-1}^2 - 2x_i + 3x_{i+1} - \cos(x_i) + 1)
\end{align}
```

**Dimensions:** $D$

**Global optimum:** $`f(x^*) = 0`$ for $`x_i^* = 0`$

## Powell
***Function name:*** `powell`

```math
f(x) = \sum_{i = 1}^{D/4} \left[ (x_{4 i - 3} + 10 x_{4 i - 2})^2 + 5 (x_{4 i - 1} - x_{4 i})^2 + (x_{4 i - 2} - 2 x_{4 i - 1})^4 + 10 (x_{4 i - 3} - x_{4 i})^4 \right]
```

**Dimensions:** $D$

**Global optimum:** $`f(x^*) = 0`$ for $`x_i^* = 0`$

## Qing 
***Function name:*** `qing`

```math
f(x) = \sum_{i=1}^D \left(x_i^2 - i\right)^2
```

**Dimensions:** $D$

**Global optimum:** $`f(x^*) = 0`$ for $`x_i^* = \pm \sqrt{i}`$

## Quintic 
***Function name:*** `quintic`

```math
f(x) = \sum_{i=1}^D \left| x_i^5 - 3x_i^4 + 4x_i^3 + 2x_i^2 - 10x_i - 4\right|
```

**Dimensions:** $D$

**Global optimum:** $`f(x^*) = 0`$ for $`x_i^* = -1\quad \text{or} \quad x_i^* = 2`$

## Rastrigin 
***Function name:*** `rastrigin`

```math
f(x) = 10D + \sum_{i=1}^D \left[x_i^2 -10\cos(2\pi x_i)\right]
```

**Dimensions:** $D$

**Global optimum:** $`f(x^*) = 0`$ for $`x_i^* = 0`$

## Rosenbrock 
***Function name:*** `rosenbrock`

```math
f(x) = \sum_{i=1}^{D-1} \left[100 (x_{i+1} - x_i^2)^2 + (x_i - 1)^2 \right]
```

**Dimensions:** $D$

**Global optimum:** $`f(x^*) = 0`$ for $`x_i^* = 1`$

## Salomon 
***Function name:*** `salomon`

```math
f(x) =  1 - \cos\left(2\pi\sqrt{\sum\nolimits_{i=1}^D x_i^2} \right)+ 0.1 \sqrt{\sum\nolimits_{i=1}^D x_i^2}
```

**Dimensions:** $D$

**Global optimum:** $`f(x^*) = 0`$ for $`x_i^* = 0`$

## Schaffer 2 
***Function name:*** `schaffer2`

```math
f(x) = 0.5 + \frac{ \sin^2 \left( x_1^2 - x_2^2 \right) - 0.5 }{ \left[ 1 + 0.001 \left(  x_1^2 + x_2^2 \right) \right]^2 }
```

**Dimensions:** 2

**Global optimum:** $`f(x^*) = 0`$ for $`x^* = (0, 0)`$

## Schaffer 4 
***Function name:*** `schaffer4`

```math
f(x) = 0.5 + \frac{ \cos^2 \left( \sin \left( \vert x_1^2 - x_2^2\vert \right) \right)- 0.5 }{ \left[ 1 + 0.001 \left(  x_1^2 + x_2^2 \right) \right]^2 }
```

**Dimensions:** 2

**Global optimum:** $`f(x^*) = 0.292579`$ for $`x^* = (0, \pm 1.25313) \text{or} (\pm 1.25313, 0)`$

## Schwefel 
***Function name:*** `schwefel`

```math
f(x) = 418.9829D - \sum_{i=1}^{D} x_i \sin(\sqrt{\lvert x_i \rvert})
```

**Dimensions:** $D$

**Global optimum:** $`f(x^*) = 0`$ for $`x_i^* = 420.9687`$

## Schwefel 2.21 
***Function name:*** `schwefel221`

```math
f(x) = \max_{1 \leq i \leq D} \vert x_i\vert
```

**Dimensions:** $D$

**Global optimum:** $`f(x^*) = 0`$ for $`x_i^* = 0`$

## Schwefel 2.22 
***Function name:*** `schwefel222`

```math
f(x) = \sum_{i=1}^{D} \lvert x_i \rvert +\prod_{i=1}^{D} \lvert x_i \rvert
```

**Dimensions:** $D$

**Global optimum:** $`f(x^*) = 0`$ for $`x_i^* = 0`$

## Sphere 
***Function name:*** `sphere`

```math
f(x) = \sum_{i=1}^D x_i^2
```

**Dimensions:** $D$

**Global optimum:** $`f(x^*) = 0`$ for $`x_i^* = 0`$

## Step 
***Function name:*** `step`

```math
f(x) = \sum_{i=1}^D \left( \lfloor \lvert x_i \rvert \rfloor \right)
```

**Dimensions:** $D$

**Global optimum:** $`f(x^*) = 0`$ for $`x_i^* = 0`$

## Step 2
***Function name:*** `step2`

```math
f(x) = \sum_{i=1}^D \left( \lfloor x_i + 0.5 \rfloor \right)^2
```

**Dimensions:** $D$

**Global optimum:** $`f(x^*) = 0`$ for $`x_i^* = -0.5`$

## Styblinski-Tang 
***Function name:*** `styblinski_tang`

```math

```

**Dimensions:** $D$

**Global optimum:** $`f(x^*) = -39.16599 D`$ for $`x_i^* = -2.903534`$

## Trid 
***Function name:*** `trid`

```math
f(x) = \sum_{i = 1}^D \left( x_i - 1 \right)^2 - \sum_{i = 2}^D x_i x_{i - 1}
```

**Dimensions:** $D$

**Global optimum:** $`f(x^*) = \frac{-D (D + 4) (D - 1)}{6}`$ for $`x_i^* = i (d + 1 - i)`$

## Weierstrass
***Function name:*** `weierstrass`

```math
f(x) = \sum_{i=1}^D \left[ \sum_{k=0}^{k_{max}} a^k \cos\left( 2 \pi b^k ( x_i + 0.5) \right) \right] - D \sum_{k=0}^{k_{max}} a^k \cos \left(\pi b^k \right)
```

**Dimensions:** $D$

**Global optimum:** $`f(x^*) = 0`$ for $`x_i^* = 0`$

## Whitley 
***Function name:*** `whitley`

```math
f(x) = \sum_{i=1}^D \sum_{j=1}^D \left[\frac{(100(x_i^2-x_j)^2 + (1-x_j)^2)^2}{4000} - \cos(100(x_i^2-x_j)^2 + (1-x_j)^2)+1\right]
```

**Dimensions:** $D$

**Global optimum:** $`f(x^*) = 0`$ for $`x_i^* = 1`$

## Zakharov
***Function name:*** `zakharov`

```math
f(x) = \sum_{i = 1}^D x_i^2 + \left( \sum_{i = 1}^D 0.5 i x_i \right)^2 + \left( \sum_{i = 1}^D 0.5 i x_i \right)^4
```

**Dimensions:** $D$

**Global optimum:** $`f(x^*) = 0`$ for $`x_i^* = 0`$


# References

[1] P. Ernesto and U. Diliman, [“MVF–Multivariate Test Functions Library in C for Unconstrained Global Optimization,”](http://www.geocities.ws/eadorio/mvf.pdf) University of the Philippines Diliman, Quezon City, 2005.

[2] M. Jamil and X.-S. Yang, [“A literature survey of benchmark functions for global optimisation problems,”](https://arxiv.org/abs/1308.4008) International Journal of Mathematical Modelling and Numerical Optimisation, vol. 4, no. 2, p. 150, Jan. 2013, doi: 10.1504/ijmmno.2013.055204.

[3] J. J. Liang, B. Y. Qu, and P. N. Suganthan, [“Problem definitions and evaluation criteria for the CEC 2014 special session and competition on single objective real-parameter numerical optimization,”](http://bee22.com/manual/tf_images/Liang%20CEC2014.pdf) Computational Intelligence Laboratory, Zhengzhou University, Zhengzhou China and Technical Report, Nanyang Technological University, Singapore, vol. 635, no. 2, 2013.

[4] S. Surjanovic and D. Bingham, Virtual Library of Simulation Experiments: Test Functions and Datasets. Retrieved November 7, 2023, from https://www.sfu.ca/~ssurjano/. 
