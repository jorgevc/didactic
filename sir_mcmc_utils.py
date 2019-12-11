import numpy as np

def PoissonLikelihood(dat, model_prediction):
	loglike=0.0
	for x, L in zip(dat, model_prediction):
		if(L>0.0):
			loglike = loglike - L + x*np.log(L)
	return loglike
		
def SIR(y,t,gamma,beta):
	S=y[0]
	I=y[1]
	R=y[2]
	N=S+I+R
	
	dS = -beta * S*I/N
	dI = beta * S*I/N - gamma*I
	dR = gamma*I
	return np.array([dS,dI,dR])





























#gamma0 = 1./3.        # recovery period of influenza in days^{-1}
#R0    = 1.5        # reproduction number of a hypothetical strain of pandemic influenza
#beta0 = R0*gamma0   # the baseline transmission rate
#N0=10000000.0
#y0 = np.array([N0-1.,1.,0.])

#def mod(y,t):
	#return SIR(y,t,gamma0,beta0)
	
#time = np.linspace(0.0,200,20)
#y = odeint(mod,y0,time)
#Infected= y[:,1]
#s = np.random.poisson(Infected)
#plt.plot(time,Infected)
#plt.scatter(time,s)
#plt.show()
#np.savetxt('data.dat', np.array([time,s]).T , fmt=['%1.0f','%1i'] ,delimiter=',')
