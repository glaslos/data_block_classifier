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

from pychart import canvas, theme, axis, area, bar_plot, line_plot, line_style

class BarChart(object):

    def __init__(self):
        pass

    def bar_chart(self, data, name):
        canvas.init
        format_extension = 'png'
        theme.output_format = format_extension
        theme.output_file = 'charts/' + name + '.' + format_extension
        theme.use_color = 1
        theme.reinitialize()
        
        xaxis=axis.X(label="Char", format = '/a90{}%s', tic_interval = 30)
        yaxis=axis.Y(label="Frequency", tic_interval = 0.1)
        ar = area.T(size = (300, 150),
                    y_range=(0,1),
                    x_range=(0,255),
                    x_axis=xaxis, 
                    y_axis=yaxis
                    )
        ar.add_plot(bar_plot.T(label="Frequency", data=data, width = 0.1),)
        ar.draw()
        canvas.close()

class LineChart(object):
    def __init__(self):
        pass
    
    def line_chart(self, data, name):
        canvas.init
        format_extension = 'pdf'
        theme.output_format = format_extension 
        theme.output_file = 'charts/' + name + '.' + format_extension
        theme.use_color = 1
        theme.reinitialize()
        
        xaxis=axis.X(label="Char", format = '/a90{}%s', tic_interval = 30)
        yaxis=axis.Y(label="Frequency", tic_interval=0.1)
        ar = area.T(size = (300, 150),
                    y_range=(0,1),
                    x_range=(0,255),
                    x_axis=xaxis,
                    y_axis=yaxis
                    )
        lp = line_plot.T(label="Frequency", data=data, line_style=line_style.T(width = 0.2))
        ar.add_plot(lp)
        ar.draw()
        canvas.close()

class FrequencyVisualization(object):
    
    def __init__(self, data, name):
        #bar = BarChart()
        #bar.bar_chart(data, name)
        line = LineChart()
        line.line_chart(data, name) 