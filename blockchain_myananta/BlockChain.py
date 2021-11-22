#BlockChain.py
class Blockchain:    
    from cryptography.hazmat.backends import default_backend
    from cryptography.hazmat.primitives import hashes

    class someClass:
        string = None
        num = 328965
        def __init__(self, mystring):
            self.string = mystring
        def __repr__(self):
            return self.string + "^^^" + str(self.num)

    class CBlock:
        data = None
        previousHash = None
        previousBlock = None
        def __init__(self, data, previousBlock):
            self.data = data
            self.previousBlock = previousBlock
            if previousBlock != None:
                self.previousHash = previousBlock.computeHash()
        def computeHash(self):
            digest = self.hashes.Hash(self.hashes.SHA256(), backend=self.default_backend())
            digest.update(bytes(str(self.data),'utf8'))
            digest.update(bytes(str(self.previousHash),'utf8'))
            return digest.finalize()

        def main(self):    
            root = self.CBlock('I am root', None)
            B1 = self.CBlock(b'I am a child.', root)
            B2 = self.CBlock('I am B1s brother', root)
            B3 = self.CBlock(12354, B1)
            B4 = self.CBlock(self.someClass('Hi there!'), B3)
            B5 = self.CBlock("Top block", B4)

            for b in [B1, B2, B3, B4, B5]:    
                if b.previousBlock.computeHash() == b.previousHash:
                    print ("Success! Hash is good.")
                else:
                    print ("ERROR! Hash is no good.")

            B3.data=12345
            if B4.previousBlock.computeHash() == B4.previousHash:
                print ("ERROR! Couldn't detect tampering.")
            else:
                print ("Success! Tampering detected.")
                
            print(B4.data)
            B4.data.num = 99999
            print(B4.data)
            if B5.previousBlock.computeHash() == B5.previousHash:
                print ("ERROR! Couldn't detect tampering.")
            else:
                print ("Success! Tampering detected.")
            
        
        

