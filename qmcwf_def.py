def QMCWF(U,L,psi_0,step):
    
    psi_f = psi_0
    psi_n = psi_0
    prob_g = np.zeros(step+1)
    prob_e = np.zeros(step+1)
    prob_g[0] = abs(psi_0[0,0])**2
    prob_e[0] = abs(psi_0[1,0])**2
    
    for t in range(step):
        size = np.dot(np.dot(psi_0.conj().T,U_dagger),np.dot(U,psi_0))
        no_jump_prob = float(size[0,0])
        epsilon = random.rand()
        if epsilon < no_jump_prob :
            psi_f = np.dot(U,psi_0)
            psi_n = psi_f/np.sqrt(1-dp)
            prob_g[t+1] = abs(psi_n[0,0])**2
            
            prob_e[t+1] = abs(psi_n[1,0])**2
            psi_0 = psi_n
        else :
            psi_n = np.dot(L,psi_0)/np.sqrt(dp/dt)
            prob_g[t+1] = abs(psi_n[0,0])**2
            prob_e[t+1] = abs(psi_n[1,0])**2
            prob_g[t+2:step+2] = 1
            break
    print(prob_g.shape)
    return psi_n,prob_g,prob_e

def QMCWF2(U,L,psi_0i,step):
    
    psi_f = psi_0i
    psi_n = psi_0i
    prob_g = np.zeros(step+1)
    prob_e = np.zeros(step+1)
    prob_g[0] = abs(psi_0i[0,0])**2
    prob_e[0] = abs(psi_0i[1,0])**2
    for t in range(step):
        size = np.dot(np.dot(psi_0i.conj().T,U_dagger),np.dot(U,psi_0i))
        jump_prob = 1.0 - float(size[0,0])
        #print(size)
        epsilon = random.rand()
        if epsilon > jump_prob:
            psi_f = np.dot(U,psi_0i)
            psi_n = psi_f/lg.norm(psi_f)
            #print(psi_n)
            prob_g[t+1] = abs(psi_n[0,0])**2
            prob_e[t+1] = abs(psi_n[1,0])**2
            psi_0i = psi_n
        else :
            psi_f = np.dot(L,psi_0i)
            psi_n = psi_f/lg.norm(psi_f)
            prob_g[t+1] = abs(psi_n[0,0])**2
            prob_e[t+1] = abs(psi_n[1,0])**2
            prob_g[t+2:step+2] = 1
            break
    return prob_g,prob_e
print(np.zeros((200,step+1)).shape)  
ground_prob,exited_prob = QMCWF2(U,L,psi_0,step)
plt.plot(tlist,ground_prob,label = "ground state")
plt.plot(tlist,exited_prob, label = "exited state")
plt.legend()