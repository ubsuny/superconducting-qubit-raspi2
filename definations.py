import scipy as sp
import numpy as np
import matplotlib.pyplot as plt

def a(n):
    '''
        returns the annihilation operator for maximum n photons
    '''
    a = np.zeros((n+1,n+1))
    b = np.arange(1,n+1)
    np.fill_diagonal(a[:,1:],np.sqrt(b))
    return a

def adagger(n):
    '''
        returns the creation operator for maximum n photons
    '''
    return a(n).conj().T



def plotFlipFlopPopulation(t, rho_ff):
    
    for state in np.arange(rho_ff.shape[1]):
            k = plot(t, rho_ff[:, state, state], label= state)
    return k