# dupFinder.py
import os, sys
import hashlib
import stat
from pytube import YouTube



# duplicates file
def findDup(parentFolder):
    # Dups in format {hash:[names]}
    testing_path = 'W:\Work\PythianTask\TestingDir\\1'
    # linking = gos.link(testing_path, 'tap')
    # os.chmod(testing_path, stat.S_IRUSR | stat.S_IRGRP | stat.S_IROTH)
    # print(os.readlink(testing_path))
    fileList = []
    fileList = os.listdir(testing_path)
    # print('>>>>>>>>>>>>>>>>>>>>>>>> Listing' % fileList)

    count = 0
    dups = {}

    for dirName, subdirs, fileList in os.walk(parentFolder):
        print('Scanning %s...' % dirName)
        for filename in fileList:
            # Get the path to the file
            path = os.path.join(dirName, filename)
            # Calculate hash
            file_hash = hashfile(path)
            # Add or append the file path
            count = count + 1
            if file_hash in dups:
                dups[file_hash].append(path)
            else:
                dups[file_hash] = [path]

    print('>>>>>>> Count : %d ', str(count))
    return dups


# Joins two dictionaries
def joinDicts(dict1, dict2):
    for key in dict2.keys():
        if key in dict1:
            dict1[key] = dict1[key] + dict2[key]
        else:
            dict1[key] = dict2[key]


def hashfile(path, blocksize=65536):
    afile = open(path, 'rb')
    hasher = hashlib.md5()
    buf = afile.read(blocksize)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(blocksize)
    afile.close()
    return hasher.hexdigest()



if __name__ == '__main__':
    if len(sys.argv) > 1:
        dups = {}
        folders = sys.argv[1:]
        for i in folders:
            # Iterate the folders given
            if os.path.exists(i):
                # Find the duplicated files and append them to the dups
                joinDicts(dups, findDup(i))
            else:
                print('%s is not a valid path, please verify' % i)
                sys.exit()
        # printResults(dups)
    else:
        print('Usage: python dupFinder.py folder or python dupFinder.py folder1 folder2 folder3')

# import os
# import sys
#
#
# class testing_dir:
#
#     def __init__(self):
#         self.base_path = 'W:\Work\PythianTask\TestingDir'
#         self.access_rights = 0o755
#
#     def creating_dir(self, i):
#         try:
#             final_path = os.path.join(self.base_path, str(i))
#             os.mkdir(final_path, self.access_rights)
#         except OSError:
#             print("Creation of the directory %s failed" % self.access_rights)
#         else:
#             print("Successfully created the directory %s" % self.access_rights)
#
#     def bulk_dir(self, number_of_dir):
#         for i in range(0, number_of_dir):
#             self.creating_dir(i + 1)
#             print(self.base_path)
#             print(i)
#
#             self.base_path = os.path.join(self.base_path, str(i + 1))
#             print(self.base_path)
#             for j in range(0, number_of_dir):
#                 self.creating_dir(j + 1)
#                 print(j)
#
#     def walking_through_dir(self):
#
#         return sum([len(dirs) for dirs in os.walk(self.base_path)])
#         # for filename in os.listdir(self.base_path):
#         #     print(filename)
#         #     self.base_path = os.path.join(self.base_path, filename)
#         #     return self.walking_through_dir(self.base_path)
#
#
#
#         # os.listdir(self.base_path)
#
#         # return [os.path.join(d, f) for f in os.listdir(d)]
#
#
#         # for filename in os.listdir(self.base_path):
#         #     print(filename)
#
#
#         # print(os.listdir(self.base_path))
#         # for subdir, dirs, files in os.walk(self.base_path):
#
#
#
#             # print(1)
#             # for subdir in dirs:
#             #     print('here')
#             #     print(os.path.join(dirs, subdir))
#             #     print('-----------------------------')
#
#
# if __name__ == '__main__':
#     test = testing_dir()
#     # test.creating_dir('tapan')
#     print(test.walking_through_dir())
#     # test.bulk_dir(5)
#     # test.creating_dir('tapan')
#     # test.creating_dir(1)
