import os, sys
import hashlib
from collections import Counter




def createFileHashDict(parentFolder):
    # Dups in format {hash:[names]}
    all_files_hash_dict = {}
    all_files_hash_list = []
    for dirName, subdirs, fileList in os.walk(parentFolder):
        print('Scanning %s...' % dirName)
        for filename in fileList:
            # Get the path to the file
            path = os.path.join(dirName, filename)
            # Calculate hash
            file_hash = hashfile(path)
            if file_hash in all_files_hash_dict:
                all_files_hash_dict[file_hash].append(path)
            else:
                all_files_hash_dict[file_hash] = [path]
            all_files_hash_list.append(file_hash)

    for value in Counter(all_files_hash_list):
        for duplicate_file in all_files_hash_dict[value]:
            print(duplicate_file)
        print("==============================================================================================================================")

    # print('>>>>>>> Count : %d ', str())
    return all_files_hash_dict


def hashfile(path, blocksize=65536):
    afile = open(path, 'rb')
    hasher = hashlib.md5()

    buf = afile.read(blocksize)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(blocksize)
    afile.close()
    return hasher.hexdigest()

createFileHashDict("./TestingDir/")