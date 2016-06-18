import numpy
from matplotlib  import pyplot as plt

class NBody:
    def __init__(self, m, numpar, soft=0.01, G=1.0, dt=0.1):
        self.data={}
        self.data['soft']=soft
        self.data['n']=numpar
        self.data['G']=1.0
        self.data['dt']=dt

        self.x=numpy.random.randn(self.data['n'])
        self.y=numpy.random.randn(self.data['n'])
        self.m=numpy.ones(self.data['n'])*m
        self.vx=0*self.x
        self.vy=self.vx.copy()
    def pot(self):
        self.fx=numpy.zeros(self.data['n'])
        self.fy=0*self.fx
        potE=0
        for i in range(0,self.data['n']):
            dx=self.x[i]-self.x
            dy=self.y[i]-self.y
            rsqr=dx**2+dy**2
            soft=self.data['soft']**2
            rsqr[rsqr<soft]=soft
            rsqr=rsqr+self.data['soft']**2
            r=numpy.sqrt(rsqr)
            r3=1.0/(r*rsqr)
            self.fx[i]=-numpy.sum(self.m*dx*r3)*self.data['G']
            self.fy[i]=-numpy.sum(self.m*dy*r3)*self.data['G']
            potE += self.data['G']*numpy.sum(self.m/r)
        return potE
    def kin(self):
        self.fx=numpy.zeros(self.data['n'])
        self.fy=0*self.fx
        t_delta = 0.1
        self.vx += self.fx*t_delta
        self.vy += self.fy*t_delta
        kinE = 0.5*numpy.sum(self.m*(self.vx**2+self.vy**2))
        return kinE
    def update(self):
        self.x+=self.vx*self.data['dt']
        self.y+=self.vy*self.data['dt']
        pot=self.pot()
        self.vx+=self.fx*self.data['dt']
        self.vy+=self.fy*self.data['dt']
        kinetic=0.5*numpy.sum(self.m*(self.vx**2+self.vy**2))
        return pot+kinetic
   
if __name__=='__main__':
    n=150
    sys=NBody(m=1.0/n,numpar=n)
    print 'number of masses is ',sys.data['n']
    plt.plot(sys.kin(),'-*')
    plt.plot(sys.pot(),'+-')
    plt.plot(sys.update(),'r')
    
    
    for i in range(0,1000):
        energy=sys.update()
        kine = sys.kin
        pote = sys.pot()
        plt.plot(kine,'*')
        

#print len(kine)#, len(pote), len(energy) 
        
