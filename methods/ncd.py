import zlib

class NormalizedCompressionDistance(object):
    """
    
    Papers:
    The Normalised Compression Distance as a file fragment classifier, Stefan Axelsson
    """
    def __init__(self):
        pass
    
    def ncd(self, a, b):
        # http://jon.oberheide.org/ncd/downloads/ncd.py
        compressed_a = zlib.compress(a)
        compressed_b = zlib.compress(b)
        return (float(len(zlib.compress(a + b)) - len(min(compressed_a, compressed_b)))) / float(len(max(compressed_a, compressed_b)))