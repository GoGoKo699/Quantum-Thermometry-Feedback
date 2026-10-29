# Thermal sensitivity has a finite area

[Science index](README.md) · [Model](model.md) · [Two-batch proof](two_batch_converse.md)

## Gibbs information in logarithmic temperature

For a fixed finite-dimensional Hamiltonian $`H`$ and $`\beta=e^{-x}=1/T`$, its Gibbs eigenvalues are $`p_i(x)=e^{-\beta E_i}/Z(\beta)`$. Differentiating the log likelihood with the Hamiltonian fixed gives

```math
\partial_x \ln p_i(x)=\beta(E_i-\langle H\rangle_x).
```

The classical Fisher information of a complete energy measurement, and the quantum Fisher information of the commuting Gibbs family, therefore agree:

```math
F_H(x)=\sum_i p_i(x)[\partial_x\ln p_i(x)]^2
=\beta^2\mathrm{Var}_x(H)=:C_H(x).
```

Here $`k_B=1`$, so $`C_H`$ is the dimensionless heat capacity. This identity also proves that arbitrary POVMs cannot exceed energy measurement information for a single fixed Gibbs Hamiltonian.

## Integrated area bound

The thermal entropy is

```math
S_H(x)=-\mathrm{Tr}(\rho_{H,x}\ln\rho_{H,x})
=\beta\langle H\rangle_x+\ln Z(\beta).
```

Direct differentiation gives the **entropy–area identity**

```math
\frac{dS_H(x)}{dx}=C_H(x).
```

Because $`0\le S_H(x)\le\ln D`$ for a $`D`$-dimensional state and $`C_H(x)\ge0`$,

```math
\boxed{\int_{-\infty}^{\infty} C_H(x)\,dx
=S_H(+\infty)-S_H(-\infty)\le\ln D.}
```

The same inequality holds on any subinterval, including the prior interval. For $`n`$ qubits, $`D=2^n`$ and

```math
\int_a^b C_H(x)\,dx\le n\ln2.
```

Interactions can make $`C_H(x)`$ extremely tall near a special $`x`$, but they cannot increase its integrated sensitivity beyond this logarithmic Hilbert-space budget. The integrated identity and its use in nonadaptive thermometry are **established ingredients**, notably in Mehboudi et al. [PRL 128, 130502 (2022)](https://doi.org/10.1103/PhysRevLett.128.130502). The new use is to combine the area budget with an *adaptive posterior concentration bound*.

For a normalized nonnegative density $`q(x)`$ on $`[a,b]`$,

```math
\int_a^b q(x)C_H(x)\,dx
\le\|q\|_\infty\,n\ln2.
```

This is the useful posterior-weighted form: tuning can reposition the sensitivity peak, but only a sufficiently concentrated posterior allows its whole area to matter.

## Separate pointwise upper bound

For the round-count consequence we also need a uniform $`O(n^2)`$ bound on $`C_H(x)`$, without restricting the energy scale. Here is a direct elementary proof.

Shift the lowest energy to zero, put $`Y=\beta E\ge0`$, and let $`D=2^n`$. The partition function then satisfies $`Z\ge1`$, and for every $`t\ge0`$ the Gibbs tail is

```math
\Pr(Y\ge t)\le \min\{1,D e^{-t}\}.
```

Consequently

```math
\begin{aligned}
C_H(x)&=\mathrm{Var}(Y)\le\mathbb E[Y^2]\\
&=2\int_0^\infty t\,\Pr(Y\ge t)\,dt\\
&\le(\ln D)^2+2\ln D+2.
\end{aligned}
```

In particular, for $`n\ge1`$,

```math
\boxed{C_H(x)\le Bn^2,\qquad
B=(\ln 2)^2+2\ln2+2.}
```

The bound is loose but universal. The sharp local optimum for a highly degenerate two-level spectrum is known from earlier thermometer-design literature; that sharper coefficient is unnecessary here. The area bound is linear in $`n`$ and controls *global* nonadaptive information; the pointwise bound is quadratic and controls a *perfectly localized* thermal response. They measure different constraints.

## Example: a degenerate two-level block

For a $`k`$-qubit Hamiltonian with one ground state, $`g=2^k-1`$ excited states and gap $`E>0`$,

```math
H=E\left(I-|0^k\rangle\langle0^k|\right),\qquad
p_{\mathrm{exc}}(x)=\frac{g e^{-Ee^{-x}}}{1+g e^{-Ee^{-x}}}.
```

Let $`L=\ln g`$ and $`z=L-Ee^{-x}`$. Since $`p_{\mathrm{exc}}=\sigma(z)`$,

```math
C_H(x)=(Ee^{-x})^2\,p_{\mathrm{exc}}(1-p_{\mathrm{exc}}).
```

Near $`Ee^{-x}=L`$, its peak is of order $`L^2=\Theta(k^2)`$ but its width in $`x`$ is of order $`1/k`$. The area remains $`O(k)`$, consistent with the entropy identity. This is precisely the leverage and limitation exploited by the two-batch construction.

[Continue: posterior-concentration converse](two_batch_converse.md).