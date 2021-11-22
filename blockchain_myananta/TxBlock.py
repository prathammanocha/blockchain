#TxBlock
from BlockChain import CBlock
class TxBlock (CBlock):
    from Signatures import generate_keys, sign, verify
    from Transactions import Tx
    import pickle
    from cryptography.hazmat.primitives import serialization
    from cryptography.hazmat.backends import default_backend


    
    def __init__(self, previousBlock):
        super(TxBlock, self).__init__([], previousBlock)
    def addTx(self, Tx_in):
        self.data.append(Tx_in)
    def is_valid(self):
        if not super(TxBlock, self).is_valid():
            return False
        for tx in self.data:
            if not tx.is_valid():
                return False
        return True
                

    def main(self):
        pr1, pu1 = self.generate_keys()
        pr2, pu2 = self.generate_keys()
        pr3, pu3 = self.generate_keys()

        Tx1 = self.Tx()
        Tx1.add_input(pu1, 1)
        Tx1.add_output(pu2, 1)
        Tx1.sign(pr1)

        if Tx1.is_valid():
            print("Success! Tx is valid")

        savefile = open("tx.dat", "wb")
        self.pickle.dump(Tx1, savefile)
        savefile.close()

        loadfile = open("tx.dat", "rb")
        newTx = self.pickle.load(loadfile)

        if newTx.is_valid():
            print("Sucess! Loaded tx is valid")
        loadfile.close()

        root = TxBlock(None)
        root.addTx(Tx1)

        Tx2 = self.Tx()
        Tx2.add_input(pu2,1.1)
        Tx2.add_output(pu3, 1)
        Tx2.sign(pr2)
        root.addTx(Tx2)

        B1 = TxBlock(root)
        Tx3 = self.Tx()
        Tx3.add_input(pu3,1.1)
        Tx3.add_output(pu1, 1)
        Tx3.sign(pr3)
        B1.addTx(Tx3)
        
        Tx4 = self.Tx()
        Tx4.add_input(pu1,1)
        Tx4.add_output(pu2, 1)
        Tx4.add_reqd(pu3)
        Tx4.sign(pr1)
        Tx4.sign(pr3)
        B1.addTx(Tx4)

        savefile = open("block.dat", "wb")
        self.pickle.dump(B1, savefile)
        savefile.close()

        loadfile = open("block.dat" ,"rb")
        load_B1 = self.pickle.load(loadfile)

        for b in [root, B1, load_B1, load_B1.previousBlock]:
            if b.is_valid():
                print ("Success! Valid block")
            else:
                print ("ERROR! Bad block")

        B2 = TxBlock(B1)
        Tx5 = self.Tx()
        Tx5.add_input(pu3, 1)
        Tx5.add_output(pu1, 100)
        Tx5.sign(pr3)
        B2.addTx(Tx5)

        load_B1.previousBlock.addTx(Tx4)
        for b in [B2, load_B1]:
            if b.is_valid():
                print ("ERROR! Bad block verified.")
            else:
                print ("Success! Bad blocks detected")  
        
    

    

    
    
