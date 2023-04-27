
import hashlib
import matplotlib.pyplot as plt
import matplotlib.patches as patches

class Block:
    def __init__(self, index, previous_hash, data):
        self.index = index
        self.previous_hash = previous_hash
        self.data = data
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        return hashlib.sha256(f"{self.index}{self.previous_hash}{self.data}".encode('utf-8')).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, "0", "Genesis Block")

    def add_block(self, data):
        last_block = self.chain[-1]
        new_block = Block(len(self.chain), last_block.hash, data)
        self.chain.append(new_block)

def visualize_blockchain(blockchain):
    fig, ax = plt.subplots()
    for index, block in enumerate(blockchain.chain):
        rect = patches.Rectangle((index * 100, 50), 80, 50, linewidth=1, edgecolor='black', facecolor='cyan')
        ax.add_patch(rect)
        ax.annotate(f"Block {block.index}", (index * 100 + 20, 75), fontsize=10, fontweight='bold')
        ax.annotate(f"Hash:", (index * 100 + 5, 60), fontsize=8)
        ax.annotate(block.hash[:6], (index * 100 + 40, 60), fontsize=8, color='blue')
        if index > 0:
            plt.arrow(index * 100 - 20, 75, 20, 0, width=0.5, head_width=3, head_length=5, color='black')
    plt.xlim(0, len(blockchain.chain) * 100)
    plt.ylim(0, 150)
    plt.axis('off')
    plt.title("Representación gráfica de una blockchain")
    plt.show()

if __name__ == "__main__":
    my_blockchain = Blockchain()
    my_blockchain.add_block("Block 1 data")
    my_blockchain.add_block("Block 2 data")
    my_blockchain.add_block("Block 3 data")

    visualize_blockchain(my_blockchain)
