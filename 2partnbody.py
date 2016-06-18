# Tutorial 5
# Question2: Write a Method that will calculates the force on the particles using
# softened potential
# 
import numpy

class NBody:
    def __init__(self, m, numpar,soft, G):
        
        self.data = {}
        self.data['n'] = numpar
        self.data['soft'] = soft
        self.data['G'] = G
        
        self.xp = numpy.random.randn(self.data['n']) 
        self.yp = numpy.random.randn(self.data['n'])
        self.m=numpy.ones(self.data['n'])*m
                    
    def force(self):
        self.pot = numpy.zeros(self.data['n'])
        force = 0.0
        for i in range(self.data['n']):
            dxp = self.xp[i]-self.xp
            dyp = self.yp[i]-self.yp
            rsqr = dxp**2 + dyp**2
            soft = self.data['soft']**2
            rsqr[rsqr<soft]=soft
            rsqr=rsqr+self.data['soft']**2
            r = numpy.sqrt(rsqr)
            self.pot=self.data['G']*numpy.sum(self.m/r)
            force +=self.pot/r
        return force

if __name__=='__main__':
    sys = NBody(1.0,100,0.01,1.0)
    print 'number of particles is ', repr(sys.data['n'])
    print 'the system has data ', repr(sys.data)
    print 'force on each mass is ', repr(sys.force())
    
                        
                             
                             

                                                                  
        
