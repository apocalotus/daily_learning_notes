## Decentralized Partially Observable Markov Decision Process
model $
G = (S, U, P, r, Z, O, n, \gamma) 
$

S: true state of the environment

U: joint action

r: general reward funtion $r(s,u): S \times U \rightarrow R$

Finnaly, each agent has a partial observation described  by $o^i \in O$, which is derived from the observation function $Z(o^i| s, u^i) : S \times U \rightarrow O$

All agents work cooperatively to maximize the shared global reward $R_t = \Sigma \gamma^k r_{t+k}$, which is described by the joint value function $Q^\pi (s_t, u_t) = \mathbb{E}_{s_{t+1 : \infin}, u_{t+1 : \infin}} [R_t | s_t, u_t]$

## Centralized Training with Decentralized Execution and Value Decomposition

### Individual-Global-Max (IGM) principle

$$
argmax_{u} Q_{tot} (\tau, u) = (argmax_{u_1} Q_1 (\tau_1, u_1), ... , argmax_{u_n} Q_n (\tau_n, u_n) )
$$

The simplest factorization structure, called *additivity*, has been proposed by VDN, wchich makes VDN simply factorize $Q_{tot}$ into a su of peragent utilities.

## QMIX and Monotonicity Constraint

<div align="center">
<img src=assets/qmix_frame-800.webp  width=90%/>

<div style="color:orange; border-bottom: 1px solid #d9d9d9;
    display: inline-block;
    color: #999;
    padding: 2px;">Figure 4: Framework of QMIX. (Image source: QMIX
). On the left is Mixing Network (A Hypernetwork), and on the right is the Agent network.</div>

<br>


<img src=assets/basic1.png  width=50%/>

<div style="color:orange; border-bottom: 1px solid #d9d9d9;
    display: inline-block;
    color: #999;
    padding: 2px;">Monotonicity Constraint</div></div>

<br>


## Tricks in RL

To facilitate the study of proper techniques affecting the training effectiveness and sample efficiency of QMIX, we perform a set of experiments designed to provide insight into some methods that have been proven effectiveness in single-agent RL but may be ambiguous in MARL.

+ Adam optimizer with paralletl rollout process
+ the number of parallel rollout process
+ incremental replay buffer size
+ $\epsilon-$ exploration steps
+ the implementation of eligiblity traces methods, e.g. $Q(\lambda), TD(\lambda)$, in centralized value function
+ the hidden size of the recurrent network of agents
