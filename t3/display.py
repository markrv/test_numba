import matplotlib as mpl
import matplotlib.pyplot as plt
from t3.run3 import go, go_fast

# Plot
# ns = range(100000, 4000000, 100000)
# plt.ylabel('сек')
# plt.xlabel('N')
# plt.plot(ns, [go(n) for n in ns], label='cpu')
# plt.plot(ns, [go_fast(n) for n in ns], label='gpu')
# plt.legend()
# plt.show()
print(go_fast(100))