"""
	Author: Hannah Li 7/14/2017
 	Dependencies: randomdotorg, pycrypto
 	pip install randomdotorg, pycrypto
 	Using Python 2.7.10

 	Note: Using a key size of a number larger than 1024 AND is a multiple of 256 is recommended. Since generating a RSA keys involve finding two large, random prime numbers, using random.org's random number generator to help creating a RSA key pair is extremely slow. It also doesn't help we are adding network latency to the generation time. For a faster implementation, consider using pycrypto's native random library. It might also help to fetch a large number of random numbers at once, and try each one of them when finding random prime numbers.  
"""

import randomdotorg
from Crypto.PublicKey import RSA
from datetime import datetime


class RSAKeyGenerator(object):
	"""	
		Generates a RSA public/private key pair using www.random.org's random number generator		

	"""
	
	def __init__(self, key_size=1024):
		"""
			Accepts an optional key_size value  
			:Parameters:
				key_size : int
					RSA key size (in bits) default: 1024, must be a multiple of 256
			
			:Return:
				a RSAKeyGenerator object 
		"""
		if not (key_size % 256 == 0 and key_size >= 1024):
				raise ValueError("RSA key length must be a multiple of 256 and >= 1024")
		else:
			self.key_size = key_size
	

	def generate_rsa_key_pair(self):
		"""
			Generates a RSA key pair and prints them to terminal
		"""
		print "Started rsa key generation"
		key = RSA.generate(self.key_size, randfunc=self.random_number_generator)
			
		pub_key = key.publickey().exportKey()
		print pub_key
		

		priv_key = key.exportKey()
		print "Private key", priv_key 
		print "Note: Normally, the private key should be protected. For the purposes of this demo, I'm printing it to terminal."
	
	def random_number_generator(self, n):
		"""
			:Parameters:
				n : int
					number of random bytes to be generated 
			:Return:
				a string of n bytes of random number generated using random.org
		"""
		r = randomdotorg.RandomDotOrg('RSAKeyGenerator') 
		return str(hex(r.getrandbits(n*8)))[2:]
		

if __name__ == '__main__':
	print "Demo testing RSA key pair generator"
	start=datetime.now()
	rsakeygenerator = RSAKeyGenerator() #add optional key_size length: rsakeygenerator = RSAKeyGenerator(1024)
	rsakeygenerator.generate_rsa_key_pair()
	print "Completed in: ", str(datetime.now()-start)
