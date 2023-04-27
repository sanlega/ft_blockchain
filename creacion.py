import hashlib
import time

def crear_bloque(transacciones, version, prev_block, bits, dificultad):
    # Crea un diccionario que represente el objeto de bloque
    bloque = {
        "version": version,
        "prev_block": prev_block,
        "merkle_root": "",
        "timestamp": int(time.time()),
        "bits": bits,
        "nonce": 0,
        "transactions": transacciones,
    }

    # Calcula el Merkle Root de las transacciones
    hashes = [hashlib.sha256(str(tx).encode()).hexdigest() for tx in transacciones]
    while len(hashes) > 1:
        if len(hashes) % 2 != 0:
            hashes.append(hashes[-1])
        hashes = [hashlib.sha256((hashes[i] + hashes[i+1]).encode()).hexdigest() for i in range(0, len(hashes), 2)]
    merkle_root = hashes[0]
    bloque["merkle_root"] = merkle_root

    # Ejecuta el algoritmo de Prueba de Trabajo para encontrar un nonce válido
    while True:
        bloque_str = str(bloque).encode()
        block_hash = hashlib.sha256(bloque_str).hexdigest()
        if block_hash[:dificultad] == "0" * dificultad:
            bloque["nonce"] = nonce
            bloque["block_hash"] = block_hash
            return bloque
        nonce += 1
