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


class EntropyRateMarkovChain(object):
    """
    
    Papers:
    Embedded Malware Detection using Markov n-grams, M. Zubair Shafiq
    On the estimation of the entropy rate of finite Markov chains, Gabriela Ciuperc
    """
    def __init__(self, data_block):
        self.data = data_block
        self.transition_matrix = [[0] * 256] * 256
        self.count_tuples()
        self.calc_distribution()
        self.calc_entropy_rate()
    
    def count_tuples(self):
        last = ord(self.data[0:1])
        self.transition_matrix[last][last] += 1.0 / 512.0
        for byte in self.data[1:]:
            current = ord(byte)
            self.transition_matrix[last][current] += 1.0 / 512.0
            last = current
    
    def calc_distribution(self):
        self.stationary_distribution = [sum(self.transition_matrix[i][j] for j in range(256)) for i in range(256)]
            
    def calc_entropy_rate(self):
        self.entropy_rate = sum([- self.stationary_distribution[i] * sum([float(state) * math.log(float(state), 2) 
                                    for state in self.transition_matrix[i] if state > 0]) for i in range(256)])/1024