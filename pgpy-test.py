from pgpy.constants import PubKeyAlgorithm, KeyFlags, HashAlgorithm, SymmetricKeyAlgorithm, CompressionAlgorithm
import pgpy
from time import sleep

# we can start by generating a primary key. For this example, we'll use RSA, but it could be DSA or ECDSA as well
key = pgpy.PGPKey.new(PubKeyAlgorithm.RSAEncryptOrSign, 4096)
keyUserName=str(input("Please enter a name: "))
keyUserName="ollie"
#keyComment=str(input("enter a comment: "))
keyComment="no"
#keyEmail=str(input("enter an email: "))
keyEmail="email@email.com"
# we now have some key material, but our new key doesn't have a user ID yet, and therefore is not yet usable!
uid = pgpy.PGPUID.new(keyUserName, comment=keyComment, email=keyEmail)

# now we must add the new user id to the key. We'll need to specify all of our preferences at this point
# because PGPy doesn't have any built-in key preference defaults at this time
# this example is similar to GnuPG 2.1.x defaults, with no expiration or preferred keyserver
key.add_uid(uid, usage={KeyFlags.Sign, KeyFlags.EncryptCommunications, KeyFlags.EncryptStorage},
            hashes=[HashAlgorithm.SHA256, HashAlgorithm.SHA384, HashAlgorithm.SHA512, HashAlgorithm.SHA224],
            ciphers=[SymmetricKeyAlgorithm.AES256, SymmetricKeyAlgorithm.AES192, SymmetricKeyAlgorithm.AES128],
            compression=[CompressionAlgorithm.ZLIB, CompressionAlgorithm.BZ2, CompressionAlgorithm.ZIP, CompressionAlgorithm.Uncompressed])

keyname=input("Please enter name of key: ")

with open(str(keyname)+"-private.asc", "w") as f:
    f.write(str(key))

with open(str(keyname)+"-public.asc", "w") as ff:
    ff.write(str(key.pubkey))


sleep(1)
print("\n\n")
sleep(1)

#reading in key from file and ecrypting it then decrypting
PRIVATE_KEY_FILE=str(keyname)+"-private.asc"
priKey, _ = pgpy.PGPKey.from_file(str(PRIVATE_KEY_FILE))
print("private key is:")
print(priKey)
testmsg=pgpy.PGPMessage.new("test msg")
encrypted_test = str(priKey.pubkey.encrypt(testmsg))
print("encrypted message is: ")
print(encrypted_test)
with open("currentMsg.asc", "w") as x1:
    x1.write(encrypted_test)
msg2 = pgpy.PGPMessage.from_blob(encrypted_test)
decrypted_test=priKey.decrypt(msg2)
print("decrypted message is: "+str(decrypted_test.message))
#https://stackoverflow.com/questions/62858697/encrypt-decrypt-message-using-pgpy#63434142
