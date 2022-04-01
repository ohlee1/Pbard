from pgpy.constants import PubKeyAlgorithm, KeyFlags, HashAlgorithm, SymmetricKeyAlgorithm, CompressionAlgorithm
import pgpy

# we can start by generating a primary key. For this example, we'll use RSA, but it could be DSA or ECDSA as well
key = pgpy.PGPKey.new(PubKeyAlgorithm.RSAEncryptOrSign, 4096)

# we now have some key material, but our new key doesn't have a user ID yet, and therefore is not yet usable!
uid = pgpy.PGPUID.new('Abraham Lincoln', comment='Honest Abe', email='abraham.lincoln@whitehouse.gov')

# now we must add the new user id to the key. We'll need to specify all of our preferences at this point
# because PGPy doesn't have any built-in key preference defaults at this time
# this example is similar to GnuPG 2.1.x defaults, with no expiration or preferred keyserver
key.add_uid(uid, usage={KeyFlags.Sign, KeyFlags.EncryptCommunications, KeyFlags.EncryptStorage},
            hashes=[HashAlgorithm.SHA256, HashAlgorithm.SHA384, HashAlgorithm.SHA512, HashAlgorithm.SHA224],
            ciphers=[SymmetricKeyAlgorithm.AES256, SymmetricKeyAlgorithm.AES192, SymmetricKeyAlgorithm.AES128],
            compression=[CompressionAlgorithm.ZLIB, CompressionAlgorithm.BZ2, CompressionAlgorithm.ZIP, CompressionAlgorithm.Uncompressed])

keyname=input("Please enter name of key: ")

with open(str(keyname)+"-private.txt", "w") as f:
    f.write(str(key))

with open(str(keyname)+"-public.txt", "w") as ff:
    ff.write(str(key.pubkey))

txt_msg = pgpy.PGPMessage.new("Hello PGPy World")
print('txt_msg.is_encrypted')
print(txt_msg.is_encrypted)
print('txt_msg.message')
print(txt_msg.message)
encrypted_txt_msg = key.pubkey.encrypt(txt_msg)
print('encrypted_txt_msg.is_encrypted')
print(encrypted_txt_msg.is_encrypted)
print('encrypted_txt_msg.message\n\n')
print(type(encrypted_txt_msg.message))
print(str(encrypted_txt_msg))