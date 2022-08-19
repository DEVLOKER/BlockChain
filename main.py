import os
#import Blockchain
from Blockchain import *
from Block import *
from Transaction import *
from Client import *
import json
import datetime
import time

print("##################### Blockchain System #####################")

startTimer = time.time() # datetime.datetime.now().timestamp()

client1 = Client()
client2 = Client()
transation1 = Transaction(client1, client2, 5.0)
transation2 = Transaction(client2, client1, 2.0)

difficulty = 0
blockChainSystem = Blockchain(difficulty) 
#print(blockChainSystem.last_block()) #print(blockChainSystem.chain[0])
block0 = Block(blockChainSystem.last_block().compute_hash())
block0.addTrasaction(transation1)
block0.addTrasaction(transation2)
blockChainSystem.add_block(block0)

endTimer = time.time()

for i, block_ in enumerate(blockChainSystem.chain):
	blck = block_.__dict__()
	print("\n____________________________ Block N° ",str(blck['id'])," \n")
	print(json.dumps(blck, indent=4, sort_keys=True))

print("chain is valid? : ", blockChainSystem.check_chain_validity())

print('execution time : ', format(endTimer-startTimer, '.6f'),' ms')

os.system("pause")