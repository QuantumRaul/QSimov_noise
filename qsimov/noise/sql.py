import sqlite3
import os

# Conectar (crea la base de datos si no existe)
conexion = sqlite3.connect("qpus.db")
cursor = conexion.cursor()

# Crear la tabla (si no existe ya)
cursor.execute("""
CREATE TABLE IF NOT EXISTS qpus (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    qbit_type TEXT NOT NULL,
    topology TEXT NOT NULL,
    spam_error FLOAT NOT NULL,
    Gate_fidelity1 FLOAT NOT NULL,
    Gate_fidelity2 FLOAT NOT NULL,
    t1 FLOAT NOT NULL,
    t2 FLOAT NOT NULL                   
)
""")

conexion.commit()
conexion.close()

qpus = [
    ("IBM_Brisbane", "superconductor", "heavy_hex", 0.01465, 0.99979, 0.99, 232.87, 154.33),
    ("IBM_Sherbrooke", "superconductor", "heavy_hex", 0.01611, 0.99981, 0.99, 269.33, 168.71),
    ("IBM_Kyiv", "superconductor", "heavy_hex", 0.01465, 0.99975, 0.991, 277.24, 108.45),
    ("Rigetti_Ankaa3", "superconductor", "square", 0, 1, 0.99, 36, 21),
    ("IonQ_Aria", "ion_trap", "all", 0.0065, 0.9998, 0.985, 100000000, 1000000),
    ("IonQ_Forte", "ion_trap", "all", 0.0065, 0.9998, 0.985, 100000000, 1000000),
    ("IQM_Garnet", "superconductor", "square", 0, 0.9992, 0.9951, 250, 170)
]

conexion = sqlite3.connect("qpus.db")
cursor = conexion.cursor()

cursor.executemany("INSERT INTO qpus (name, qbit_type, topology, spam_error, Gate_fidelity1, Gate_fidelity2, t1, t2) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", qpus)

print(f"El archivo esta en la ruta {os.path.abspath('qpus.db')}")
conexion.commit()
conexion.close()