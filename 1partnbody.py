
import numpy

class NBody:
    def __init__(self, m=1.0, numpar=100,soft=0.01, G=1.0,dt=0.1):
        
        self.data = {}
        self.data['n'] = numpar
        self.data['soft'] = soft
        self.data['G'] = G
        self.data['dt']=dt
        
        self.xp = numpy.random.randn(self.data['n']) 
        self.yp = numpy.random.randn(self.data['n'])
        self.m = numpy.ones(self.data['n'])*m
        self.vx = 0*self.xp
        self.vy = self.vx.copy()
                    
    def pot(self):
        self.fx = numpy.zeros(self.data['n'])
        self.fy = 0*self.fx
        pot =0.0
        for i in range(0,self.data['n']):
            dxp = self.xp[i]-self.xp
            dyp = self.yp[i]-self.yp
            rsqr = dxp**2 + dyp**2
            soft = self.data['soft']**2
            rsqr[rsqr<soft]=soft
            rsqr=rsqr+self.data['soft']**2
            r = numpy.sqrt(rsqr)
            r3 = 1.0/(r*rsqr)
            self.fx[i]=-numpy.sum(self.m*dxp*r3)*self.data['G']
            self.fy[i]=-numpy.sum(self.m*dyp*r3)*self.data['G']
            pot += self.data['G']*numpy.sum(self.m/r) 
        return pot
    def kin(self):
        
    
    def update(self):
        self.xp = self.vx*self.data['dt']
        self.yp = self.vy*self.data['dt']
        pot = self.pot()
        self.vx += self.fx*self.data['dt']
        self.vy += self.fy*self.data['dt']
        kin = 0.5*numpy.sum(self.m*(self.vx**2+self.vy**2))
        return pot + kin        
        

if __name__=='__main__':
    #sys = NBody(1.0,100,0.01,1.0,0.1)
    #print 'the system has', repr(sys.data)
    #print 'the number of particles is', repr(sys.data)
    n=15
    sys=NBody(m=1.0/n,numpar=n)
    #print 'the x positions are ', repr(sys.xp)
    #print 'the y positions are ', repr(sys.yp)
    for i in range(0,100):
        energy = sys.update()
        print energy, sys.pot()
        
        
   # print 'energy of the system is  ', repr(sys.update())
    
                        
                             
                             

                                                                  
        
