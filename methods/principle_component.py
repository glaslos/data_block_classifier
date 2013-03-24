# Copyright (C) 2012  Lukas Rist
# 
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

from itertools import imap
from operator import mul

import numpy
import methods as bfd


class PrincipleComponent(object):
    """
    
    Papers:
    A New Approach to Content-based File Type Detection, Mehdi Chehel Amirani
    """
    def __init__(self):
        self.total_freq = []
        
    def calc_total_freq(self, chars):
        fd = bfd.FrequencyDistribution()
        self.byte_freq = fd.byte_frequency(self, chars)
        self.total_freq += self.byte_freq
    
    def calc_mean_vector(self):
        # aka centroid
        self.mean_vector = [float(sum(row)) / float(len(row)) for row in self.total_vars]
    
    def dot_product(self, x, y):
        return sum(imap(mul, x, y))
    
    def calc_principle_component(self):
        # Transpose the matrix
        self.num_distrib = len(self.total_freq)
        self.total_vars = zip(*self.total_freq)
        self.num_vars = len(self.total_vars)
        self.calc_mean_vector()
        self.covariance_matrix = [[self.dot_product(map(lambda x: x - self.mean_vector[i], self.total_vars[i]), 
                                                    map(lambda x: x - self.mean_vector[j], self.total_vars[j])) /
                                   float(self.num_distrib - 1)
                                   for j in range(self.num_vars)]
                                  for i in range(self.num_vars)
                                  ]
    
    def calc_eigen(self):
        matrix = numpy.mat(self.covariance_matrix)
        self.eigenvalues, self.eigenvectors = numpy.linalg.eig(matrix)
        
    def select_k_max_eigenvectors(self, k = 2):
        # k = 15 for later
        self.max_eigenvectors = []
        for i in xrange(k):
            j = self.eigenvalues.argmax()
            self.max_eigenvectors.append(self.eigenvectors[j])
            self.eigenvalues[j] = float("-inf")
        
    def calc_dimensionality_reduction_error(self):
        print numpy.sum(numpy.ma.masked_equal(self.eigenvalues, float("-inf"))) / 2
        
    def calc_deviation_vector(self):
        self.empirical_standard_deviation_vector = [numpy.sqrt(self.covariance_matrix[i][i]) for i in range(self.num_vars)]
        
    def calc_zscore(self):
        h = numpy.identity(self.num_vars)
        self.z_score_matrix = numpy.divide(self.covariance_matrix, numpy.dot(self.empirical_standard_deviation_vector, h))
        
    def data_projection(self):
        print numpy.dot(numpy.array(self.max_eigenvectors), self.z_score_matrix)
    
if __name__ == "__main__":
    pca = PrincipleComponent()
    pca.total_freq = [
                     [4, 2, 0.6],
                     [4.2, 2.1, 0.59],
                     [3.9, 2, 0.58],
                     [4.3, 2.1, 0.62],
                     [4.1, 2.2, 0.63]
                    ]
    pca.calc_principle_component()
    pca.calc_eigen()
    pca.calc_dimensionality_reduction_error()
    pca.select_k_max_eigenvectors()
    pca.calc_dimensionality_reduction_error()
    pca.calc_deviation_vector()
    pca.calc_zscore()
    pca.data_projection()