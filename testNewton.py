#!/usr/bin/env python

import newton
import unittest
import numpy as N
import functions as F

class TestNewton(unittest.TestCase):
    def testLinear(self):
        f = lambda x : 3.0 * x + 6.0
        solver = newton.Newton(f, tol=1.e-15, maxiter=2)
        x = solver.solve(2.0)
        self.assertEqual(x, -2.0)

    def testSingleStep(self):
        def f(x):
          return 4.0 * x + N.exp(x)
        solver = newton.Newton(f, tol = 1.e-15, maxiter=1, dx = 1.e-10) 
        x = solver.solve(0.0)
        self.assertAlmostEqual(x, -1./5.)

    def testLinearPolynomial(self):
        p = F.Polynomial([1,-6,-19,84])
        solver = newton.Newton(p, tol = 1.e-15, maxiter = 20, dx = 1.e-10)
        x = solver.solve(0.0)
        self.assertAlmostEqual(x,3.)
        y = solver.solve(-6.0)
        self.assertAlmostEqual(y,-4)
        z = solver.solve(6.0)
        self.assertAlmostEqual(z,7)

    def testMultivariate(self):
        def f(x):
          a = x[0] * (x[0,0] + 2*x[1,0])
          b = 2.* x[1,0]
          val = N.mat(N.zeros((2,1)))
          val[0,0] = a
          val[1,0] = b
          return val

        solver = newton.Newton(f, tol = 1.e-10, maxiter = 30) 
        x = solver.solve(N.matrix("1; 1"))
        print x 
        N.testing.assert_array_almost_equal(x, N.mat("0 ; 0"))


if __name__ == "__main__":
    unittest.main()
