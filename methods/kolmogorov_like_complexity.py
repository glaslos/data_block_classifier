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

from collections import defaultdict


class KolmogorovLikeComplexity(object):
    """

    Papers:
    Statistical Disk Cluster Classification for File Carving, Cor J. Veenman
    Kolmogorov Complexity Estimates For Detection Of Viruses In Biologically Inspired Security Systems: A Comparison With Traditional Approaches, Sanjay Goel
    Kolmogorov Complexsity and Hausdorff Dimension, LudwigStaiger
    """
    def __init__(self):
        control = [i for i in range(32)]
        # Adding the delete character (127)
        control.extend([127, ])
        self.character_categories = {
            "control": control,
            "punctuation": [33, 34, 40, 41, 43, 44, 45, 46, 47, 58, 59, 60, 61,
                            62, 63, 91, 93, 94, 123, 125, ],
            "word_divider": [32, ],
            "typography": [35, 37, 38, 64, 92, 95, 124, 126, ],
            "currency": [36, ],
            "diacritical": [39, 96, ],
            "uppercase_letters": [i for i in range(65, 91)],
            "lowecase_letters": [i for i in range(97, 123)],
            "numbers": [i for i in range(48, 58)],
            "non_printable": [i for i in range(128, 256)],
        }

    def gen_lookup_table(self):
        lookup = {}
        for cat, nums in self.character_categories.iteritems():
            for n in nums:
                lookup[n] = cat
        print len(lookup)
        
        categorized = defaultdict(list)
        for n in numbers:
            categorized[lookup[n]].append(n)
            print "put %d in category %s" % (n, lookup[n])
            
        
if __name__ == "__main__":
    kc = KolmogorovLikeComplexity()
    kc.gen_lookup_table()