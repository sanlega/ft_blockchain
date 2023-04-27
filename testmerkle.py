import hashlib

def merkle_tree(string):
    # Convert the string to bytes
    if isinstance(string, bytes):
        bytes_string = string
    else:
        bytes_string = bytes(string, 'utf-8')

    # Create a list of leaf nodes (hashes of the individual bytes)
    leaf_nodes = [hashlib.sha256(bytes([byte])).hexdigest() for byte in bytes_string]

    # Create a list to hold the current layer of the tree
    current_layer = leaf_nodes

    # Build up the tree by repeatedly hashing pairs of nodes until we reach the root
    while len(current_layer) > 1:
        next_layer = []
        for i in range(0, len(current_layer), 2):
            left_child = current_layer[i]
            right_child = current_layer[i+1] if i+1 < len(current_layer) else current_layer[i]
            parent_hash = hashlib.sha256(bytes.fromhex(left_child + right_child)).hexdigest()
            next_layer.append(parent_hash)
        current_layer = next_layer

    # The last item in the list is the root hash of the tree
    root_hash = current_layer[0]

    return root_hash

input_string = "Hello, world!"
root_hash = merkle_tree(input_string)
print(root_hash)
