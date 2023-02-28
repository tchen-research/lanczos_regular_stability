import numpy as np
import scipy as sp

def GOE_tridiag_model(n,k=-1):
    """
    n : int, size of T
    k : int, size of Tk
    """
    if k==-1:
        k=n
    
    a = np.random.normal(size=k,scale=np.sqrt(2))
    b = np.zeros(k-1)
    for j in range(k-1):
        b[j] = np.random.chisquare(df=(n-(j+1)))
    
    b = np.sqrt(b) / (2*np.sqrt(n))
    a = a / (2*np.sqrt(n))
    
    return sp.sparse.spdiags(a,0,k,k) + sp.sparse.spdiags(b,1,k,k) + sp.sparse.spdiags(b,-1,k,k)

def GOE_tridiag_model(n,k=-1):
    """
    n : int, size of T
    k : int, size of Tk
    """
    if k==-1:
        k=n
    
    a = np.random.normal(size=k,scale=np.sqrt(2))
    b = np.zeros(k-1)
    for j in range(k-1):
        b[j] = np.random.chisquare(df=(n-(j+1)))
    
    b = np.sqrt(b) / (2*np.sqrt(n))
    a = a / (2*np.sqrt(n))
    
    return sp.sparse.spdiags(a,0,k,k) + sp.sparse.spdiags(b,1,k,k) + sp.sparse.spdiags(b,-1,k,k)





lw = 1
c1 = '#1e3668'
c2 = '#199d8b'
c3 = '#d52f4c'
c4 = '#5ab2d6'
c5 = '#ffb268'