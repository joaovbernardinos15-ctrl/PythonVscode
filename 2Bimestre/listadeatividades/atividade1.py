
import numpy as np

notas_lista = [8.5, 7.0, 9.5, 6.0, 10.0]

notas = np.array(notas_lista)

print("Tipo:", type(notas))
print("Média:", np.mean(notas))
