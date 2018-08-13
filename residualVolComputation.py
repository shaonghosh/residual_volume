from __future__ import division, print_function

import numpy as np
import pylab as pl
from scipy.special import gamma
from scipy.optimize import fsolve


def residualVol(N):
    '''
    This function computes the residual volume left in the unit side n-box after putting
    n-balls in each of the corners of the n-box and a n-ball that just touches the
    surfaces of the n-balls at the corners.

    N = Number of dimensions

    boxVol = volume of box
    ballVol = Total volume of portions of the n-balls enclosed in the box (effective volume)
    centralBallVol = Volume of the largest n-ball that can fit at the center of box
	resVol = Volume left
    '''
    boxVol = 2**N
    # Vol of n-Ball from  https://en.wikipedia.org/wiki/Volume_of_an_n-ball #
    ballVol = (np.pi**(N/2))/(gamma(N/2 + 1)) # Volume of the 'effective' unit n-ball
    radius = np.sqrt(N) - 1 # Radius of the central n-ball
    centralBallVol = (np.pi**(N/2))/(gamma(N/2 + 1))*(radius**N)
    resVol = boxVol - ballVol - centralBallVol
    return resVol


if __name__ == "__main__":
    dims = np.arange(2, 9)
    resVols = residualVol(dims)
    pl.plot(dims, resVols, 'r-o')
    pl.xlabel('Number of dimensions')
    pl.ylabel('Volume left after putting all the balls')
    pl.grid(1)
    zero_of_residualVol = fsolve(residualVol, 6, xtol=1e-12)
    print('The residual volume vanishes at D = {}'.format(zero_of_residualVol[0]))
    pl.show()

