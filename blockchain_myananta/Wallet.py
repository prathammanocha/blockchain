class wallet:

    import SocketUtils
    import Transactions
    import Signatures

    def wallet_init(self):    

        head_blocks = [None]

        pr1,pu1 = self.Signatures.generate_keys()
        pr2,pu2 = self.Signatures.generate_keys()
        pr3,pu3 = self.Signatures.generate_keys()

        Tx1 = self.Transactions.Tx()
        Tx2 = self.Transactions.Tx()

        Tx1.add_input(pu1, 4.0)
        Tx1.add_input(pu2, 1.0)
        Tx1.add_input(pu3, 4.8)
        Tx2.add_input(pu3, 4.0)
        Tx2.add_output(pu2, 4.0)
        Tx2.add_reqd(pu1)

        Tx1.sign(pr1)
        Tx1.sign(pr2)
        Tx2.sign(pr3)
        Tx2.sign(pr1)

        try:
            self.SocketUtils.sendObj('localhost',Tx1)
            self.SocketUtils.sendObj('localhost',Tx2)
        except:
            print ("Error! Connection unsuccessful")

        server = self.SocketUtils.newServerConnection('localhost',5006)
        for i in range(10):
            newBlock = self.SocketUtils.recvObj(server)
            if newBlock:
                break
        server.close()

        if newBlock.is_valid():
            print("Success! Block is valid")
        if newBlock.good_nonce():
            print("Success! Nonce is valid")
        for tx in newBlock.data:
            if tx == Tx1:
                    print("Tx1 is present")
            if tx == Tx2:
                    print("Tx2 is present")

        



