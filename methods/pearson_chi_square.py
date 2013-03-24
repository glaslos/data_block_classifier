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

import random


class PearsonChiSquare(object):
    """
    
    Papers:
    Automated mapping of large binary objects using primitive fragment type classification, Gregory Conti
    """
    def __init__(self):
        pass
    
    def calc_chi_square(self, observed, expected):
        """
        Calculate the upper probability of the Chi Square distribution using 
        this Chi Square value and 255 degrees of freedom.
        
        The closer to 1 the return value is, the more similar is the observed sample
        to the expected sample.
        """
        chi_squared = sum([(observed[i][1] - expected[i][1]) ** 2 / expected[i][1] for i in range(256)])
        upper_probability = chi_squared / 256
        return upper_probability
    
    def train_chi_square(self, data_block=512):
        train_set = [0] * data_block
        for i in range(data_block):
            train_set[i] = random.randint(0, 256)
        train_frequency = [(i, train_set.count(i)) for i in range(256)]
        biggest_item = float(max([item[1] for item in train_frequency]))
        return [(item, float(train_frequency[i][1])/biggest_item) for item in range(256)]