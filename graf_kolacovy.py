import matplotlib.pyplot as plt
import numpy as np

y = np.array([524250, 530755, 576017, 85126, 170771, 6460])
mylabels = ["Banány", "Jablka", "Pomeranče", "Hrušky","Jahody", "Maliny"]

plt.pie(y, labels = mylabels)
plt.legend(title = "Ovoce:")
plt.show() 