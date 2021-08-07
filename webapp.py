import streamlit as st
import streamlit.components.v1 as components
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import pandas as pd
import seaborn as sns

plt.style.use('ggplot')

st.write("""
# Collatz Conjecture Visualization

## Collatz Conjecture
### Formula:
""")
st.latex(r"""
f(x) = \left\{\begin{matrix}
3x + 1 & \text{if $x$ is odd} \\ \frac{x}{2} & \text{if $x$ is even}
\end{matrix}\right.
""")
st.write("""
### Conjection:
All numbers will end up in the loop 4 - 2 - 1.
## Visualization
(The more complex number, the longer wait time)
""")

def get_sequence(n):
    arr = []
    while n > 1:
        arr.append(n)
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    arr.append(1)
    
    return arr

def animate(i):
    data = df.iloc[:int(i+1)] #select data range
    # For simplicity, I will not plot the scatterplot.
    # p = sns.scatterplot(x=data.index + 1, y='Value', data=data, color='red')
    p = sns.lineplot(x=data.index + 1, y='Value', data=data, color='orange')
    p.tick_params(labelsize=12)
    plt.setp(p.lines,linewidth=2)

n = int(st.text_input("Your number", 100))
arr = get_sequence(n)
df = pd.DataFrame(arr).rename(columns = {0: 'Value'})

fig = plt.figure()

plt.xlim(0, int(len(arr) * 1.05) + 1)
plt.ylim(0, int(np.max(arr) * 1.05) + 1)
plt.title('3n + 1 problem visualization', fontsize=20)

ani = animation.FuncAnimation(fig, animate, frames=len(arr), interval=100, repeat=True)
plt.plot()
components.html(ani.to_jshtml(fps=10), height=550, scrolling=False)