# newton - Newton-Raphson solver
#
# For APC 524 Homework 3
# CWR, 18 Oct 2010

import numpy as N
import functions as F

class Newton(object):
    def __init__(self, f, tol=1.e-6, maxiter=20, dx=1.e-6, DFA=None , r =1.e10 ):
        """Return a new object to find roots of f(x) = 0 using Newton's method.
        tol:     tolerance for iteration (iterate until |f(x)| < tol)
        maxiter: maximum number of iterations to perform
        dx:      step size for computing approximate Jacobian
        DFA:     analytic jacobian if applicable
        r:       maximum distance away from initial guess"""
        self._f = f
        self._tol = tol
        self._maxiter = maxiter
        self._dx = dx
        self._DFA = DFA
        self._r = r

    def solve(self, x0):
        """Return a root of f(x) = 0, using Newton's method, starting from
        initial guess x0"""
        x = x0
        for i in xrange(self._maxiter):
            fx = self._f(x)
            if N.linalg.norm(fx) < self._tol:
                return x
            x = self.step(x, fx)
            if N.linalg.norm(x-x0) > self._r:
                raise Exception('x has exceeded the radius of the initial guess')
        if N.linalg.norm(fx) > self._tol:
            raise Exception('Solution does not converge for this number of iterations')

        return x

    def step(self, x, fx=None):
        """Take a single step of a Newton method, starting from x
        If the argument fx is provided, assumes fx = f(x)"""
        if fx is None:
            fx = self._f(x)
        if self._DFA==None:
            Df_x = F.ApproximateJacobian(self._f, x, self._dx)
            h = N.linalg.solve(N.matrix(Df_x), N.matrix(fx))
        else:
            h = N.linalg.solve(N.matrix(self._DFA(x)), N.matrix(fx))
            
        return x - h
