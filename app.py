# learning streamlit for the Block-Bend course
import streamlit as st
import pandas as pd
from dataclasses import dataclass
from datetime import datetime
from typing import Any
import hashlib

@dataclass
class Block:
    data: Any
    creator_id: int
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

        return sha.hexdigest()

# creating a new block
new_block = Block(data="My first block!", creator_id=42)

# print the new block
print(new_block)

# Create a new block instance using some test data
new_block = Block(data="test", creator_id=42)

# Calculate the block hash using the new method
block_hash = new_block.hash_block()

# Print the block's hash
print(block_hash)

st.write("# Python Web App")

st.write("My first web app in python! :sunglasses: :monkey: :cat: :white_check_mark: :joy: :thumbsup::rocket:")

df = pd.DataFrame({'col1': [1,2], 'col2': [3,4]})

st.write(df)

input_value = st.text_input("Enter a message")

if(st.button("Display Message")):
    st.write(input_value)

    sha = hashlib.sha256()
    encoded_data = input_value.encode()
    sha.update(encoded_data)
    st.write(sha.hexdigest())

@dataclass
class Counter:
    count: int = 0

    def update_count(self):
        self.count = self.count + 1


new_counter= Counter()

new_counter.update_count()
new_counter.update_count()
print("The new count is: ", new_counter.count)
