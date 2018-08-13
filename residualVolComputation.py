from __future__ import division, print_function

import numpy as np
import pylab as pl
from scipy.special import gamma
from scipy.optimize import fsolve


def residualVol(N, residual=True):
    '''
    This function computes the residual volume left in the unit side n-box after putting
    n-balls in each of the corners of the n-box and a n-ball that just touches the
    surfaces of the n-balls at the corners.

    N = Number of dimensions

    boxVol = volume of box
    ballVol = Total volume of portions of the n-balls enclosed in the box (effective volume)
    centralBallVol = Volume of the largest n-ball that can fit at the center of box
	resVol = Volume left

    Returns :: The residual volume or the difference between volume of the box and the
               central ball
    '''
    boxVol = 2**N
    # Vol of n-Ball from  https://en.wikipedia.org/wiki/Volume_of_an_n-ball #
    ballVol = (np.pi**(N/2))/(gamma(N/2 + 1)) # Volume of the 'effective' unit n-ball
    radius = np.sqrt(N) - 1 # Radius of the central n-ball
    centralBallVol = (np.pi**(N/2))/(gamma(N/2 + 1))*(radius**N)
    resVol = boxVol - ballVol - centralBallVol
    resVol_central = boxVol - centralBallVol
    if residual:
        return resVol
    return resVol_central


if __name__ == "__main__":
    dims = np.arange(2, 9)
    resVols = residualVol(dims)
    resVols_central = residualVol(dims, residual=False)
    frac_resVols = resVols/(2**dims)
    frac_resVols_central = resVols_central/(2**dims)
    pl.figure(figsize=(7.5,7.5))

    pl.subplot(2,1,1)
    p1, = pl.plot(dims, resVols, 'r-o')
    p2, = pl.plot(dims, resVols_central, 'b--o')
    pl.legend([p1, p2], ['Residual volume', 'Volume of box - central ball'])

    pl.xlabel('Number of dimensions')
    pl.ylabel('Volume left after putting all the balls')
    pl.grid(1)
    pl.subplot(2,1,2)
    p1, = pl.plot(dims, frac_resVols, 'r-o')
    p2, = pl.plot(dims, frac_resVols_central, 'b--o')
    pl.legend([p1, p2], ['Fractional residual volume',
                         '(Volume of box - central ball)/Volume of box'])

    pl.xlabel('Number of dimensions')
    pl.ylabel('Fractional volume left after putting all the balls')
    pl.grid(1)


    zero_of_residualVol = fsolve(residualVol, 6, xtol=1e-12)
    zero_of_residualVol_cental = fsolve(residualVol, 6, args=(False), xtol=1e-12)
 

    print('The residual volume vanishes at D = {}'.format(zero_of_residualVol[0]))
    print('The volume of the central ball exceeds volume of box at D = {}'.format(zero_of_residualVol_cental[0]))

    pl.show()



