import doki
import numpy as np
import qsimov as qj
import random as rnd
import sympy as sp
import sys

from random import randint, random

#We create a registry of nq qubits
nq = 5


#reg = qj.QPU(type = "superconductor", topology= "heavy_hex", num_qubits= nq, path = "qpus_falso.db")
reg = qj.QPU(type = "superconductor", topology= "heavy_hex", num_qubits= nq, path = "qpus.db")
#reg = qj.QRegistry(nq)
    
for i in range(nq):
    reg = reg.apply_gate("X", targets = [i])
reg = reg.apply_gate("X", controls = 1, targets = 3)
resultados = []
newreg, result = reg.measure([i for i in range(nq)])

for i in range(nq):
    if result[i]:
        resultados.append(1)
    else:
        resultados.append(0)
print(f'Los resultados son {resultados}')
