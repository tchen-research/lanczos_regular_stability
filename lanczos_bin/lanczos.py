import numpy as np
import scipy as sp


def lanczos_reorth(A,v,k,reorth=0):
    """
    run Lanczos with reorthogonalization
    
    Input
    -----
    A : entries of diagonal matrix A
    v : starting vector
    k : number of iterations (matvecs)
    reorth : number of iterations to reorthogonalize
    
    Output
    ------
    Q : Lanczos vectors
    α : diagonal coefficients
    β : off diagonal coefficients 
    """
    
    n = A.shape[0]
    
    Q = np.zeros((n,k+1),dtype=A.dtype)
    α = np.zeros(k,dtype=A.dtype)
    β = np.zeros(k,dtype=A.dtype)
    
    Q[:,0] = v / np.linalg.norm(v)
    
    for n in range(k):

        qnp1 = A@Q[:,n] - β[n-1]*Q[:,n-1] if n>0 else A@Q[:,n]
        α[n] = Q[:,n].conj().T@qnp1
        qnp1 -= α[n]*Q[:,n]
        
        if reorth>n:
            qnp1 -= Q[:,:n-1]@(Q[:,:n-1].conj().T@qnp1)
            
        β[n] = np.linalg.norm(qnp1)
        Q[:,n+1] = qnp1 / β[n]
                
    return Q,(α,β)