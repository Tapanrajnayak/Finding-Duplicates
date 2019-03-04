import os, sys
import hashlib

class Duplicates():


    def __init__(self, parentFolder):
        self.parentfolder = parentFolder


    def createFileHashDict(self, parentFolder):
        all_files_hash_dict = {}
        for dirName, subdirs, fileList in os.walk(parentFolder):
            print('Scanning %s...' % dirName)
            for filename in fileList:
                # Get the path to the file
                path = os.path.join(dirName, filename)
                # Calculate hash
                file_hash = self.hashfile(path)
                if file_hash in all_files_hash_dict:
                    all_files_hash_dict[file_hash].append(path)
                else:
                    all_files_hash_dict[file_hash] = [path]
                # all_files_hash_list.append(file_hash)

        for key, value in all_files_hash_dict.items():
            if len(value) > 1:
                print('Duplicate files detected\n')
                for item in value:
                    print(item)
                print("=====================================================================")
            else:
                pass
        # for value in Counter(all_files_hash_list):
        #     for duplicate_file in all_files_hash_dict[value]:
        #         print(duplicate_file)
        #     print("==============================================================================================================================")

        # print('>>>>>>> Count : %d ', str())
        return all_files_hash_dict


    def hashfile(self, path, blocksize=65536):
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
        folders = sys.argv[1]
        if os.path.exists(folders):
            script = Duplicates(folders)
            script.createFileHashDict(folders)
        else:
            print('%s is not a valid path, please verify' % folders)
            sys.exit()
    else:
        print('USE: python3 Duplicates.py Folder')
