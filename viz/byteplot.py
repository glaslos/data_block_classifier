from PIL import Image
import numpy
import random


class BytePlot(object):
    
    def __init__(self):
        pass
    
    def new_image(self, width, height):
        self.im = Image.new('L', (width, height), 'white')
        
    def write_data(self, path):
        fd = open(path, 'rb')
        read_data = numpy.fromfile(file=fd, dtype=numpy.uint8)
        self.im.putdata(read_data)
        
    def save(self, path='plots/byteplot.png'):
        self.im.save(path)
        
if __name__ == "__main__":
    bp = BytePlot()
    data = numpy.random.randint(0, 255, size=10000)
    bp.new_image(100, 100)
    data = [random.randint(0,255) for r in xrange(10000)]
    bp.write_data(data)
    bp.save('../plots/byteplot.png')