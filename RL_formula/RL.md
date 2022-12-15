$ y = \frac{1}{1+exp(-x)} $

$$
Q学習　\\
Q(s_t,a_t) \leftarrow Q(s_t,a_t) + \eta\left(R_{t+1}+\gamma \max_{a}Q(s_{t+1}, a) - Q(s_{t}, a_{t})\right) 
$$