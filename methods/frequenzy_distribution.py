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

class FrequencyDistribution(object):
    """
    Counting the frequency of bytes. 
    
    The a-law function is used to optimize the finger print.
    We generate a combined finger print from training samples.
     
    A correlation factor is calculated for every byte to get characteristics. 
    We generate a combined correlation factor finger print from training samples.
    0 means low correlation, byte is unimportant for finger print.
    1, byte is most important for the finger print.
    
    Frequency is normalized to 0-1.
    
    Papers:
    Content Based File Type Detection Algorithms, Mason McDaniel
    """
    
    def __init__(self):
        self.finger_print = [0]*256
        self.num_fprints = 0
        self.correlation_print = [0]*256
    
    def a_law(self, x):
        # Optimizes distributions with high peaks. 
        # 87.7 is an experimental value from experiments with radio frequencies
        # 5.4739 = 1 + math.log(A) and 0.0114 = 1/A
        A = 87.7
        x = math.fabs(x)
        if x < 0.0114:
            y = A*x/(5.4739)
        elif 0.0114 <= x <= 1:
            y = (1 + math.log(A*x))/(5.4739)
        return y
    
    def combined_finger_print(self, old_score, num_fprints, new_print):
        # calculate a combined finger print from the analyzed fragments 
        combined_score = ((old_score * num_fprints) + new_print) / (num_fprints + 1)
        return combined_score
    
    def gen_finger_print(self, normalized_frequency_list):
        for item in normalized_frequency_list:
            self.finger_print[item[0]] = self.combined_finger_print(
                                        self.finger_print[item[0]],
                                        self.num_fprints, 
                                        item[1])
    
    def to_tuple_list(self, list):
        tuple_list = []
        for i in range(256):
            tuple_list.append((i, list[i]))
        return tuple_list
    
    def gen_correlation_list(self, normalized_frequency_list):
        for item in normalized_frequency_list:
            self.correlation_print[item[0]] = self.combined_correlation_factor(
                    self.correlation_print[item[0]],
                    self.num_fprints, 
                    self.correlation_factor(self.correlation_print[item[0]] - item[1]))
    
    def correlation_factor(self, frequency_diff):
        # generates a correlation factor from a frequency difference. 
        sigma = 0.0375
        corr_factor = math.exp(math.pow(-frequency_diff, 2)/2*math.pow(sigma, 2))
        return corr_factor
    
    def combined_correlation_factor(self, old_strength, num_blocks, new_factor):
        # calculate a combined correlation factor from the analyzed fragments 
        combined_factor = ((old_strength * num_blocks) + new_factor) / (num_blocks + 1)
        return combined_factor
    
    def normalize_freq_list(self, frequency_list):
        biggest_item = float(max([item[1] for item in frequency_list]))
        return [(item[0], float(item[1])/biggest_item) for item in frequency_list]
    
    def byte_frequency(self, chars):
        # build byte frequency distribution
        # TODO: Use the a-law algorithm if we need it.
        frequency_list = [(ord(c),chars.count(c)) for c in set(chars)]
        normalized_frequency_list = self.normalize_freq_list(frequency_list) 
        return normalized_frequency_list