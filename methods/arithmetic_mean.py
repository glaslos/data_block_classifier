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


class ArithmeticMean(object):
    """Calculates the arithmetic mean of the byte values
    
    Papers:
    Automated mapping of large binary objects using primitive fragment type classification, Gregory Conti
    """
    def __init__(self):
        pass
    
    def clac_arithmetic_byte_mean(self, normalize_freq_list, block_size = 512):
        mean = sum([val[0] for val in normalize_freq_list]) / block_size
        return mean