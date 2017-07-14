# RSAKeyPairGenerator
Generates a RSA key pair using random.org's random number generator
Using Python 2.7.10

## Dependencies: python libraries randomdotorg, pycrypto   	
 	pip install randomdotorg, pycrypto
  
## Instructions:
  python generateRSAKeyPair.py
  
Note: Using key size of a number larger than 1024 AND is a multiple of 256 is required. Since generating a RSA keys involve finding two large, random prime numbers, using random.org's random number generator to help creating a RSA key pair is extremely slow (1/2 minute for a key size of 1024). It also doesn't help we are adding network latency to the generation time. 

For a faster implementation, consider using pycrypto's native random library. It might also help to fetch a large number of random numbers at once, and try each one of them when finding random prime numbers.  

