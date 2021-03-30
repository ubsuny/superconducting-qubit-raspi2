### Superconducting qubit and it's dynamics using QMCWF



Every phenomena is fundamentally quantum in nature and as we go to tiny world that becomes more obvious.So why don't we use quantum physics based computation. we have made huge progress in terms of understanding light-atom interactions even at quantum level and has given field of cavity quantum electrodynamics. Here I will talk about one such interaction between Superconducting Qubit for our case it will be Transmon qubit and superconducting waveguide resonator which can store quantised light. I will talk about realization of qubit and  see the dynamics of our coupled transmon and resonator. 

Let's talk about the **Resonator** first. There are many ways to implement the resonator which is just a harmonic oscillator at the end. For our case we can either use the 3D cavity or Superconducting coplanar waveguide (CPW) resonator. we also call it Microwave resonator because of the resonance frequency of it. Around resonance, the properties of a CPW resonator can be approximated by LCR lumped element[1]. The LCR model is useful to get an intuitive understanding of the resonator properties. If we write the hamiltonian of the resonator

\begin{equation}
H_r = \frac{1}{2} CV^2 + \frac{1}{2} LI^2
\end{equation}
where $V=Q/C$ and $I = \dot{Q}$ then the equation will become\cite{CQED},
\begin{equation}
H_r = \frac{L}{2} \dot{Q}^2 + \frac{1}{2}C Q^2 
\end{equation}

we can connect above equation with the hamiltonian of the simple harmonic oscillator by putting $p= L\dot{Q}$ and $Q=x$. So, the new hamiltonian will be same as SHO:
\begin{equation}
H_r = \hbar \omega_r\left(a^+a +\frac{1}{2}\right)
\end{equation}
where $<a^+a> = <n> = n$ is the average photon number. In our code we have decided to assumed $\hbar = 1$ and $\omega_r =  2 . \pi$.

Now, for the **transmon** part, superconductivity allows to introduce nonlinearity in quantum electrical circuits while avoiding losses. Indeed, the Josephson junction is a nonlinear circuit element. We can write the hamiltonian for the transmon qubit(one type of the superconducting qubit) as,

\begin{equation}
H_T = \frac{(Q - Q_g)^2}{2C_{\Sigma}} - E_J cos(2\pi\frac{\Phi}{\Phi_0})  \\
H_T = 4E_C(n - n_g)^2 - E_J cos\phi
\end{equation}

Here,charging energy $E_C = e^2/2C_{\Sigma}$ and $E_J = \Phi_0 I_c/2\pi$. So, basically when the ration of $E_J/E_C$ is very large, typically in the order of 10 we get the transmon qubit. Above transmon qubit is multi-level system but what we want is just the two level system so that we can use it as a qubit. One of the simplest way to do that is truncate the all the levels above first ecited state. We can do that because we have the anharmonisity in level seperation[2]. So let's do that. First we write the $\phi$ and $n$ in terms of $\sigma$ and $\sigma^+$ [3],

\begin{equation}
\phi = (\frac{2E_C}{E_J})^{1/4} (\sigma^+ + \sigma) \\
n = \frac{i}{2} (\frac{2E_J}{E_C})^{1/4} (\sigma^+ - \sigma)
\end{equation}

Using these expressions finally leads to,

\begin{equation}
H_T = \sqrt{8E_C E_J}\sigma^+\sigma - \frac{E_C}{12} (\sigma^+ + \sigma)^4  \\
H_T = \hbar \omega_a \sigma^+\sigma - \frac{E_C}{2} \sigma^+\sigma^+bb
\end{equation}

In the second equation above have used the Rotating wave approximation. Now second term in the above equation tells us about the anharmonicity in transmon energy levels which we will get reed of, Hence our final hamiltonian for the Transmon will look like,

\begin{equation}
H_T = \hbar \omega_a \sigma^+\sigma
\end{equation}

Now, lets couple this two together, the resonator and the transmon, the simplest way to do that is under RWA approcimation, which will give us the Jaynes-Cumming Hamiltonian[3] as shown below,

\begin{equation}
H_{JC} = H_r + H_T + \hbar g (a^+\sigma^- + a\sigma^+) 
\end{equation}

here $g$ is the coupling constant. When the two systems are couples (single transmon qubit with single mode of the oscillator) we can see interisting dynamics in it. First thing to note is before coupling term added, what we will see as the energy levels are degenerate. which means the $|0e>$ (transmon in the exited state and the resonator in the ground state) and $|1,g>$ (transmon in the ground state and resonator in first exited state means with single photon) are degenerate. But, after adding the coupling term they will become non degenerate[3]. Now, suppose we start in the $|0e>$ state of the system, because of the coupling term what the hamiltonial will do is, it will oscillate between the $|0e>$ and $|1g>$ at $2g$ frequency[3]. This is known as Vaccum Rabi oscillations. This happens when the detuning ($\Delta$) between the qubit and resonator frequancy is zero, means both frequancies are same. so we will get complete oscillations where at one point the probability of being in the exited state would be zero. 

But, what happens if detuning ($\Delta$) is not zero, In such cases we will still get the oscillations but they won't be same as above case. chances of zero probability for exited will never be completely zero. another thing that will happen is the oscillation frequency will increase. And if the detuning is too big, there won't be much of a coupling between the qubit and resonator and we won't see any oscillations as if it is decoupled. For the initial part of my project is to show dynamics of the system. 


In this project my goal is to implement transmon qubit and resonator which are coulped with each other and see it's dynamics. eventually i will implement the transmon qubit in contact with the environment(Heat bath) and see how it's dynamics work out. As a initial goal I wanted to see how it's working and how in a simplest way I can implement it without using Quantum Monte Carlo wavefuction method. That's exactly what I have done in the first part of the milestone to implement the Jaynes-Cumming model using density matrix and it's time evolution in the eigun states basis.   

let's see it mathematically to understand my code,






### Referances

[1]. Goppl, M., A. Fragner, M. Baur, R. Bianchetti, S. Filipp, J. M. Fink, P. J. Leek, G. Puebla, L. Stefen, and A. Wallraff, 2008, J. Appl. Phys. 104(6), 113904, URL http://dx.doi.org/10.1063/1.3010859.

[2]. Koch, J., T. M. Yu, J. Gambetta, A. A. Houck, D. I. Schuster, J. Majer, A. Blais, M. H. Devoret, S. M. Girvin, and R. J. Schoelkopf, 2007, Phys. Rev. A 76(4), 042319, URL http://link.aps.org/abstract/PRA/v76/e042319.

[3]. Blais, A., Grimsmo, A., Girvin, S., & Wallraff, A. (2020). Circuit Quantum Electrodynamics.