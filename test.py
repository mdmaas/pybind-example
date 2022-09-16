import sys
sys.path.append("build/")
from MyLib import MyClass

import matplotlib.pyplot as plt

Simulation = MyClass(-4,4,1000)
Simulation.run()

plt.plot(Simulation.v_data, Simulation.v_gamma, \
"--", linewidth = 3, color=(1,0,0,0.6),label="Function Value")
plt.ylim(-10,10)
plt.xlabel("x")
plt.ylabel("($f(x) = \gamma(x)$)")
plt.title("(Gamma Function: $\gamma(z) = \int_0^\infty x^{z-1} e^{-x} dx$)",fontsize = 18);
plt.show()


 
