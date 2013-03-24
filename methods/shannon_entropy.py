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

class ShannonEntropy(object):
    """
    
    Papers:
    Automated mapping of large binary objects using primitive fragment type classification, Gregory Conti
    Shannon Entropy
    """
    def __init__(self):
        self.entropy = 0.0
    
    def calc_shannon_entropy(self, normalized_freq_list):
        # Markov model with order-0 source 
        self.entropy = sum([-float(freq[1]) * math.log(float(freq[1]), 2) for freq in normalized_freq_list if freq[1] > 0])
        return self.entropy