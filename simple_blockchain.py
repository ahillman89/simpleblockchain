# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 21:31:03 2023

@author: alexa
"""

import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, timestamp, data, hash):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash


def calculate_hash(index, previous_hash, timestamp, data):
    return hashlib.sha256(f'{index}{previous_hash}{timestamp}{data}'.encode('utf-8')).hexdigest()


def create_genesis_block():
    # Manually construct a block with index zero and arbitrary previous hash
    return Block(0, '0', time.time(), 'Genesis Block', calculate_hash(0, '0', time.time(), 'Genesis Block'))


def create_new_block(prev_block, data):
    index = prev_block.index + 1
    timestamp = time.time()
    hash = calculate_hash(index, prev_block.hash, timestamp, data)
    return Block(index, prev_block.hash, timestamp, data, hash)


# Create blockchain and add genesis block
blockchain = [create_genesis_block()]
previous_block = blockchain[0]

# Add blocks to the blockchain
num_blocks = 10
for i in range(1, num_blocks + 1):
    new_data = f"Block #{i} data"
    new_block = create_new_block(previous_block, new_data)
    blockchain.append(new_block)
    previous_block = new_block
    print(f"Block #{new_block.index} has been added to the blockchain!")
    print(f"Hash: {new_block.hash}\n")

# Verification
def verify_blockchain(blockchain):
    for i in range(1, len(blockchain)):
        current_block = blockchain[i]
        previous_block = blockchain[i - 1]
        if current_block.previous_hash != previous_block.hash or \
           current_block.hash != calculate_hash(current_block.index, current_block.previous_hash, current_block.timestamp, current_block.data):
            return False
    return True

print(f"Blockchain is valid: {verify_blockchain(blockchain)}")

