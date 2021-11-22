#Signatures.py
class signatures:

    from cryptography.hazmat.backends import default_backend
    from cryptography.hazmat.primitives.asymmetric import rsa
    from cryptography.hazmat.primitives import hashes
    from cryptography.hazmat.primitives.asymmetric import padding
    from cryptography.exceptions import InvalidSignature

    def generate_keys(self):
        private = self.rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=self.default_backend()
        )    
        public = private.public_key()
        return private, public

    def sign(self, message, private):
        message = bytes(str(message), 'utf-8')
        sig = private.sign(
            message,
            self.padding.PSS(
                mgf=self.padding.MGF1(self.hashes.SHA256()),
                salt_length=self.padding.PSS.MAX_LENGTH
            ),
            self.hashes.SHA256()
        )
        return sig

    def verify(self, message, sig, public):
        message = bytes(str(message), 'utf-8')
        try:
            public.verify(
                sig,
                message,
                self.padding.PSS(
                mgf=self.padding.MGF1(self.hashes.SHA256()),
                salt_length=self.padding.PSS.MAX_LENGTH
                ),
                self.hashes.SHA256()
            )
            return True
        except self.InvalidSignature:
            return False
        except:
            print("Error executing public_key.verify")
            return False
        

    def main(self):
        pr,pu = self.generate_keys()
        print(pr)
        print(pu)
        message = "This is a secret message"
        sig = self.sign(message, pr)
        print(sig)
        correct = self.verify(message, sig, pu)
        print(correct)

        if correct:
            print("Success! Good sig")
        else:
            print ("ERROR! Signature is bad")

        pr2, pu2 = self.generate_keys()

        sig2 = self.sign(message, pr2)

        correct= self.verify(message, sig2, pu)
        if correct:
            print("ERROR! Bad signature checks out!")
        else:
            print("Success! Bad sig detected")

        badmess = message + "Q"
        correct= self.verify(badmess, sig, pu)
        if correct:
            print("ERROR! Tampered message checks out!")
        else:
            print("Success! Tampering detected")
        
        
        
            
        
