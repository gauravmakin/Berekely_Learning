import numpy as np

class _file_operations:
    def write_my_file(my_array):
        my_array.tofile('myfile.txt',",", format="%s")

    def read_my_file(my_file):
        reading = open(my_file, 'r')
        contents = reading.readlines()
        reading.close()
        return contents



my_array =np.arange(5,45,7)
_file_operations.write_my_file(my_array)










