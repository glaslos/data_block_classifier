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

import time
import os
import math

from viz import visualize, byteplot

from methods import frequenzy_distribution


class FragmentClassification(object):
    """
    Classifies file fragments using various methods.
    
    Parameter:
        target: readable data
        block size: > 0 in bytes (default 512)
        concurrency factor: 1 - x, parallel processes (default 1)
        train: If True, generate a finger print (default False)
    
    Output: File fragment start number, classified type, encoding
        Example: 521 txt-ASCII
    """
    def __init__(self, target, block_size=512, concurrency_factor=1, train=False, plot=False):
        self.block_size = block_size
        self.target = target
        self.train = train
        self.previous_block = ""
        if plot:
            self.bp = byteplot.BytePlot()
            height = int(math.ceil(os.path.getsize(target)/block_size)) + 1
            self.bp.new_image(block_size, height)
            self.bp.write_data(self.target)
            self.bp.save()
        start = time.time()
        self.process_target()
        print time.time() - start
        
    def process_target(self):
        self.freq = frequenzy_distribution.FrequencyDistribution()
        with file(self.target, 'rb') as self.sample:
            self.data_block = self.sample.read(self.block_size)
            while self.data_block:
                self.freq.num_fprints += 1
                data = self.freq.byte_frequency(self.data_block)
                if self.train:
                    self.freq.gen_finger_print(data)
                    self.freq.gen_correlation_list(data)
                self.data_block = self.sample.read(self.block_size)
        if self.train:
            visualize.FrequencyVisualization(
                self.freq.to_tuple_list(self.freq.finger_print), "finger_print"
                )
            visualize.FrequencyVisualization(
                self.freq.to_tuple_list(self.freq.correlation_print), "correlation_print"
                )


if __name__ == "__main__":
    FragmentClassification('docs/A New Approach to Content-based File Type Detection.pdf', 512, 1, False)