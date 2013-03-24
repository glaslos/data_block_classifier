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

import math

class KGoodNeighbors(object):
    """
    Modification of K nearest neighbors.
    
    Calculates candidate distance to items with same features.
    
    Candidate features are not weighted.
    Weighting could be done based on estimated region.
    
    Decision is made on low coefficient variation.
    
    Training items could be combined to a single feature vector
    or feature matrix.   
    
    Papers:
    Statistical Learning for File-Type Identification, Siddharth Gopal
    """
    def __init__(self):
        pass
    
    def euclidean_distance(self, x, y):
        # Distance between two items
        return sum([(x[i]-y[i])**2 for i in range(len(x))])

    def root_mean_square_deviation(self, x, y):
        # General mean deviation
        return math.sqrt(self.euclidean_distance(x, y)/len(x))

    def arithmetic_mean(self, x):
        return sum(x) / len(x)

    def coefficient_variation(self, x, y):
        # Variation of the candidates coefficients
        return self.root_mean_square_deviation(x, y) / self.arithmetic_mean(x)

    def find_neighbors(self, x, k = 3):
        pass