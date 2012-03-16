import primes
import numpy as np


def count( n, m ):

        table = np.ones(n+1,m+1)*(-1)

        table[:,0]=1
        
        for i from 0 to n:
                for j from 0 to m:
                        table[ i, j ] = table[ i - primes.prime(j), j ] + table[ i, j - 1 ]

        return table[ n, m ]