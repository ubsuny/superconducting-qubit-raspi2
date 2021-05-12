import numpy as np
import matplotlib.pyplot as plt
from numpy import random
import scipy.linalg as lg
from scipy.optimize import curve_fit




def QMCWF(U, L, psi_0i, step):
    
    '''
        We use this method to find the single trajectory of the system in contact with the environment. Trajectory evolves with two 
        possibilities, first is quantum jump and second is hamiltonian evolution.
        
        U = evolution matrix
        L = jump matrix 
        psi_0i = intial wavefunction
        step = number of time steps to evolve the system for
         
    '''
    # initialising
    psi_f = psi_0i   
    psi_n = psi_0i
    
    # initialising the probability of the ground and exited state
    prob_g = np.zeros(step+1)
    prob_e = np.zeros(step+1)
    
    # squaring it
    prob_g[0] = abs(psi_0i[0, 0])**2
    prob_e[0] = abs(psi_0i[1, 0])**2
    
    # evolving the system trajectory
    for t in range(step):
        size = np.dot(np.dot(psi_0i.conj().T, U.conj().T), np.dot(U, psi_0i)) # the probability of the no-jump
        jump_prob = 1.0 - float(size[0, 0])                                 # jump probability
        # print(size)
        epsilon = random.rand()                                            # generating random number                             
        if epsilon > jump_prob:
            psi_f = np.dot(U, psi_0i)                                       #evolving according to U operator for single time step
            psi_n = psi_f / lg.norm(psi_f)                                   # normalising wavefunction
            # print(psi_n)
            prob_g[t+1] = abs(psi_n[0, 0])**2
            prob_e[t+1] = abs(psi_n[1, 0])**2
            psi_0i = psi_n
        else :
            psi_f = np.dot(L, psi_0i)                                       # evolving according to jump operator
            psi_n = psi_f / lg.norm(psi_f)                                   # normalising
            prob_g[t+1] = abs(psi_n[0, 0])**2
            prob_e[t+1] = abs(psi_n[1, 0])**2
            prob_g[t+2 : step+2] = 1
            break
    return prob_g, prob_e

def QMCWF1(U, c_3, psi_0i, step):
    
    '''
        We use this method to find the single trajectory of the system in contact with the environment. Trajectory evolves with two 
        possibilities, first is quantum jumps from the list of given two and second is hamiltonian evolution. 
        
        U = evolution matrix
        L = jump matrices 
        psi_0i = intial wavefunction
        step = number of time steps to evolve the system for 
    '''
    # initialising
    psi_f = psi_0i
    psi_n = psi_0i
    
    # initialising the probability of the ground and exited state
    prob_g = np.zeros(step+1)
    prob_e = np.zeros(step+1)
    prob_g[0] = abs(psi_0i[0, 0])**2
    prob_e[0] = abs(psi_0i[1, 0])**2
    
    # evolving the system trajectory
    for t in range(step):
        size = np.dot(np.dot(psi_0i.conj().T, U.conj().T), np.dot(U, psi_0i))        # the probability of the no-jump
        jump_prob = 1.0 - float(size[0, 0])                                        # jump probability
        # print(jump_prob)
        
        epsilon = random.rand()
        if epsilon > jump_prob:
            psi_f = np.dot(U, psi_0i)
            psi_n = psi_f / (lg.norm(psi_f))
            # print(abs(psi_n[1, 0])**2)
            prob_g[t+1] = abs(psi_n[0, 0])**2
            prob_e[t+1] = abs(psi_n[1, 0])**2
            psi_0i = psi_n
        else :
            cum_pro = 0
            dpm = 0
            count = 0
            for K in range(2):                                              # loop over jump operators
                psi_f = np.dot(L[K, :, :], psi_0i)
                dpm = dt * np.abs(np.dot(psi_f.conj().T, psi_f ))
                print(dt * np.abs(np.dot(psi_f.conj().T, psi_f)))
                cum_pro += dpm
                count += 1
                if epsilon < cum_pro:                                       # condition for which jump operator to choose
                    psi_f /= np.sqrt(dpm / dt)
                    psi_n = psi_f
                    prob_g[t+1] = abs(psi_n[0, 0])**2
                    prob_e[t+1] = abs(psi_n[1, 0])**2
                    psi_0i = psi_n
                    break
            if count == 1:
               prob_g[t+2 : step+2] = 1 
  
    return prob_g, prob_e

def test(x, a, b):
    '''
        give the array of  form  a*exp(b*x) for the given array x.
    '''
    return a * np.exp(b * x)
