# Bellman Operator

In RL, we discuss Bellman Policy Operator $B_{\pi}$ and Bellman Optimality Operator $B_{*}$

$v$ is a value funtion,

Bellman Policy Operator
$$B_{\pi} = R_{\pi} + \gamma P_{\pi} \cdot v $$

$B_{\pi}$ has fixed point $v_{\pi}$, s.t
$$B_{\pi}v_{\pi} = v_{\pi}$$

Bellmon Optimality Operator

Definition:
$$(B_{*}v) = max_{a} \{ \mathcal{R^{a}_{s} + \gamma \Sigma_{s^{\prime} \in \mathcal{S}} \mathcal{P^{a}_{s, s^{\prime}}} \cdot v(s^{\prime}) } \}$$

Similarly, $B_{*}$ also has fixed point $v_{*}$

Here we define a greedy policy $G(v)(s)$

$G(v)(s) := argmax_{a} \{ \mathcal{R^{a}_{s} + \gamma \Sigma_{s^{\prime} \in \mathcal{S}} \mathcal{P^{a}_{s, s^{\prime}}} \cdot v(s^{\prime}) } \}$

## Contraction property & monotonicity

$B_{\pi}, B_{*}$ is $\gamma$ - contraction operators in $L^{\infin}$
, 

which implies $B_{\pi}, B_{*}$ have unique fixed point

## Solution to DP Problems

### Policy Evalution

$$lim_{N \rightarrow \infin} B^{N}_{\pi} v = v_{\pi}$$

### Policy Improvement

Consider Greedy Policy $\pi_{k+1} \space s.t.$
$$\pi_{k+1} = G(v_{k})$$

Consider $B_{G(v)} v = B_{*}v$
, then

$$B_{*} v_{\pi_{k}} =  B_{G(v_{\pi_{k}} )} v_{\pi_{k}} = B_{\pi_{k+1}} v_{\pi_{k}} $$

According to  definition of Bellman Optimality Operator,

$B_{\pi_{k+1}} v_{\pi_{k}} \ge v_{\pi_k}$ , then

$$v_{\pi_{k+1}} = lim_{N \rightarrow \infin} B^{N}_{*}v_{\pi_{k}} = lim_{N \rightarrow \infin} B^{N}_{\pi_{k+1}}v_{\pi_{k}}$$

$$ v_{\pi_{k+1}} = lim_{N \rightarrow \infin} B^{N}_{\pi_{k+1}}v_{\pi_{k}} \ge v_{\pi_k}$$


### Policy Iteration
Earlier, we have $v_{\pi_{k+1}}  \ge v_{\pi_k}$. 

Therefore, when $v_{\pi_{k+1}} = v_{\pi_k}$, we found $v_{*} = v_{\pi_k}$

## Value Iteration

Due to monotonictiy of $B_{*}$, we have

$lim_{N \rightarrow \infin} B^N_{*} v = v_{*}$

### Optimality of Value Iteration

Greedy Policy from Optimal VF(value function) is an Optimal Policy.


