# use to batch extract zip files 

import zipfile
import os


def get_files(path):
    f = []
    for (dirpath, dirnames, filenames) in os.walk(path):
        f.extend(filenames)
    return f

def extract(zip_path_in, path_out):
    for file in get_files(zip_path_in):
        zip_path = os.path.join(zip_path_in, file)
        zip_ref = zipfile.ZipFile(zip_path, 'r')
        zip_ref.extractall(path_out)
        zip_ref.close()
        
# extract('extract/zipped JAN', 'extract/extracted')
extract('extract/MAR', 'extract/extracted')
