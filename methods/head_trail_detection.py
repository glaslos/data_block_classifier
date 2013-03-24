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

class HeaderTrailer(object):
    """
    
    Papers:
    Content Based File Type Detection Algorithms, Mason McDaniel
    """
    def __init__(self):
        pass

    def combined_fingerprint(self, old_score, num_files, new_score):
        # calculate a combined finger print from the analyzed blocks 
        news_score = ((old_score * num_files) + new_score) / (num_files + 1)
        return news_score
    
    def file_header(self, data_block):
        if "%PDF-" in data_block:
            print data_block
        if "startxref" in data_block:
            print data_block
        if ">>stream" in data_block:
            print data_block
        if "FFD8FF" in data_block:
            print data_block
            raw_input('next?')
        
    def file_footer(self, data_block):
        if "%%EOF" in data_block:
            pass