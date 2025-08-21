# THIS IS NOT MY WORK, trying to get te hang of process with professor's code this time -TV
#creating a function to get the first derivative
def deriv(f, x, eps = 1e-5):
    return (f(x+eps) - f(x)) / eps

# creating a function to get the second derivative 
def deriv2(f, x, eps = 1e-5): 
    return (deriv(f, x+eps, eps) - deriv(f, x, eps)) / eps

def optimize(x0, f, tol = 1e-4): 
    if isinstance(x0,complex):
        raise TypeError(f"Input is complex, please use integer or float type")
# final function
    """Run Newton's method to minimize a function. 
    Parameters 
    ----------
    x0: starting value 
    f: function to minimize 
    tol: 
    """
    x_new = x0 - deriv(f, x0) / deriv2(f, x0) 
    x = x0 
    while abs(x_new - x) > tol: 
        x = x_new 
        x_new = x - deriv(f, x) / deriv2(f, x)
    return {"x": x_new, 
            'value': f(x_new)}
import newton
import numpy as np
newton.optimize(start, fun)   ## Assuming your function is called `optimize`.
newton.optimize(2.5, np.cos)  ## Minimizing cos(x) from close-ish to one minimum.