import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import streamlit as st
import sympy as sp
from sympy.core.power import Pow

# F(n) Calculation

@st.cache
def evaluate_binet(n_val):
    Phi = sp.symbols('Phi') # Golden ratio
    n = sp.symbols('n')
    # Binet's formula for calculating n'th fibonnacci symbol
    binet = (Phi**n - ((-1)**n)/(Phi**n)) / Pow(sp.Integer(5), sp.Float(0.5))
    Phi_val = (sp.Integer(1) + Pow(sp.Integer(5), sp.Float(0.5))) / sp.Integer(2)
    return binet.evalf(subs={'Phi': Phi_val, 'n':n_val})


# Visualisation
st.header('Fibonacci numbers for real indices')

lower_bound = st.sidebar.number_input('Lower Bound', value=-7)
upper_bound = st.sidebar.number_input('Upper Bound', value=7)
resolution = st.sidebar.number_input('Resolution', value=200)

imag = st.sidebar.number_input('+ imaginary constant', value=0.0, step=0.01)

interval = np.linspace(lower_bound, upper_bound, resolution)
fibonnaccis = []
for i in interval:
    fibonnaccis.append(evaluate_binet(i+imag*1j).as_real_imag())
fibonnaccis = np.array(fibonnaccis)


fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d')
ax.plot(interval, fibonnaccis[:, 0], fibonnaccis[:, 1])

show_int = st.sidebar.checkbox('Show integer values', value=True)
if show_int:
    fibonnaccis_int = []
    for i in range(lower_bound, upper_bound+1):
        fibonnaccis_int.append(evaluate_binet(i).as_real_imag())
    fibonnaccis_int = np.array(fibonnaccis_int)
    ax.scatter(
        xs=list(range(lower_bound, upper_bound+1)),
        ys=fibonnaccis_int[:, 0],
        marker='o',
        color='orange'
    )

ax.set_xlabel('idx')
ax.set_ylabel('res r')
ax.set_zlabel('res i')

# rotate the axes
v_angle = st.sidebar.slider('v_angle', 0, 360, 30)
h_angle = st.sidebar.slider('h_angle', 0, 360, 0)
ax.view_init(v_angle, h_angle)
st.pyplot(fig)