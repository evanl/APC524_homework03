import numpy as N

def ApproximateJacobian(f, x, dx=1e-6):
    """Return an approximation of the Jacobian Df(x) as a numpy matrix"""
    try:
        n = len(x)
    except TypeError:
        n = 1
    fx = f(x)
    Df_x = N.matrix(N.zeros((n,n)))

    for i in range(n):
        v = N.matrix(N.zeros((n,1)))
        v[i,0] = dx
        Df_x[:,i] = (f(x + v) - fx) / dx
    return Df_x

class Polynomial(object):
    """Callable polynomial object.

    Example usage: to construct the polynomial p(x) = x^2 + 2x + 3,
    and evaluate p(5):

    p = Polynomial([1, 2, 3])
    p(5)"""

    def __init__(self, coeffs):
        self._coeffs = coeffs

    def __repr__(self):
        return "Polynomial(%s)" % (", ".join([str(x) for x in self._coeffs]))

    def f(self,x):
        ans = self._coeffs[0]
        for c in self._coeffs[1:]:
            ans = x*ans + c
        return ans

    def __call__(self, x):
        return self.f(x)

class LinearMap(object):
    """ LinearMap takes in a numpy matrix and stores it to be evaluated.

        Example, store a symmetric tensor [10 20 ; 20 30] and use it to map x and y
 
        Example Usage:  A = LinearMap( N.matrix("10 20 ; 20 30"))
                        y = A(x) # note that x is a 2x1 matrix of values   """
    def __init__(self, matrix):
        self._matrix = matrix

    def f(self,x):
      return self._matrix * x
      
    def __call__(self,x):
        return self.f(x)  
