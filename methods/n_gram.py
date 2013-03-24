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

from operator import itemgetter
from collections import defaultdict

class NGram(object):
    """
    Find patterns which could server as a file type identifier.
    
    Small n could match files with high entropy: compressed and encrypted.
    
    Papers:
    Embedded Malware Detection using Markov n-grams, M. Zubair Shafiq
    Fileprints: Identifying File Types by n-gram Analysis, Wei-Jen Li
    Filetype Identification Using Long, Summarized N-Grams, Ryan C. Mayer
    """
    def __init__(self):
        pass
    
    def calc_ngram(self, inputstring, nlen = 3):
        ngram_list = [inputstring[x:x+nlen] for x in xrange(len(inputstring)-nlen+1)]
        ngram_freq = defaultdict(int)
        for j in ngram_list:
            ngram_freq[j] += 1
        return sorted(ngram_freq.iteritems(), key=itemgetter(1), reverse=True)