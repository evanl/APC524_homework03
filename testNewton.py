#!/usr/bin/env python

import newton
import unittest
import numpy as N

class TestNewton(unittest.TestCase):
    def testLinear(self):
        f = lambda x : 3.0 * x + 6.0
        solver = newton.Newton(f, tol=1.e-15, maxiter=2)
        x = solver.solve(2.0)
        self.assertEqual(x, -2.0)

    def testSingleLinearStep(self):
        def f(x):
          return 4.0 * x + N.exp(x)
        solver = newton.Newton(f, tol = 1.e-15, maxiter=1, dx = 1.e-10) 
        x = solver.solve(0.0)
        self.assertAlmostEqual(x, -1./5.)

if __name__ == "__main__":
    unittest.main()
