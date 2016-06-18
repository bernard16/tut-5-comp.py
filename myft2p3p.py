from numpy import concatenate,exp,pi,arange,complex
import numpy

def myfft3(vec):
    n=vec.shape[0]
    if n==1:
        return vec
    mya=vec[0::3]
    myb=vec[1::3]
    myc=vec[2::3]
    j=complex(0,1)
    nn=n/3
    twid1=exp(-2*pi*j*arange(0,nn)/n)
    twid2=exp(-4*pi*j*arange(0,nn)/n)

    f1=exp(-2*pi*j/3) 
    f2=exp(-4*pi*j/3)
    f1b=f2;        
    f2b=f1; 

    aft=myfft3(mya)
    bft=myfft3(myb)*twid1
    cft=myfft3(myc)*twid2
    
    ft1=aft+bft+cft
    ft2=aft+bft*f1+cft*f2
    ft3=aft+bft*f1b+cft*f2b
    
    ft=concatenate((ft1,ft2,ft3))

    return ft

vec = numpy.random.randn(243)
print len(vec)
print 'compare:', numpy.allclose(myfft3(vec),numpy.fft.fft(vec))
