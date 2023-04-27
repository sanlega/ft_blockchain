# Implementar merkle blocks para almacenar las transaciones

####################### EJEMPLO #######################

import hashlib

# Generando una lista de transacciones como esta:
transactions = [
    {"id": "tx1", "input": "A", "output": "B", "amount": 10},
    {"id": "tx2", "input": "C", "output": "D", "amount": 20},
    {"id": "tx3", "input": "E", "output": "F", "amount": 30},
    {"id": "tx4", "input": "G", "output": "H", "amount": 40},
]

# Convertimos cada transacción en su forma de hash
hashes = [hashlib.sha256(str(tx).encode()).hexdigest() for tx in transactions]

# Organizamos los hashes en pares y aplica la función de hash
while len(hashes) > 1:
    if len(hashes) % 2 != 0:
        hashes.append(hashes[-1])
    hashes = [hashlib.sha256((hashes[i] + hashes[i+1]).encode()).hexdigest() for i in range(0, len(hashes), 2)]

# El último hash es el Merkle Root
merkle_root = hashes[0]

# Creamos el objeto Merkle Block
merkle_block = {
    "prev_block": "0000000000000000000000000000000000000000000000000000000000000000",
    "merkle_root": merkle_root,
    "timestamp": 1234567890,
    "bits": 12345,
    "nonce": 67890,
    "transactions": transactions,
}

# Calculamos el hash del objeto Merkle Block completo
block_hash = hashlib.sha256(str(merkle_block).encode()).hexdigest()

# Imprimimos el Merkle Root y el hash del bloque completo
print("Merkle Root:", merkle_root)
print("Block Hash:", block_hash)


####################### IMPLEMENTACIÓN BLOQUES #######################

import hashlib

def crear_bloque(version, prev_block, merkle_root, timestamp, bits, nonce, transactions):
    # Crea un diccionario que representa el objeto de bloque
    bloque = {
        "version": version,
        "prev_block": prev_block,
        "merkle_root": merkle_root,
        "timestamp": timestamp,
        "bits": bits,
        "nonce": nonce,
        "transactions": transactions,
    }
    
    # Calcula el hash SHA-256 del objeto de bloque completo y agrega el hash al diccionario
    bloque_str = str(bloque).encode()
    block_hash = hashlib.sha256(bloque_str).hexdigest()
    bloque["block_hash"] = block_hash
    
    # Devuelve el diccionario que representa el objeto de bloque completo
    return bloque
