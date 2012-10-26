APC 524 Homework 3 

This homework submission contains the following Python script files:

  - testFunctions.py
  - testNewton.py 

which depend on the following class and function definition files:

  - functions.py
  - newton.py


USAGE: 

    Each test function can be run from the command line in a unix shell:

      $ python testFunctions.py

TEST DESCRIPTIONS:

    -testFunctions.py

        -testApproxJacobian1

            - can the Jacobian approximate a constant derivative

        -testApproxJacobian2

            - Can the Jacobian function approximate a linear array

        -testPolynomial

            - Is the given polynomial represented by the function correctly.

        -testMultivariateLinear

            - Can the Jacobian approximate a nonlinear multivariate function: 
                f1 = x1 ^2 + 2 * x2 
                f2 = 2 * x1 * x2

    -testNewton.py

        -testLinear

            - This function tests the Newtons Method solver to see if it correctly solves a simple linear equation. 

        -testSingleStep

            - Tests to see if a single step evaluates correctly for an exponential function  

        -testLinearPolynomial

            - Tests to see if a linear polynomial solves correctly. 
                
