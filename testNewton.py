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
        p = F.Polynomial([2,1,6,-15])
        solver = newton.Newton(p, tol = 1.e-15, maxiter = 20, dx = 1.e-10)
        x = solver.solve(0.0)
        self.assertAlmostEqual(x,1.357953822)

if __name__ == "__main__":
    unittest.main()
