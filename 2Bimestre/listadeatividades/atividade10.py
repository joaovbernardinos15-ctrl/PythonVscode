
import numpy as np

temp_c = [25, 28, 30, 22, 24, 31, 29]

celsius = np.array(temp_c)

fahrenheit = celsius * 1.8 + 32

dias = np.sum(fahrenheit > 80)

print("Fahrenheit:", fahrenheit)
print("Dias acima de 80°F:", dias)


