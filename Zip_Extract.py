import patoolib
import multiprocessing as mp
import os

SOURCE_PATH = 0
DESTINATION_PATH = 1


def get_files(path):
    files = []
    files = os.listdir(path)
    return files

def get_compressed_files(path):
    files = []
    files = get_files(path)
    compressed_files = []

    for l in range(len(files)):
        if files[l][-4:] == ".zip" or files[l][-4:] == ".rar":
            # file_path = f'{path[SOURCE_PATH]}\{files[l][:-4]}'
            compressed_files.append((files[l]))

    return compressed_files

def unpack_zip(zipfile='', path_from_local=''):
    filepath = f'{path_from_local}{zipfile}'
    if(zipfile[-4:] == '.zip'):
        extract_path = filepath.strip('.zip') + '\\'
    elif(zipfile[-4:] == '.rar'):
        extract_path = filepath.strip('.rar') + '\\'
    else:
        print("Invalid File Type")
        return False
    # parent_archive.extractall(extract_path)
    patoolib.extract_archive(f'{path_from_local}\{zipfile}', outdir=extract_path)
    # namelist = parent_archive.namelist()
    # namelist = os.listdir(extract_path)
    namelist = get_compressed_files(extract_path)
    # parent_archive.close()
    for name in namelist:
        try:
            if (name[-4:] == '.zip' or name[-4:] == '.rar'):
                unpack_zip(zipfile=name, path_from_local=extract_path)
        except:
            print ('failed on', name)
            pass
    return extract_path


def get_initial_paths():
    path = []
    with open("Config.txt") as config:
        for line in config:
            #Get the file path
            path.append(line.split(": ", 1)[1])
        #Strip \n from the end of the first string
        path[0] = path[0].strip() 
    return path

def main():
    # unzip_pool = mp.Pool[4]
    path = get_initial_paths()
    files = []
    files = get_compressed_files(path[SOURCE_PATH])
    for zip_file in files:
        unpack_zip(zip_file, path[SOURCE_PATH])
    # unzip_pool.appy_async(unzip)


if __name__ == '__main__':
    main()