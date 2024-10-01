# -*- coding: utf-8 -*-
#
# Copyright (C) 2019 Julia Favaro
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""Core logic for the pdf definition."""

from matplotlib import pyplot as plt
import numpy as np
from scipy.interpolate import InterpolatedUnivariateSpline #class import


class ProbabilityDensityDistribution(InterpolatedUnivariateSpline): #INHERITANCE, this **is** a Spline, not Composition

    """Class describing a probability density function.

    Parameters
    ----------
    x : array-like
        The array of x values to be passed to the pdf, assumed to be sorted.

    y : array-like
        The array of y values to be passed to the pdf.
    """

    def __init__(self, x, y):
        """Constructor."""
        spline= InterpolatedUnivariateSpline(x,y) #this exists only in the constructor because there is no self at the beginning
        norm=spline.integral(x.min(), x.max())
        self._x=x #private variable because I don't want it to change from outside my class
        self._y=y/norm
        #The reason we use super is so that child classes that may be using  multiple inheritance
        #it will call the correct next parent class function in the Method Resolution Order (MRO).
        super().__init__(self._x,self._y) 

    def plot(self):
        '''This function will plot on the screen both the points given 
        and the interpolation'''
        print(f'Calling {self.__class__.__name__}.plot()...')
        plt.plot(self._x, self._y, 'o')
        x=np.linspace(self._x.min(), self._x.max(),250)
        plt.plot(x, self(x))

    def normalization(self):
        '''Úseful function for normalization for distributions
        like the exponential one'''
        return self.integral(self._x.min(), self._x.max())

#this is the first phase of coding: test driven development
if __name__=='__main__':
    x=np.linspace(0., 1., 10)
    y=np.exp(x)
    pdf=ProbabilityDensityDistribution(x,y)

    #note that changing to composition to hereditary did not change anything of the interface
    x0=0.5
    print(f'Real value {np.exp(x0)}, Interpolated {pdf(x0)}') #you can do this thanks to the special method __call__ implemented in the Spline class
    pdf.plot()
    plt.show()