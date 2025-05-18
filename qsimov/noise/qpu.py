from qsimov.structures.qregistry import QRegistry
import sqlite3
import numpy as np

class QPU(QRegistry):

    def __init__(self, type, topology, num_qubits, path ="qpus.db"):
        
        params = noise_param(type, topology, type, path)
        super().__init__(num_qubits, noise = True, noise_params = params)




def noise_param(type, topology, qbit_type, path):
    '''
    Calculates the noise parametres of the qpu
    param = [spam, gf1, gf2, t1, t2]
    spam => Preparation and measurement error
    gf1  => Gate fidelities for gates of 1 qubit
    gf2  => Gate fidelities for gates of 2 qubits
    t1   => Relaxation time in micro s
    t2   => Decoherence time in micro s
    '''
    param = []
    try:
        # Conexión a la base de datos
        conexion = sqlite3.connect(path)
        cursor = conexion.cursor()
        params = ["spam_error", "Gate_fidelity1", "Gate_fidelity2", "t1", "t2"]
        for parametre in params:
            promedio_topology = promedio(cursor, parametre, "topology", topology)
            promedio_type = promedio(cursor, parametre, "qbit_type", qbit_type)
            avg = (promedio_topology+promedio_type)/2
            param.append(round(avg, 10))
        
    except sqlite3.Error as e:
        print("Error al acceder a la base de datos:", e)

    finally:
        if conexion:
            conexion.close()
    
    return param

def promedio(cursor, parametro, campo, valor):

    cursor.execute(f"""
        SELECT {parametro} FROM qpus
        where {campo} = ? 
        """, (valor,))
    parametres = cursor.fetchall()
   
    avg_par = sum(par[0] for par in parametres)/len(parametres)

    return avg_par