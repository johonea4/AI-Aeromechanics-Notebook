import numpy as np

class EM_Gaussian:
    def __init__(self,data,numComponents):
        self.data = data
        self.numComponents = numComponents
        self.means = [0] * numComponents
        self.variances = [0] * numComponents
        self.weights = [0] * numComponents
        
    def Initialize(self):
        self.variances = [1] * self.numComponents
        idx = np.random.randint(0,len(self.data),self.numComponents)
        self.means = self.data[idx]
        self.weights = [1.0/float(self.numComponents)] * self.numComponents
        
    def GetProbability(self):
        px = []
        for i in range(self.numComponents):
            a1 = -0.5*np.log(2.0*np.pi*self.variances[i])
            a2 = np.subtract(self.data,self.means[i])
            a2 = np.square(a2)
            a2 = np.divide(a2,2.0*self.variances[i])
            a3 = np.subtract(a1,a2)
            a3 = np.exp(a3)
            px.append(a3)
        return px
        
    def ComputeResponsibilities(self):
        px = self.GetProbability()
        lhood = []
        for i in range(self.numComponents):
            a1 = np.multiply(px[i],self.weights[i])
            a2 = []
            for j in range(self.numComponents):
                b1 = np.multiply(px[j],self.weights[j])
                if j==0:
                    a2 = b1
                else:
                    a2 = np.add(a2,b1)
            a1 = np.divide(a1,a2)
            lhood.append(a1)
        return lhood
    
    def ComputeLiklihood(self):
        #ln(Pr(X | mixing, mean, stdev)) = 
        #sum((n=1 to N), ln(sum((k=1 to K), mixing_k * N(x_n | mean_k,stdev_k))))
        px = self.GetProbability()
        px = np.transpose(px)
        px = np.multiply(px,self.weights)
        px = np.sum(px,1)
        px = np.log(px)
        return np.sum(px)
    
    def TestConvergence(self,prevL, newL, conv_ctr, cap=10):
        inc = (abs(prevL) * 0.9 < abs(newL) < abs(prevL) * 1.1)
        if inc:
            conv_ctr += 1
        else:
            conv_ctr = 0
        return conv_ctr, conv_ctr > cap
    
    def Run(self):
        convergence = False
        prevL = self.ComputeLiklihood()
        newL = prevL
        cDiff = 0
        while convergence == False:
            px = self.ComputeResponsibilities()
            self.weights = np.mean(px,1)
            self.means = np.divide(np.sum(np.multiply(self.data,px),1),np.sum(px,1))
            vals = []
            for i in range(self.numComponents):
                vals.append(np.subtract(self.data,self.means[i]))
            self.variances = np.divide(np.sum(np.multiply(np.square(vals),px),1),np.sum(px,1))
            newL = self.ComputeLiklihood()
            cDiff,convergence = self.TestConvergence(prevL,newL,cDiff)
            prevL = newL
            
    def Segment(self):
        px = self.GetProbability()
        indexes = np.argmax(px,0)
        arr = self.data
        for i in range(self.numComponents):
            idx = np.where(indexes==i)
            arr[ idx ] = self.means[i]
        return arr