from Pychain import BlockChain

blockchain = BlockChain()

print("_______Mining about to start______")
print(blockchain.chain)

last_block = blockchain.latest_block
last_proof_no = last_block.proof_no
proof_no = blockchain.proof_of_work(last_proof_no)

blockchain.new_data(
    sender="0",  #node created a new block
    recipient="R Pi", # receiver name 
    quantity=
    1,  #creating a new block (or identifying the proof number) is awarded with 1
)

last_hash = last_block.calculate_hash
block = blockchain.construct_block(proof_no, last_hash)

print("______Mining successful_______")
print(blockchain.chain)