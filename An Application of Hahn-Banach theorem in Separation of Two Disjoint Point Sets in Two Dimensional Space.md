1. Introduction
============

Hahn-Banach theorem is a well known mathematical tool for functional
analysis, In a word, it states that given a sublinear functional <img src="https://www.zhihu.com/equation?tex=p" alt="p" class="ee_img tr_noresize" eeimg="1"> on
space <img src="https://www.zhihu.com/equation?tex=E" alt="E" class="ee_img tr_noresize" eeimg="1">, and a linear functional <img src="https://www.zhihu.com/equation?tex=\ell" alt="\ell" class="ee_img tr_noresize" eeimg="1"> on subspace <img src="https://www.zhihu.com/equation?tex=V" alt="V" class="ee_img tr_noresize" eeimg="1">, which
satisfies <img src="https://www.zhihu.com/equation?tex=\ell\leq p" alt="\ell\leq p" class="ee_img tr_noresize" eeimg="1">, we can extend the functional <img src="https://www.zhihu.com/equation?tex=\ell" alt="\ell" class="ee_img tr_noresize" eeimg="1"> to linear
functional <img src="https://www.zhihu.com/equation?tex=\tilde{\ell}" alt="\tilde{\ell}" class="ee_img tr_noresize" eeimg="1"> on whole space <img src="https://www.zhihu.com/equation?tex=E" alt="E" class="ee_img tr_noresize" eeimg="1"> and still satisfies the
inequality. A direct consequence is the following: Given two disjoint
sets <img src="https://www.zhihu.com/equation?tex=A" alt="A" class="ee_img tr_noresize" eeimg="1"> and <img src="https://www.zhihu.com/equation?tex=B" alt="B" class="ee_img tr_noresize" eeimg="1">, chosen any points <img src="https://www.zhihu.com/equation?tex=a_0\in A" alt="a_0\in A" class="ee_img tr_noresize" eeimg="1"> and <img src="https://www.zhihu.com/equation?tex=b_0\in B" alt="b_0\in B" class="ee_img tr_noresize" eeimg="1">, we
construct set <img src="https://www.zhihu.com/equation?tex=C" alt="C" class="ee_img tr_noresize" eeimg="1">: 

<img src="https://www.zhihu.com/equation?tex=C=\{y_0:y_0=a-b+b_0-a_0,a\in A, b\in B\}\\" alt="C=\{y_0:y_0=a-b+b_0-a_0,a\in A, b\in B\}\\" class="ee_img tr_noresize" eeimg="1">


Considering Minkowski functional <img src="https://www.zhihu.com/equation?tex=p_C" alt="p_C" class="ee_img tr_noresize" eeimg="1"> of set <img src="https://www.zhihu.com/equation?tex=C" alt="C" class="ee_img tr_noresize" eeimg="1">, it guarantees that
<img src="https://www.zhihu.com/equation?tex=p_C(x)\leq 1" alt="p_C(x)\leq 1" class="ee_img tr_noresize" eeimg="1"> for <img src="https://www.zhihu.com/equation?tex=x\in C" alt="x\in C" class="ee_img tr_noresize" eeimg="1"> and <img src="https://www.zhihu.com/equation?tex=p_C(x)>1" alt="p_C(x)>1" class="ee_img tr_noresize" eeimg="1"> for <img src="https://www.zhihu.com/equation?tex=x\notin C" alt="x\notin C" class="ee_img tr_noresize" eeimg="1">. If we let
<img src="https://www.zhihu.com/equation?tex=\ell(b_0-a_0)=p_C(b_0-a_0)" alt="\ell(b_0-a_0)=p_C(b_0-a_0)" class="ee_img tr_noresize" eeimg="1"> and extend <img src="https://www.zhihu.com/equation?tex=\ell" alt="\ell" class="ee_img tr_noresize" eeimg="1"> on whole space
<img src="https://www.zhihu.com/equation?tex=\mathbb{R}^d" alt="\mathbb{R}^d" class="ee_img tr_noresize" eeimg="1"> to <img src="https://www.zhihu.com/equation?tex=\tilde{\ell}" alt="\tilde{\ell}" class="ee_img tr_noresize" eeimg="1"> with restriction <img src="https://www.zhihu.com/equation?tex=\ell\leq p_C" alt="\ell\leq p_C" class="ee_img tr_noresize" eeimg="1">, the
following inequality will hold:


<img src="https://www.zhihu.com/equation?tex=\max_{a\in A}{\tilde{\ell}(a)}\le\min_{b\in B}{\tilde{\ell}(b)}\\" alt="\max_{a\in A}{\tilde{\ell}(a)}\le\min_{b\in B}{\tilde{\ell}(b)}\\" class="ee_img tr_noresize" eeimg="1">

 By
computing the two sides of inequality, <img src="https://www.zhihu.com/equation?tex=\tilde{\ell}(x)=\gamma" alt="\tilde{\ell}(x)=\gamma" class="ee_img tr_noresize" eeimg="1"> will
separate two sets where:


<img src="https://www.zhihu.com/equation?tex=\gamma\in[\max_{a\in A}{\tilde{\ell}(a)},\min_{b\in B}{\tilde{\ell}(b)}]\\" alt="\gamma\in[\max_{a\in A}{\tilde{\ell}(a)},\min_{b\in B}{\tilde{\ell}(b)}]\\" class="ee_img tr_noresize" eeimg="1">


and it gives mathematical foundation of possibility of separating two
disjoint sets by a hyperplane [@bertsekas2009convex]. We will give
details of the proof of above statements in
section [3](#sec:proof){reference-type="ref" reference="sec:proof"}.
However, there are some existence proof skills in proof of the
theorem [@stein2011functional]. Thus we cannot derive the separating
hyperplane directly from the proof.

Due to the work of Corinna Cortes and Vapnik, SVM gives a gradient
approach to construct the separating hyperplane  [@cortes1995support].
And it becomes the most popular mechanism for solving classification
problem [@bishop2006pattern]. The current usage of sub-gradient method
for SVM without kernel needs <img src="https://www.zhihu.com/equation?tex=O(ndT)" alt="O(ndT)" class="ee_img tr_noresize" eeimg="1"> time, for n examples, d
dimensions, T steps [@9520]. The shortage of SVM is it does not
guarantee we get the solution in a given time.

In this article, we review the proof of Hahn-Banach theorem, and in
section [4](#sec:bounds analysis){reference-type="ref"
reference="sec:bounds analysis"} prove that the key functional,
Minkowski functional is piecewise linear convex function by constructing
the analytical form of Minkowski functional, when it is a functional of
a convex polygon. The construction of analytical form cannot be done in
general cases. Furthermore, we show that the minimum of Minkowski
functional on a convex polygon can be computed directly once we have the
convex hull, without using any gradient method.

We conclude that two disjoint data sets, separator in linear separation
problem can be easily constructed using a convex polygon <img src="https://www.zhihu.com/equation?tex=K" alt="K" class="ee_img tr_noresize" eeimg="1"> obtained
from Minkowski difference of two data sets with the help of Minkowski
functional. And the minimum of Minkowski functional makes construction
steps possible and quickly be done in practice, instead of using any
gradient method like SVM. In
section [6](#experiment){reference-type="ref" reference="experiment"},
we give three results in 2D case. We show that for two disjoint sets,
our separator can separate two sets accurately. And our separator
behaves well even when two sets have a little of intersection. Our
experiments is in two dimensional case, but the algorithm is expected to
be used in any dimensional space.

From a higher perspective, this functional approach is using Minkowski
functional of convex hull related to data set measures the whole data
space.

2. Preliminaries
=============

In the following sections, <img src="https://www.zhihu.com/equation?tex=Conv(A)" alt="Conv(A)" class="ee_img tr_noresize" eeimg="1"> denotes the convex hull of point
set <img src="https://www.zhihu.com/equation?tex=A" alt="A" class="ee_img tr_noresize" eeimg="1">. <img src="https://www.zhihu.com/equation?tex=A\setminus B" alt="A\setminus B" class="ee_img tr_noresize" eeimg="1"> denotes the set difference of A and B.
<img src="https://www.zhihu.com/equation?tex=span\{x_0,x_1,\dots,x_d\}" alt="span\{x_0,x_1,\dots,x_d\}" class="ee_img tr_noresize" eeimg="1"> denotes the set of all finite linear
combinations of <img src="https://www.zhihu.com/equation?tex=x_0,x_1,\dots,x_d" alt="x_0,x_1,\dots,x_d" class="ee_img tr_noresize" eeimg="1">. <img src="https://www.zhihu.com/equation?tex=\left\lvert\cdot\right\rvert" alt="\left\lvert\cdot\right\rvert" class="ee_img tr_noresize" eeimg="1">
denotes 2-norm.

*Definition 2.1* (Minkowski difference). Given a vector space <img src="https://www.zhihu.com/equation?tex=V" alt="V" class="ee_img tr_noresize" eeimg="1"> and
two point sets <img src="https://www.zhihu.com/equation?tex=A" alt="A" class="ee_img tr_noresize" eeimg="1"> and <img src="https://www.zhihu.com/equation?tex=B" alt="B" class="ee_img tr_noresize" eeimg="1"> in <img src="https://www.zhihu.com/equation?tex=V" alt="V" class="ee_img tr_noresize" eeimg="1">, the Minkowski difference <img src="https://www.zhihu.com/equation?tex=A\ominus B" alt="A\ominus B" class="ee_img tr_noresize" eeimg="1">
is defined as: 

<img src="https://www.zhihu.com/equation?tex=A\ominus B=\{a-b\mid a\in A\text{ and }b\in B\}\\" alt="A\ominus B=\{a-b\mid a\in A\text{ and }b\in B\}\\" class="ee_img tr_noresize" eeimg="1">


Without proof here, we use the fact that 

<img src="https://www.zhihu.com/equation?tex=\label{eq:Minkowski sum}
    Conv(A\ominus B)=Conv(A)\ominus Conv(B)\\" alt="\label{eq:Minkowski sum}
    Conv(A\ominus B)=Conv(A)\ominus Conv(B)\\" class="ee_img tr_noresize" eeimg="1">

 The proof of above
equation is easy and can be found in [@625624].

*Definition 2.2* (sublinear functional). Given a vector space <img src="https://www.zhihu.com/equation?tex=V" alt="V" class="ee_img tr_noresize" eeimg="1"> and a
functional <img src="https://www.zhihu.com/equation?tex=P:V\to\mathbb{R}" alt="P:V\to\mathbb{R}" class="ee_img tr_noresize" eeimg="1">, we call <img src="https://www.zhihu.com/equation?tex=P" alt="P" class="ee_img tr_noresize" eeimg="1"> is a sublinear functional if:


<img src="https://www.zhihu.com/equation?tex=\label{property:sublinear}
    \left\{\begin{aligned}
         & P(av)=aP(v),                  & \mbox{if <img src="https://www.zhihu.com/equation?tex=a \geq 0" alt="a \geq 0" class="ee_img tr_noresize" eeimg="1"> and <img src="https://www.zhihu.com/equation?tex=v\in V" alt="v\in V" class="ee_img tr_noresize" eeimg="1">} \\
         & P(v_1+v_2)\leq P(v_1)+P(v_2), & \mbox{if <img src="https://www.zhihu.com/equation?tex=v_1,v_2\in V_0" alt="v_1,v_2\in V_0" class="ee_img tr_noresize" eeimg="1">}
    \end{aligned}
    \right.\\" alt="\label{property:sublinear}
    \left\{\begin{aligned}
         & P(av)=aP(v),                  & \mbox{if <img src="https://www.zhihu.com/equation?tex=a \geq 0" alt="a \geq 0" class="ee_img tr_noresize" eeimg="1"> and <img src="https://www.zhihu.com/equation?tex=v\in V" alt="v\in V" class="ee_img tr_noresize" eeimg="1">} \\
         & P(v_1+v_2)\leq P(v_1)+P(v_2), & \mbox{if <img src="https://www.zhihu.com/equation?tex=v_1,v_2\in V_0" alt="v_1,v_2\in V_0" class="ee_img tr_noresize" eeimg="1">}
    \end{aligned}
    \right.\\" class="ee_img tr_noresize" eeimg="1">

 *Definition 2.3* (Minkowski functional). Given a vector
space <img src="https://www.zhihu.com/equation?tex=V" alt="V" class="ee_img tr_noresize" eeimg="1"> and a non empty set <img src="https://www.zhihu.com/equation?tex=K" alt="K" class="ee_img tr_noresize" eeimg="1"> including <img src="https://www.zhihu.com/equation?tex=0" alt="0" class="ee_img tr_noresize" eeimg="1">, and <img src="https://www.zhihu.com/equation?tex=0" alt="0" class="ee_img tr_noresize" eeimg="1"> is not on the
boundary of set <img src="https://www.zhihu.com/equation?tex=K" alt="K" class="ee_img tr_noresize" eeimg="1">. For <img src="https://www.zhihu.com/equation?tex=v \in V" alt="v \in V" class="ee_img tr_noresize" eeimg="1"> define:


<img src="https://www.zhihu.com/equation?tex=p_K(v)=\inf_{r>0}\{r: v/r \in K\}\\" alt="p_K(v)=\inf_{r>0}\{r: v/r \in K\}\\" class="ee_img tr_noresize" eeimg="1">

 and functional <img src="https://www.zhihu.com/equation?tex=p_K" alt="p_K" class="ee_img tr_noresize" eeimg="1"> completely
characterized <img src="https://www.zhihu.com/equation?tex=K" alt="K" class="ee_img tr_noresize" eeimg="1"> in that 

<img src="https://www.zhihu.com/equation?tex=p_K(v)\leq 1\qquad if~and~only~if~v \in K\\" alt="p_K(v)\leq 1\qquad if~and~only~if~v \in K\\" class="ee_img tr_noresize" eeimg="1">


One important property of Minkowski functional is a sublinear
functional [@stein2011functional].

*THEOREM 2.4* (Hahn-Banach Theorem). *Suppose <img src="https://www.zhihu.com/equation?tex=V_0" alt="V_0" class="ee_img tr_noresize" eeimg="1"> is a linear subspace
of <img src="https://www.zhihu.com/equation?tex=V" alt="V" class="ee_img tr_noresize" eeimg="1"> and <img src="https://www.zhihu.com/equation?tex=p" alt="p" class="ee_img tr_noresize" eeimg="1"> is a sublinear functional on <img src="https://www.zhihu.com/equation?tex=V" alt="V" class="ee_img tr_noresize" eeimg="1">, and that we are given a
linear functional <img src="https://www.zhihu.com/equation?tex=\ell" alt="\ell" class="ee_img tr_noresize" eeimg="1"> on <img src="https://www.zhihu.com/equation?tex=V_0" alt="V_0" class="ee_img tr_noresize" eeimg="1"> that satisfies


<img src="https://www.zhihu.com/equation?tex=\ell(v)\le p(v),\qquad ~for~all~v \in V_0\\" alt="\ell(v)\le p(v),\qquad ~for~all~v \in V_0\\" class="ee_img tr_noresize" eeimg="1">

 Then <img src="https://www.zhihu.com/equation?tex=\ell" alt="\ell" class="ee_img tr_noresize" eeimg="1"> can be
extended to a linear functional <img src="https://www.zhihu.com/equation?tex=\tilde{\ell}" alt="\tilde{\ell}" class="ee_img tr_noresize" eeimg="1"> on <img src="https://www.zhihu.com/equation?tex=V" alt="V" class="ee_img tr_noresize" eeimg="1"> that satisfies


<img src="https://www.zhihu.com/equation?tex=\tilde{\ell}(v)\le p(v),\qquad~for~all~v \in V\\" alt="\tilde{\ell}(v)\le p(v),\qquad~for~all~v \in V\\" class="ee_img tr_noresize" eeimg="1">



*THEOREM 2.5* (Strict Separation Theorem). *Given a vector space <img src="https://www.zhihu.com/equation?tex=V" alt="V" class="ee_img tr_noresize" eeimg="1">,
and two non empty convex set <img src="https://www.zhihu.com/equation?tex=A" alt="A" class="ee_img tr_noresize" eeimg="1"> and <img src="https://www.zhihu.com/equation?tex=B" alt="B" class="ee_img tr_noresize" eeimg="1">, which satisfy:
<img src="https://www.zhihu.com/equation?tex=A\cap B=\emptyset" alt="A\cap B=\emptyset" class="ee_img tr_noresize" eeimg="1">. Then there is a linear functional <img src="https://www.zhihu.com/equation?tex=\ell" alt="\ell" class="ee_img tr_noresize" eeimg="1">, and a
real number <img src="https://www.zhihu.com/equation?tex=\alpha\in\mathbb{R}" alt="\alpha\in\mathbb{R}" class="ee_img tr_noresize" eeimg="1">, s.t.


<img src="https://www.zhihu.com/equation?tex=\max_{a\in A}{\ell(a)}<\alpha<\min_{b\in B}{\ell(b)},\qquad a\in A\\" alt="\max_{a\in A}{\ell(a)}<\alpha<\min_{b\in B}{\ell(b)},\qquad a\in A\\" class="ee_img tr_noresize" eeimg="1">


Since our construction of linear separator is based on the proof of
theorem 2.4 and 2.5, we will show the proof of theorems in
section [3](#sec:proof){reference-type="ref" reference="sec:proof"} and
analyze some functions in the proof in
section [4](#sec:bounds analysis){reference-type="ref"
reference="sec:bounds analysis"}.

3. Proofs
======

In this section we will prove theorem 2.4 and theorem 2.5. The procedure
of proofs will be used in constructing linear separator.

3.1. Proof of Theorem 2.4 

Given <img src="https://www.zhihu.com/equation?tex=\ell(x_0)" alt="\ell(x_0)" class="ee_img tr_noresize" eeimg="1"> for subspace <img src="https://www.zhihu.com/equation?tex=x_0\in V_0" alt="x_0\in V_0" class="ee_img tr_noresize" eeimg="1">, we select any vector <img src="https://www.zhihu.com/equation?tex=x_1" alt="x_1" class="ee_img tr_noresize" eeimg="1">
which is in space <img src="https://www.zhihu.com/equation?tex=V\setminus V_0" alt="V\setminus V_0" class="ee_img tr_noresize" eeimg="1"> and be ready to extend <img src="https://www.zhihu.com/equation?tex=\ell" alt="\ell" class="ee_img tr_noresize" eeimg="1"> to the
subspace <img src="https://www.zhihu.com/equation?tex=span\{x_0,x_1\}" alt="span\{x_0,x_1\}" class="ee_img tr_noresize" eeimg="1">. We can make a choice for the value of
<img src="https://www.zhihu.com/equation?tex=\tilde{\ell}" alt="\tilde{\ell}" class="ee_img tr_noresize" eeimg="1"> on <img src="https://www.zhihu.com/equation?tex=x_1" alt="x_1" class="ee_img tr_noresize" eeimg="1">, so as to satisfy
<img src="https://www.zhihu.com/equation?tex=\tilde{\ell}(x)\le p(x), \forall x\in V" alt="\tilde{\ell}(x)\le p(x), \forall x\in V" class="ee_img tr_noresize" eeimg="1"> if


<img src="https://www.zhihu.com/equation?tex=a\tilde{\ell}(x_1)+b\tilde{\ell}(x_0)=\tilde{\ell}(ax_1+bx_0)\le p(ax_1+bx_0),\qquad \forall a,b\in\mathbb{R}\\" alt="a\tilde{\ell}(x_1)+b\tilde{\ell}(x_0)=\tilde{\ell}(ax_1+bx_0)\le p(ax_1+bx_0),\qquad \forall a,b\in\mathbb{R}\\" class="ee_img tr_noresize" eeimg="1">


where <img src="https://www.zhihu.com/equation?tex=\tilde{\ell(x)}=\ell(x)" alt="\tilde{\ell(x)}=\ell(x)" class="ee_img tr_noresize" eeimg="1"> for all <img src="https://www.zhihu.com/equation?tex=x\in V_0" alt="x\in V_0" class="ee_img tr_noresize" eeimg="1">. If <img src="https://www.zhihu.com/equation?tex=a=0" alt="a=0" class="ee_img tr_noresize" eeimg="1">, above
inequality trivially holds. If <img src="https://www.zhihu.com/equation?tex=a\neq 0" alt="a\neq 0" class="ee_img tr_noresize" eeimg="1"> 

<img src="https://www.zhihu.com/equation?tex=\left\{
        \begin{array}{ll}
            \tilde{\ell}(x_1)\leq \frac{p(ax_1+bx_0)-b\tilde{\ell}(x_0)}{a},a>0 \\
            \tilde{\ell}(x_1)\geq \frac{b\tilde{\ell}(x_0)-p(ax_1+bx_0)}{-a},a<0
        \end{array}
        \right.\\" alt="\left\{
        \begin{array}{ll}
            \tilde{\ell}(x_1)\leq \frac{p(ax_1+bx_0)-b\tilde{\ell}(x_0)}{a},a>0 \\
            \tilde{\ell}(x_1)\geq \frac{b\tilde{\ell}(x_0)-p(ax_1+bx_0)}{-a},a<0
        \end{array}
        \right.\\" class="ee_img tr_noresize" eeimg="1">

 Then we get:


<img src="https://www.zhihu.com/equation?tex=\tilde{\ell}(w)-p(-x_1+w)\leq\tilde{\ell}(x_1)\leq p(x_1+w')-\tilde{\ell}(w'),\qquad ~\forall w, w'\in V_0\\" alt="\tilde{\ell}(w)-p(-x_1+w)\leq\tilde{\ell}(x_1)\leq p(x_1+w')-\tilde{\ell}(w'),\qquad ~\forall w, w'\in V_0\\" class="ee_img tr_noresize" eeimg="1">


Since 

<img src="https://www.zhihu.com/equation?tex=\begin{aligned}
        \tilde{\ell}(w)+\tilde{\ell}(w')= &\tilde{\ell}(w-x_1+w'+x_1)  \\
        \leq              & p(w-x_1+w'+x_1)     \\
        \leq              & p(-x_1+w)+p(x_1+w')
    \end{aligned}\\" alt="\begin{aligned}
        \tilde{\ell}(w)+\tilde{\ell}(w')= &\tilde{\ell}(w-x_1+w'+x_1)  \\
        \leq              & p(w-x_1+w'+x_1)     \\
        \leq              & p(-x_1+w)+p(x_1+w')
    \end{aligned}\\" class="ee_img tr_noresize" eeimg="1">

 always holds. The first inequality holds because of
<img src="https://www.zhihu.com/equation?tex=w+w'\in V_0" alt="w+w'\in V_0" class="ee_img tr_noresize" eeimg="1">, The second equality holds because of sublinear property
of <img src="https://www.zhihu.com/equation?tex=p" alt="p" class="ee_img tr_noresize" eeimg="1">. The Thus the upper bound of <img src="https://www.zhihu.com/equation?tex=\tilde{\ell}(x_1)" alt="\tilde{\ell}(x_1)" class="ee_img tr_noresize" eeimg="1"> is


<img src="https://www.zhihu.com/equation?tex=\label{l upper bound}
        \min_{w\in V_0}{\{-\tilde{\ell}(w)+p(w+x_1)}\}\\" alt="\label{l upper bound}
        \min_{w\in V_0}{\{-\tilde{\ell}(w)+p(w+x_1)}\}\\" class="ee_img tr_noresize" eeimg="1">

 and the lower
bound is 

<img src="https://www.zhihu.com/equation?tex=\label{l lower bound}
        \max_{w'\in V_0}{\{\tilde{\ell}(w')-p(w'-x_1)}\}\\" alt="\label{l lower bound}
        \max_{w'\in V_0}{\{\tilde{\ell}(w')-p(w'-x_1)}\}\\" class="ee_img tr_noresize" eeimg="1">

 We can choose
any real number between two bounds as value of <img src="https://www.zhihu.com/equation?tex=\tilde{\ell}(x_1)" alt="\tilde{\ell}(x_1)" class="ee_img tr_noresize" eeimg="1">. In
practice, we can choose the mean of two bounds as value of
<img src="https://www.zhihu.com/equation?tex=\tilde{\ell}(x_1)" alt="\tilde{\ell}(x_1)" class="ee_img tr_noresize" eeimg="1">. We can now extend subspace <img src="https://www.zhihu.com/equation?tex=V_0" alt="V_0" class="ee_img tr_noresize" eeimg="1"> to
<img src="https://www.zhihu.com/equation?tex=span\{x_0,x_1\}" alt="span\{x_0,x_1\}" class="ee_img tr_noresize" eeimg="1"> and letting


<img src="https://www.zhihu.com/equation?tex=\tilde{\ell}(\lambda_0x_0+\lambda_1x_1)=\lambda_0\tilde{\ell}(x_0)+\lambda_1\tilde{\ell}(x_1)\\" alt="\tilde{\ell}(\lambda_0x_0+\lambda_1x_1)=\lambda_0\tilde{\ell}(x_0)+\lambda_1\tilde{\ell}(x_1)\\" class="ee_img tr_noresize" eeimg="1">


We keep doing above step until <img src="https://www.zhihu.com/equation?tex=V=V_0" alt="V=V_0" class="ee_img tr_noresize" eeimg="1"> with <img src="https://www.zhihu.com/equation?tex=\tilde{\ell}(x)" alt="\tilde{\ell}(x)" class="ee_img tr_noresize" eeimg="1"> mapping
<img src="https://www.zhihu.com/equation?tex=V" alt="V" class="ee_img tr_noresize" eeimg="1"> to <img src="https://www.zhihu.com/equation?tex=\mathbb{R}" alt="\mathbb{R}" class="ee_img tr_noresize" eeimg="1">

For easier reading, we omit the difference between the symbol
<img src="https://www.zhihu.com/equation?tex=\tilde{\ell}" alt="\tilde{\ell}" class="ee_img tr_noresize" eeimg="1"> and <img src="https://www.zhihu.com/equation?tex=\ell" alt="\ell" class="ee_img tr_noresize" eeimg="1"> in following sections. We will keep using
symbol <img src="https://www.zhihu.com/equation?tex=\ell" alt="\ell" class="ee_img tr_noresize" eeimg="1"> after extension.

3.2 Proof of Theorem 2.5

Choose <img src="https://www.zhihu.com/equation?tex=a_0\in A\text{, }b_0\in B" alt="a_0\in A\text{, }b_0\in B" class="ee_img tr_noresize" eeimg="1"> which <img src="https://www.zhihu.com/equation?tex=b_0-a_0" alt="b_0-a_0" class="ee_img tr_noresize" eeimg="1"> is not on the
boundary of <img src="https://www.zhihu.com/equation?tex=Conv(A\ominus B)" alt="Conv(A\ominus B)" class="ee_img tr_noresize" eeimg="1">. Let <img src="https://www.zhihu.com/equation?tex=x_0=b_0-a_0" alt="x_0=b_0-a_0" class="ee_img tr_noresize" eeimg="1">. Construct set <img src="https://www.zhihu.com/equation?tex=C" alt="C" class="ee_img tr_noresize" eeimg="1">:


<img src="https://www.zhihu.com/equation?tex=\label{def:C}
        C=\{y_0:y_0=a-b+x_0,a\in A, b\in B\}\\" alt="\label{def:C}
        C=\{y_0:y_0=a-b+x_0,a\in A, b\in B\}\\" class="ee_img tr_noresize" eeimg="1">

 <img src="https://www.zhihu.com/equation?tex=C" alt="C" class="ee_img tr_noresize" eeimg="1"> has following
properties:

-   <img src="https://www.zhihu.com/equation?tex=C" alt="C" class="ee_img tr_noresize" eeimg="1"> is convex set, because of
    equation [\[eq:Minkowski sum\]](#eq:Minkowski sum){reference-type="ref"
    reference="eq:Minkowski sum"} and shifting set by <img src="https://www.zhihu.com/equation?tex=x_0" alt="x_0" class="ee_img tr_noresize" eeimg="1">.

-   <img src="https://www.zhihu.com/equation?tex=x_0 \notin C" alt="x_0 \notin C" class="ee_img tr_noresize" eeimg="1"> and <img src="https://www.zhihu.com/equation?tex=0\in C" alt="0\in C" class="ee_img tr_noresize" eeimg="1">, because of <img src="https://www.zhihu.com/equation?tex=A\cap B=\emptyset" alt="A\cap B=\emptyset" class="ee_img tr_noresize" eeimg="1">

-   <img src="https://www.zhihu.com/equation?tex=\forall x\in C\text{, }p_C(x)\leq1" alt="\forall x\in C\text{, }p_C(x)\leq1" class="ee_img tr_noresize" eeimg="1">, where <img src="https://www.zhihu.com/equation?tex=p_C" alt="p_C" class="ee_img tr_noresize" eeimg="1"> is Minkowski
    functional of <img src="https://www.zhihu.com/equation?tex=C" alt="C" class="ee_img tr_noresize" eeimg="1">.

Since the Minkowski functional <img src="https://www.zhihu.com/equation?tex=p_C" alt="p_C" class="ee_img tr_noresize" eeimg="1"> is a sublinear functional, by
Hahn-Banach Theorem, there exists a linear functional <img src="https://www.zhihu.com/equation?tex=\ell" alt="\ell" class="ee_img tr_noresize" eeimg="1">, s.t.


<img src="https://www.zhihu.com/equation?tex=\ell\le p_C\text{ and }\ell(x_0)=p_C(x_0)> 1\\" alt="\ell\le p_C\text{ and }\ell(x_0)=p_C(x_0)> 1\\" class="ee_img tr_noresize" eeimg="1">

 <img src="https://www.zhihu.com/equation?tex=p_C(x_0)<\infty" alt="p_C(x_0)<\infty" class="ee_img tr_noresize" eeimg="1"> since
<img src="https://www.zhihu.com/equation?tex=x_0" alt="x_0" class="ee_img tr_noresize" eeimg="1"> is not on the boundary of <img src="https://www.zhihu.com/equation?tex=Conv(A\ominus B)" alt="Conv(A\ominus B)" class="ee_img tr_noresize" eeimg="1">. Then we can extends
functional <img src="https://www.zhihu.com/equation?tex=\ell(x_0)" alt="\ell(x_0)" class="ee_img tr_noresize" eeimg="1"> to space <img src="https://www.zhihu.com/equation?tex=V_0=span\{x_0\}" alt="V_0=span\{x_0\}" class="ee_img tr_noresize" eeimg="1"> by letting
<img src="https://www.zhihu.com/equation?tex=\ell(kx_0)=k\ell(x_0)" alt="\ell(kx_0)=k\ell(x_0)" class="ee_img tr_noresize" eeimg="1">. For <img src="https://www.zhihu.com/equation?tex=k\geq0" alt="k\geq0" class="ee_img tr_noresize" eeimg="1">, the inequality <img src="https://www.zhihu.com/equation?tex=\ell\leq p_C" alt="\ell\leq p_C" class="ee_img tr_noresize" eeimg="1">
holds by property
[\[property:sublinear\]](#property:sublinear){reference-type="eqref"
reference="property:sublinear"}. For <img src="https://www.zhihu.com/equation?tex=k<0" alt="k<0" class="ee_img tr_noresize" eeimg="1">, the inequality
<img src="https://www.zhihu.com/equation?tex=\ell\leq p_C" alt="\ell\leq p_C" class="ee_img tr_noresize" eeimg="1"> holds immediately.

For all <img src="https://www.zhihu.com/equation?tex=x\in C" alt="x\in C" class="ee_img tr_noresize" eeimg="1">, we have: 

<img src="https://www.zhihu.com/equation?tex=\ell(a-b+x_0)\le p_C(a-b+x_0)<1\\" alt="\ell(a-b+x_0)\le p_C(a-b+x_0)<1\\" class="ee_img tr_noresize" eeimg="1">

 We get:


<img src="https://www.zhihu.com/equation?tex=\label{gamma bound}
        \ell(a)<\ell(b)+1-\ell(x_0)< \ell(b),\qquad\forall a\in A, \forall b\in B\\" alt="\label{gamma bound}
        \ell(a)<\ell(b)+1-\ell(x_0)< \ell(b),\qquad\forall a\in A, \forall b\in B\\" class="ee_img tr_noresize" eeimg="1">


The last inequality holds because of <img src="https://www.zhihu.com/equation?tex=\ell(x_0)>1" alt="\ell(x_0)>1" class="ee_img tr_noresize" eeimg="1">. Thus:


<img src="https://www.zhihu.com/equation?tex=\max_{a\in A}{\ell(a)}<\min_{b\in B}{\ell(b)}\\" alt="\max_{a\in A}{\ell(a)}<\min_{b\in B}{\ell(b)}\\" class="ee_img tr_noresize" eeimg="1">

 Thus there exists
<img src="https://www.zhihu.com/equation?tex=\alpha\in\mathbb{R}" alt="\alpha\in\mathbb{R}" class="ee_img tr_noresize" eeimg="1"> which satisfies:


<img src="https://www.zhihu.com/equation?tex=\ell(a)<\alpha<\ell(b), \qquad\forall a\in A,b\in B\\" alt="\ell(a)<\alpha<\ell(b), \qquad\forall a\in A,b\in B\\" class="ee_img tr_noresize" eeimg="1">



In practice, we can choose <img src="https://www.zhihu.com/equation?tex=\ell(x_0)=p_C(x_0)" alt="\ell(x_0)=p_C(x_0)" class="ee_img tr_noresize" eeimg="1">, and extend <img src="https://www.zhihu.com/equation?tex=\ell" alt="\ell" class="ee_img tr_noresize" eeimg="1"> as
procedure of proof in
section [3.1](#subsec:proof HB){reference-type="ref"
reference="subsec:proof HB"}. After extending <img src="https://www.zhihu.com/equation?tex=\ell(x)" alt="\ell(x)" class="ee_img tr_noresize" eeimg="1"> to entire vector
space <img src="https://www.zhihu.com/equation?tex=V" alt="V" class="ee_img tr_noresize" eeimg="1">, we select


<img src="https://www.zhihu.com/equation?tex=\gamma\in \left[\max_{a\in A}{\ell(a)},\min_{b\in B}{\ell(b)}\right]\\" alt="\gamma\in \left[\max_{a\in A}{\ell(a)},\min_{b\in B}{\ell(b)}\right]\\" class="ee_img tr_noresize" eeimg="1">


for which hyperplane <img src="https://www.zhihu.com/equation?tex=\ell(x)=\gamma" alt="\ell(x)=\gamma" class="ee_img tr_noresize" eeimg="1"> will separate set <img src="https://www.zhihu.com/equation?tex=A" alt="A" class="ee_img tr_noresize" eeimg="1"> and <img src="https://www.zhihu.com/equation?tex=B" alt="B" class="ee_img tr_noresize" eeimg="1">. In
practice, we can choose 

<img src="https://www.zhihu.com/equation?tex=\label{optimal gamma}
     \gamma=\frac{\max_{a\in A}{\ell(a)}+\min_{b\in B}{\ell(b)}}{2}\\" alt="\label{optimal gamma}
     \gamma=\frac{\max_{a\in A}{\ell(a)}+\min_{b\in B}{\ell(b)}}{2}\\" class="ee_img tr_noresize" eeimg="1">

 as
our optimal <img src="https://www.zhihu.com/equation?tex=\gamma" alt="\gamma" class="ee_img tr_noresize" eeimg="1">.

4. Analysis of two bounds of <img src="https://www.zhihu.com/equation?tex=\ell(x_1)" alt="\ell(x_1)" class="ee_img tr_noresize" eeimg="1">
=====================================

In this section, we will show that if we choose <img src="https://www.zhihu.com/equation?tex=\ell(x_0)=p_C(x_0)" alt="\ell(x_0)=p_C(x_0)" class="ee_img tr_noresize" eeimg="1">,
the two bounds of <img src="https://www.zhihu.com/equation?tex=\ell(x_1)" alt="\ell(x_1)" class="ee_img tr_noresize" eeimg="1"> will be equal, where <img src="https://www.zhihu.com/equation?tex=C" alt="C" class="ee_img tr_noresize" eeimg="1"> is defined as
equation [\[def:C\]](#def:C){reference-type="eqref" reference="def:C"}.
Since upper bound
[\[l upper bound\]](#l upper bound){reference-type="eqref"
reference="l upper bound"} of <img src="https://www.zhihu.com/equation?tex=\ell(x_1)" alt="\ell(x_1)" class="ee_img tr_noresize" eeimg="1"> has the same form with lower
bound [\[l lower bound\]](#l lower bound){reference-type="eqref"
reference="l lower bound"} except for a minus sign, we only need to
analyze the upper bound and use the same routine on lower bound.

We rewrite the function <img src="https://www.zhihu.com/equation?tex=p_C(x_1+w)-\ell(w)" alt="p_C(x_1+w)-\ell(w)" class="ee_img tr_noresize" eeimg="1"> as 

<img src="https://www.zhihu.com/equation?tex=\label{eq:f(k)}
    f(k)=p_C(x_1+kx_0)-k\ell(x_0)\\" alt="\label{eq:f(k)}
    f(k)=p_C(x_1+kx_0)-k\ell(x_0)\\" class="ee_img tr_noresize" eeimg="1">

 We first prove <img src="https://www.zhihu.com/equation?tex=p_C(x_1+kx_0)" alt="p_C(x_1+kx_0)" class="ee_img tr_noresize" eeimg="1"> is
piecewise linear continuous convex function of <img src="https://www.zhihu.com/equation?tex=k" alt="k" class="ee_img tr_noresize" eeimg="1">. Then we analyze
function <img src="https://www.zhihu.com/equation?tex=f(k)" alt="f(k)" class="ee_img tr_noresize" eeimg="1">. We choose <img src="https://www.zhihu.com/equation?tex=x_1" alt="x_1" class="ee_img tr_noresize" eeimg="1"> orthogonal to <img src="https://www.zhihu.com/equation?tex=x_0" alt="x_0" class="ee_img tr_noresize" eeimg="1"> for the sake of
easier analysis.

4.1 Analysis of <img src="https://www.zhihu.com/equation?tex=p_C(x_1+kx_0)" alt="p_C(x_1+kx_0)" class="ee_img tr_noresize" eeimg="1">
---------------------------

In this part, we will show that <img src="https://www.zhihu.com/equation?tex=p_C(x_1+kx_0)" alt="p_C(x_1+kx_0)" class="ee_img tr_noresize" eeimg="1"> is piecewise linear
continuous function of <img src="https://www.zhihu.com/equation?tex=k" alt="k" class="ee_img tr_noresize" eeimg="1">. We denote the point at which the ray in
direction of <img src="https://www.zhihu.com/equation?tex=x_1+kx_0" alt="x_1+kx_0" class="ee_img tr_noresize" eeimg="1"> intersects polygon as <img src="https://www.zhihu.com/equation?tex=M" alt="M" class="ee_img tr_noresize" eeimg="1">. See (a) in
figure [\[fig:proof\]](#fig:proof){reference-type="ref"
reference="fig:proof"}. Then we set the x-axis in direction of <img src="https://www.zhihu.com/equation?tex=x_0" alt="x_0" class="ee_img tr_noresize" eeimg="1"> and
the y-axis in direction of <img src="https://www.zhihu.com/equation?tex=x_1" alt="x_1" class="ee_img tr_noresize" eeimg="1">. The result coordinate system as (b) in
figure [\[fig:proof\]](#fig:proof){reference-type="ref"
reference="fig:proof"}. The coordinate value of <img src="https://www.zhihu.com/equation?tex=M" alt="M" class="ee_img tr_noresize" eeimg="1"> satisfies

\centering
![The diagram of proof.[]{label="fig:proof"}](proof1.png){#fig:proof
width="60%"}

\(a) The intersection of the polygon and the ray

\medskip
\centering
![The diagram of proof.[]{label="fig:proof"}](proof2.png){#fig:proof
width="60%"}

\(b) The coordinate system and related lines

\medskip


<img src="https://www.zhihu.com/equation?tex=\label{s}
    \left\{
    \begin{aligned}%
         y & =ax+b                                        \\
         y & =\frac{\lVert x_1\rVert}{k\lVert x_0\rVert}x
    \end{aligned}
    \right.\\" alt="\label{s}
    \left\{
    \begin{aligned}%
         y & =ax+b                                        \\
         y & =\frac{\lVert x_1\rVert}{k\lVert x_0\rVert}x
    \end{aligned}
    \right.\\" class="ee_img tr_noresize" eeimg="1">

 Solving equation [\[s\]](#s){reference-type="eqref"
reference="s"} we get the x-axis component of <img src="https://www.zhihu.com/equation?tex=M" alt="M" class="ee_img tr_noresize" eeimg="1"> is:


<img src="https://www.zhihu.com/equation?tex=x_M=\frac{bk\left\lvert x_0\right\rvert}{-ak\left\lvert x_0\right\rvert+\left\lvert x_1\right\rvert}\\" alt="x_M=\frac{bk\left\lvert x_0\right\rvert}{-ak\left\lvert x_0\right\rvert+\left\lvert x_1\right\rvert}\\" class="ee_img tr_noresize" eeimg="1">


By triangle similarity,
<img src="https://www.zhihu.com/equation?tex=p_C(x_1+kx_0)=\frac{k\left\lvert x_0\right\rvert}{x_M}" alt="p_C(x_1+kx_0)=\frac{k\left\lvert x_0\right\rvert}{x_M}" class="ee_img tr_noresize" eeimg="1">, we get:


<img src="https://www.zhihu.com/equation?tex=\label{explicit p}
    p_C(x_1+kx_0)=-\frac{a\left\lvert x_0\right\rvert}{b}k+\frac{\left\lvert x_1\right\rvert}{b}\\" alt="\label{explicit p}
    p_C(x_1+kx_0)=-\frac{a\left\lvert x_0\right\rvert}{b}k+\frac{\left\lvert x_1\right\rvert}{b}\\" class="ee_img tr_noresize" eeimg="1">


Thus <img src="https://www.zhihu.com/equation?tex=p_C(x_1+kx_0)" alt="p_C(x_1+kx_0)" class="ee_img tr_noresize" eeimg="1"> is a linear function of <img src="https://www.zhihu.com/equation?tex=k" alt="k" class="ee_img tr_noresize" eeimg="1"> on each segment and is
a piecewise linear continuous function. And <img src="https://www.zhihu.com/equation?tex=p_C(k_1+kx_0)" alt="p_C(k_1+kx_0)" class="ee_img tr_noresize" eeimg="1"> is a convex
function of <img src="https://www.zhihu.com/equation?tex=k" alt="k" class="ee_img tr_noresize" eeimg="1"> since: 

<img src="https://www.zhihu.com/equation?tex=\begin{aligned}
         & f(\lambda k_1+(1-\lambda)k_2)                                                  \\
    =    & p_C(x_1+(\lambda k_1+(1-\lambda)k_2)x_0)-(\lambda k_1+(1-\lambda)k_2)\ell(x_0) \\
    =    & p_C(\lambda(x_1+kx_0)+(1-\lambda)(x_1+k_2x_0))                                 \\
         & -(\lambda k_1+(1-\lambda)k_2)\ell(x_0)                                         \\
    \leq & p_C(\lambda(x_1+kx_0))-\lambda k_1\ell(x_0)                                    \\
         & +p_C((1-\lambda)(x_1+k_2x_0))-(1-\lambda)k_2\ell(x_0)                          \\
    =    & \lambda (p_C(x_1+kx_0)-\lambda k_1\ell(x_0))                                   \\
         & + (1-\lambda)(p_C(x_1+k_2x_0)-k_2\ell(x_0))                                    \\
    =    & \lambda f(k_1)+(1-\lambda)f(k_2)\end{aligned}\\" alt="\begin{aligned}
         & f(\lambda k_1+(1-\lambda)k_2)                                                  \\
    =    & p_C(x_1+(\lambda k_1+(1-\lambda)k_2)x_0)-(\lambda k_1+(1-\lambda)k_2)\ell(x_0) \\
    =    & p_C(\lambda(x_1+kx_0)+(1-\lambda)(x_1+k_2x_0))                                 \\
         & -(\lambda k_1+(1-\lambda)k_2)\ell(x_0)                                         \\
    \leq & p_C(\lambda(x_1+kx_0))-\lambda k_1\ell(x_0)                                    \\
         & +p_C((1-\lambda)(x_1+k_2x_0))-(1-\lambda)k_2\ell(x_0)                          \\
    =    & \lambda (p_C(x_1+kx_0)-\lambda k_1\ell(x_0))                                   \\
         & + (1-\lambda)(p_C(x_1+k_2x_0)-k_2\ell(x_0))                                    \\
    =    & \lambda f(k_1)+(1-\lambda)f(k_2)\end{aligned}\\" class="ee_img tr_noresize" eeimg="1">

 The
inequality and the following equality holds because of sublinear
properties of <img src="https://www.zhihu.com/equation?tex=p_C" alt="p_C" class="ee_img tr_noresize" eeimg="1">. Thus <img src="https://www.zhihu.com/equation?tex=f(k)" alt="f(k)" class="ee_img tr_noresize" eeimg="1"> is a piecewise linear continuous convex
function.

4.2 The upper bound of <img src="https://www.zhihu.com/equation?tex=\ell(x_1)" alt="\ell(x_1)" class="ee_img tr_noresize" eeimg="1">
------------------------------

If we choose <img src="https://www.zhihu.com/equation?tex=\ell(x_0)=p_C(x_0)" alt="\ell(x_0)=p_C(x_0)" class="ee_img tr_noresize" eeimg="1">, equation
[\[s\]](#s){reference-type="eqref" reference="s"} for <img src="https://www.zhihu.com/equation?tex=x_0" alt="x_0" class="ee_img tr_noresize" eeimg="1"> becomes:


<img src="https://www.zhihu.com/equation?tex=\label{eqs:x0}
    \left\{
    \begin{aligned}%
         y & =ax+b \\
         y & =0
    \end{aligned}
    \right.\\" alt="\label{eqs:x0}
    \left\{
    \begin{aligned}%
         y & =ax+b \\
         y & =0
    \end{aligned}
    \right.\\" class="ee_img tr_noresize" eeimg="1">

 we get: 

<img src="https://www.zhihu.com/equation?tex=\label{explicit px0}
    p_C(kx_0)=-\frac{a\left\lvert x_0\right\rvert}{b}k\\" alt="\label{explicit px0}
    p_C(kx_0)=-\frac{a\left\lvert x_0\right\rvert}{b}k\\" class="ee_img tr_noresize" eeimg="1">

 Substitute
equation [\[explicit p\]](#explicit p){reference-type="eqref"
reference="explicit p"} and
[\[explicit px0\]](#explicit px0){reference-type="eqref"
reference="explicit px0"} for
[\[eq:f(k)\]](#eq:f(k)){reference-type="eqref" reference="eq:f(k)"}. we
can get explicit form of <img src="https://www.zhihu.com/equation?tex=f(k)" alt="f(k)" class="ee_img tr_noresize" eeimg="1">: 

<img src="https://www.zhihu.com/equation?tex=f(k)=a^*k+b^*\\" alt="f(k)=a^*k+b^*\\" class="ee_img tr_noresize" eeimg="1">

 where:


<img src="https://www.zhihu.com/equation?tex=a^*=-\frac{a_s\left\lvert x_0\right\rvert}{b_s}+\frac{a_0\left\lvert x_0\right\rvert}{b_0}\\" alt="a^*=-\frac{a_s\left\lvert x_0\right\rvert}{b_s}+\frac{a_0\left\lvert x_0\right\rvert}{b_0}\\" class="ee_img tr_noresize" eeimg="1">


and: 

<img src="https://www.zhihu.com/equation?tex=b^*=\frac{\left\lvert x_1\right\rvert}{b_s}\\" alt="b^*=\frac{\left\lvert x_1\right\rvert}{b_s}\\" class="ee_img tr_noresize" eeimg="1">

 where <img src="https://www.zhihu.com/equation?tex=a_s" alt="a_s" class="ee_img tr_noresize" eeimg="1">, <img src="https://www.zhihu.com/equation?tex=b_s" alt="b_s" class="ee_img tr_noresize" eeimg="1">
is equation of segment which intersects the ray in direction of
<img src="https://www.zhihu.com/equation?tex=x_1+kx_0" alt="x_1+kx_0" class="ee_img tr_noresize" eeimg="1">, and <img src="https://www.zhihu.com/equation?tex=a_0" alt="a_0" class="ee_img tr_noresize" eeimg="1">, <img src="https://www.zhihu.com/equation?tex=b_0" alt="b_0" class="ee_img tr_noresize" eeimg="1"> is equation of segment which intersects the
ray in direction of <img src="https://www.zhihu.com/equation?tex=x_0" alt="x_0" class="ee_img tr_noresize" eeimg="1">.

We denote the point at which line <img src="https://www.zhihu.com/equation?tex=y=a_ix+b_i" alt="y=a_ix+b_i" class="ee_img tr_noresize" eeimg="1"> and x axis intersect as
<img src="https://www.zhihu.com/equation?tex=d_i" alt="d_i" class="ee_img tr_noresize" eeimg="1">, <img src="https://www.zhihu.com/equation?tex=d_i" alt="d_i" class="ee_img tr_noresize" eeimg="1"> is 

<img src="https://www.zhihu.com/equation?tex=d_i=-\frac{b_i}{a_i}\\" alt="d_i=-\frac{b_i}{a_i}\\" class="ee_img tr_noresize" eeimg="1">



By property of convex polygon, <img src="https://www.zhihu.com/equation?tex=d_s\geq d_0" alt="d_s\geq d_0" class="ee_img tr_noresize" eeimg="1"> if <img src="https://www.zhihu.com/equation?tex=d_s>0" alt="d_s>0" class="ee_img tr_noresize" eeimg="1">, and <img src="https://www.zhihu.com/equation?tex=d_s<d_0" alt="d_s<d_0" class="ee_img tr_noresize" eeimg="1">
if <img src="https://www.zhihu.com/equation?tex=d_s<0" alt="d_s<0" class="ee_img tr_noresize" eeimg="1">. Since <img src="https://www.zhihu.com/equation?tex=d_0>0" alt="d_0>0" class="ee_img tr_noresize" eeimg="1"> we have: 

<img src="https://www.zhihu.com/equation?tex=\frac{1}{d_s}-\frac{1}{d_0}\leq0\\" alt="\frac{1}{d_s}-\frac{1}{d_0}\leq0\\" class="ee_img tr_noresize" eeimg="1">


Thus <img src="https://www.zhihu.com/equation?tex=a^*" alt="a^*" class="ee_img tr_noresize" eeimg="1"> is always non-positive and equal to zero if <img src="https://www.zhihu.com/equation?tex=x_1+kx_0" alt="x_1+kx_0" class="ee_img tr_noresize" eeimg="1"> and
<img src="https://www.zhihu.com/equation?tex=x_0" alt="x_0" class="ee_img tr_noresize" eeimg="1"> intersect the same segment. Thus the minimum of <img src="https://www.zhihu.com/equation?tex=f(k)" alt="f(k)" class="ee_img tr_noresize" eeimg="1"> is


<img src="https://www.zhihu.com/equation?tex=\label{eq:min of f(k)}
    \ell(x_1)\leq\min_k{f(k)}=\frac{\left\lvert x_1\right\rvert}{b_0}\\" alt="\label{eq:min of f(k)}
    \ell(x_1)\leq\min_k{f(k)}=\frac{\left\lvert x_1\right\rvert}{b_0}\\" class="ee_img tr_noresize" eeimg="1">


which is the upper bound of <img src="https://www.zhihu.com/equation?tex=\ell(x_1)" alt="\ell(x_1)" class="ee_img tr_noresize" eeimg="1">.

4.3 The lower bound of <img src="https://www.zhihu.com/equation?tex=\ell(x_1)" alt="\ell(x_1)" class="ee_img tr_noresize" eeimg="1">
------------------------------

The lower bound of <img src="https://www.zhihu.com/equation?tex=\ell(x_1)" alt="\ell(x_1)" class="ee_img tr_noresize" eeimg="1"> can be computed as negative of upper
bound of <img src="https://www.zhihu.com/equation?tex=\ell(-x_1)" alt="\ell(-x_1)" class="ee_img tr_noresize" eeimg="1">. The upper bound of <img src="https://www.zhihu.com/equation?tex=\ell(-x_1)" alt="\ell(-x_1)" class="ee_img tr_noresize" eeimg="1"> is:


<img src="https://www.zhihu.com/equation?tex=g(k)=\left(-\frac{a_s\left\lvert x_0\right\rvert}{b_s}+\frac{a_0\left\lvert x_0\right\rvert}{b_0}\right)k-\frac{\left\lvert x_1\right\rvert}{b_s}\\" alt="g(k)=\left(-\frac{a_s\left\lvert x_0\right\rvert}{b_s}+\frac{a_0\left\lvert x_0\right\rvert}{b_0}\right)k-\frac{\left\lvert x_1\right\rvert}{b_s}\\" class="ee_img tr_noresize" eeimg="1">


Thus the lower bound of <img src="https://www.zhihu.com/equation?tex=\ell(x_1)" alt="\ell(x_1)" class="ee_img tr_noresize" eeimg="1"> is: 

<img src="https://www.zhihu.com/equation?tex=\label{eq:min of l(x1)}
    \ell(x_1)\geq\frac{\left\lvert x_1\right\rvert}{b_0}\\" alt="\label{eq:min of l(x1)}
    \ell(x_1)\geq\frac{\left\lvert x_1\right\rvert}{b_0}\\" class="ee_img tr_noresize" eeimg="1">

 By equation
[\[eq:min of f(k)\]](#eq:min of f(k)){reference-type="eqref"
reference="eq:min of f(k)"} and
[\[eq:min of l(x1)\]](#eq:min of l(x1)){reference-type="eqref"
reference="eq:min of l(x1)"}, we conclude that


<img src="https://www.zhihu.com/equation?tex=\ell(x_1)=\frac{\left\lvert x_1\right\rvert}{b_0}\\" alt="\ell(x_1)=\frac{\left\lvert x_1\right\rvert}{b_0}\\" class="ee_img tr_noresize" eeimg="1">



5. Construct of functional <img src="https://www.zhihu.com/equation?tex=\ell(x)" alt="\ell(x)" class="ee_img tr_noresize" eeimg="1">
=================================

In this section, we will construct the explicit form of <img src="https://www.zhihu.com/equation?tex=\ell(x)" alt="\ell(x)" class="ee_img tr_noresize" eeimg="1"> in <img src="https://www.zhihu.com/equation?tex=d" alt="d" class="ee_img tr_noresize" eeimg="1">
dimensional space, the two dimensional form is the special case when
<img src="https://www.zhihu.com/equation?tex=d=2" alt="d=2" class="ee_img tr_noresize" eeimg="1">.

After extending <img src="https://www.zhihu.com/equation?tex=\ell" alt="\ell" class="ee_img tr_noresize" eeimg="1"> to whole space <img src="https://www.zhihu.com/equation?tex=V" alt="V" class="ee_img tr_noresize" eeimg="1">. we obtain <img src="https://www.zhihu.com/equation?tex=d" alt="d" class="ee_img tr_noresize" eeimg="1"> independent
vectors <img src="https://www.zhihu.com/equation?tex=x_1,x_2,\dots,x_d" alt="x_1,x_2,\dots,x_d" class="ee_img tr_noresize" eeimg="1"> and their images
<img src="https://www.zhihu.com/equation?tex=\ell(x_1),\ell(x_2),\ell(x_3),\dots,\ell(x_d)" alt="\ell(x_1),\ell(x_2),\ell(x_3),\dots,\ell(x_d)" class="ee_img tr_noresize" eeimg="1">. Our input bases is
standard basis and output basis is <img src="https://www.zhihu.com/equation?tex=x_1,x_2,\dots,x_d" alt="x_1,x_2,\dots,x_d" class="ee_img tr_noresize" eeimg="1">. Thus the
<img src="https://www.zhihu.com/equation?tex=d\times d" alt="d\times d" class="ee_img tr_noresize" eeimg="1"> matrix of new basis is: 

<img src="https://www.zhihu.com/equation?tex=W=
    \begin{bmatrix}
        x_1 & x_2 & x_3 & \dots & x_d
    \end{bmatrix}\\" alt="W=
    \begin{bmatrix}
        x_1 & x_2 & x_3 & \dots & x_d
    \end{bmatrix}\\" class="ee_img tr_noresize" eeimg="1">

 The image column vectors is: 

<img src="https://www.zhihu.com/equation?tex=L=
    \begin{bmatrix}
        \ell(x_1) & \ell(x_2) & \ell(x_3) & \dots & \ell(x_d)
    \end{bmatrix}^T\\" alt="L=
    \begin{bmatrix}
        \ell(x_1) & \ell(x_2) & \ell(x_3) & \dots & \ell(x_d)
    \end{bmatrix}^T\\" class="ee_img tr_noresize" eeimg="1">

 for any point <img src="https://www.zhihu.com/equation?tex=x" alt="x" class="ee_img tr_noresize" eeimg="1"> we can decompose <img src="https://www.zhihu.com/equation?tex=x" alt="x" class="ee_img tr_noresize" eeimg="1"> as:


<img src="https://www.zhihu.com/equation?tex=\label{decomp:basis}
    x=a_1x_1+a_2x_2+\dots+a_dx_d\\" alt="\label{decomp:basis}
    x=a_1x_1+a_2x_2+\dots+a_dx_d\\" class="ee_img tr_noresize" eeimg="1">

 and apply functional <img src="https://www.zhihu.com/equation?tex=\ell" alt="\ell" class="ee_img tr_noresize" eeimg="1"> we have


<img src="https://www.zhihu.com/equation?tex=\label{decomp:image}
    \ell(x)=a_1\ell(x_1)+a_2\ell(x_2)+\dots+a_d\ell(x_d)\\" alt="\label{decomp:image}
    \ell(x)=a_1\ell(x_1)+a_2\ell(x_2)+\dots+a_d\ell(x_d)\\" class="ee_img tr_noresize" eeimg="1">

 Solve
equation [\[decomp:basis\]](#decomp:basis){reference-type="eqref"
reference="decomp:basis"} and
[\[decomp:image\]](#decomp:image){reference-type="eqref"
reference="decomp:image"} and using matrix form: 

<img src="https://www.zhihu.com/equation?tex=\ell(x)=L^TW^{-1}x\\" alt="\ell(x)=L^TW^{-1}x\\" class="ee_img tr_noresize" eeimg="1">


By conclusion of
subsection [3.2](#subsec:proof separation){reference-type="ref"
reference="subsec:proof separation"}, we choose <img src="https://www.zhihu.com/equation?tex=\gamma" alt="\gamma" class="ee_img tr_noresize" eeimg="1"> as in
equation [\[optimal gamma\]](#optimal gamma){reference-type="ref"
reference="optimal gamma"}. Thus hyperplane <img src="https://www.zhihu.com/equation?tex=\ell(x)=\gamma" alt="\ell(x)=\gamma" class="ee_img tr_noresize" eeimg="1"> will
separate two disjoint sets.

6. Experimental Results
====================

\centering
![Three experimental results for linear
separator.[]{label="fig:experimental"}](gaussian_without_noise.png){#fig:experimental
width="60%"}

\(a) two disjoint gaussian samples

\medskip
\centering
![Three experimental results for linear
separator.[]{label="fig:experimental"}](gaussian_with_noise.png){#fig:experimental
width="60%"}

\(b) two gaussian samples with a little intersection

\medskip
\hfill
\centering
![Three experimental results for linear
separator.[]{label="fig:experimental"}](another_data_set.png){#fig:experimental
width="60%"}

\(c) datasets in python sklearn library

\medskip
In this section, we show three linear separation results. Result (a) and
(b) in
figure [\[fig:experimental\]](#fig:experimental){reference-type="ref"
reference="fig:experimental"} are using bivariate gaussian distributions
where:



<img src="https://www.zhihu.com/equation?tex=\mu_A=\begin{bmatrix*}[r]
        -2 & 0
    \end{bmatrix*}\qquad
    \sigma_A=\begin{bmatrix*}[r]
        3 & 1 \\
        1 & 2
    \end{bmatrix*}\\" alt="\mu_A=\begin{bmatrix*}[r]
        -2 & 0
    \end{bmatrix*}\qquad
    \sigma_A=\begin{bmatrix*}[r]
        3 & 1 \\
        1 & 2
    \end{bmatrix*}\\" class="ee_img tr_noresize" eeimg="1">

 and 

<img src="https://www.zhihu.com/equation?tex=\mu_B=\begin{bmatrix*}[r]
        4 & 5
    \end{bmatrix*}\qquad
    \sigma_B=\begin{bmatrix*}[r]
        4  & 2 \\
        2 & 3
    \end{bmatrix*}\\" alt="\mu_B=\begin{bmatrix*}[r]
        4 & 5
    \end{bmatrix*}\qquad
    \sigma_B=\begin{bmatrix*}[r]
        4  & 2 \\
        2 & 3
    \end{bmatrix*}\\" class="ee_img tr_noresize" eeimg="1">

 Result (a) shows our separator can separate two
disjoint sets accurately. Result (b) shows even the data sets have a
little intersection, our separator still behaves well. Result (c) comes
from iris dataset in the python sklearn library.

7. Discussions
===========

We notice that if <img src="https://www.zhihu.com/equation?tex=A" alt="A" class="ee_img tr_noresize" eeimg="1"> and <img src="https://www.zhihu.com/equation?tex=B" alt="B" class="ee_img tr_noresize" eeimg="1"> are disjoint set, then <img src="https://www.zhihu.com/equation?tex=Conv(A\ominus B)" alt="Conv(A\ominus B)" class="ee_img tr_noresize" eeimg="1">
will not include origin. Conversely, if <img src="https://www.zhihu.com/equation?tex=A" alt="A" class="ee_img tr_noresize" eeimg="1"> and <img src="https://www.zhihu.com/equation?tex=B" alt="B" class="ee_img tr_noresize" eeimg="1"> are not disjoint,
<img src="https://www.zhihu.com/equation?tex=Conv(A\ominus B)" alt="Conv(A\ominus B)" class="ee_img tr_noresize" eeimg="1"> always contains origin. This observation holds even
if we apply a nonlinear feature map on data set. It encourages us to
find a new method to test if two sets are disjoint after applying a
nonlinear feature map.

Considering analysis in
section [4](#sec:bounds analysis){reference-type="ref"
reference="sec:bounds analysis"}, a reasonable guess is in <img src="https://www.zhihu.com/equation?tex=d" alt="d" class="ee_img tr_noresize" eeimg="1">
dimensional space the minimum of <img src="https://www.zhihu.com/equation?tex=f(k_0,k_1,\cdots,k_{d-1})" alt="f(k_0,k_1,\cdots,k_{d-1})" class="ee_img tr_noresize" eeimg="1"> has the
similar form with equation
[\[eq:min of f(k)\]](#eq:min of f(k)){reference-type="eqref"
reference="eq:min of f(k)"}, if we know the equation of hyperplane which
the vector <img src="https://www.zhihu.com/equation?tex=x_0+x_1+\cdots+x_{d-2}" alt="x_0+x_1+\cdots+x_{d-2}" class="ee_img tr_noresize" eeimg="1"> crosses. Then our separator can be
used in <img src="https://www.zhihu.com/equation?tex=d" alt="d" class="ee_img tr_noresize" eeimg="1"> dimensional space.

Our code implementation computes <img src="https://www.zhihu.com/equation?tex=Conv(A\ominus B)" alt="Conv(A\ominus B)" class="ee_img tr_noresize" eeimg="1"> by computing convex
hull of <img src="https://www.zhihu.com/equation?tex=A\ominus B" alt="A\ominus B" class="ee_img tr_noresize" eeimg="1">. For computing convex hull in two dimensional
space, the classical algorithm Graham's scan costs <img src="https://www.zhihu.com/equation?tex=O(n\lg{n})" alt="O(n\lg{n})" class="ee_img tr_noresize" eeimg="1"> time,
and a better algorithm Jarvis's march costs <img src="https://www.zhihu.com/equation?tex=O(nh)" alt="O(nh)" class="ee_img tr_noresize" eeimg="1"> time, where <img src="https://www.zhihu.com/equation?tex=h" alt="h" class="ee_img tr_noresize" eeimg="1"> is
the vertices of convex hull [@cormen2009introduction]. The
prune-and-search algorithm of Kirkpatrick and Seidel uses <img src="https://www.zhihu.com/equation?tex=O(n\lg{h})" alt="O(n\lg{h})" class="ee_img tr_noresize" eeimg="1">
time [@Kirkpatrick:1986:UPC:13535.13555].

However, the size of <img src="https://www.zhihu.com/equation?tex=A\ominus B" alt="A\ominus B" class="ee_img tr_noresize" eeimg="1"> is <img src="https://www.zhihu.com/equation?tex=O(nm)" alt="O(nm)" class="ee_img tr_noresize" eeimg="1"> if the size of <img src="https://www.zhihu.com/equation?tex=A" alt="A" class="ee_img tr_noresize" eeimg="1"> and <img src="https://www.zhihu.com/equation?tex=B" alt="B" class="ee_img tr_noresize" eeimg="1">
are <img src="https://www.zhihu.com/equation?tex=O(n)" alt="O(n)" class="ee_img tr_noresize" eeimg="1"> and <img src="https://www.zhihu.com/equation?tex=O(m)" alt="O(m)" class="ee_img tr_noresize" eeimg="1">. If we compute <img src="https://www.zhihu.com/equation?tex=Conv(A\ominus B)" alt="Conv(A\ominus B)" class="ee_img tr_noresize" eeimg="1"> from <img src="https://www.zhihu.com/equation?tex=Conv(A)" alt="Conv(A)" class="ee_img tr_noresize" eeimg="1">
and <img src="https://www.zhihu.com/equation?tex=Conv(B)" alt="Conv(B)" class="ee_img tr_noresize" eeimg="1">, the time complexity will decrease significantly. Guibas
and Seidel give an algorithm that computing <img src="https://www.zhihu.com/equation?tex=Conv(A\ominus B)" alt="Conv(A\ominus B)" class="ee_img tr_noresize" eeimg="1"> in
<img src="https://www.zhihu.com/equation?tex=O(n_A+m_B+c)" alt="O(n_A+m_B+c)" class="ee_img tr_noresize" eeimg="1"> time in three dimensional case, where <img src="https://www.zhihu.com/equation?tex=n_A" alt="n_A" class="ee_img tr_noresize" eeimg="1"> and <img src="https://www.zhihu.com/equation?tex=m_B" alt="m_B" class="ee_img tr_noresize" eeimg="1"> are
the number of vertices of <img src="https://www.zhihu.com/equation?tex=Conv(A)" alt="Conv(A)" class="ee_img tr_noresize" eeimg="1"> and <img src="https://www.zhihu.com/equation?tex=Conv(B)" alt="Conv(B)" class="ee_img tr_noresize" eeimg="1">, and <img src="https://www.zhihu.com/equation?tex=c" alt="c" class="ee_img tr_noresize" eeimg="1"> is the number
of vertices of <img src="https://www.zhihu.com/equation?tex=Conv(A\ominus B)" alt="Conv(A\ominus B)" class="ee_img tr_noresize" eeimg="1"> [@Guibas:1986:CCR:10515.10525]. A
similar algorithm for higher dimensional space will help to decrease
computing time in higher dimensional space.

\bibliographystyle{plain}
