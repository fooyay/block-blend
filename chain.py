import streamlit as st
from datetime import datetime
from dataclasses import dataclass
from typing import List, Any
import hashlib

@dataclass
class Block:
    data: Any
    creator_id: int
    prev_hash: str = "0"
    timestamp: str = datetime.utcnow().strftime("%H:%M:%S")

    # Create a method called hash_block
    def hash_block(self):
        sha = hashlib.sha256()

        # Turn the block data into an encoded string
        data = str(self.data).encode()
        sha.update(data)

        # Turn the block timestamp into an encoded string
        timestamp = str(self.timestamp).encode()
        sha.update(timestamp)

        prev_hash = str(self.prev_hash).encode()
        sha.update(prev_hash)
        
        return sha.hexdigest()

@dataclass
class PyChain:
    chain: List[Block]

    def add_block(self, block):
        self.chain += [block]

@st.cache(allow_output_mutation=True)
def setup():
    return PyChain([Block(data="Genesis", creator_id=0)])
pychain = setup()

print(pychain)

prev_block = pychain.chain[-1]
prev_block_hash = prev_block.hash_block()
new_block = Block(data="new_block", creator_id = 42, prev_hash = prev_block_hash)
pychain.add_block(new_block)
print(pychain)