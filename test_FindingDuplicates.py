import os
import unittest
import time
from Duplicates import *

base_path = 'W:\Work\PythianTask\Testing'


class MyTestCase(unittest.TestCase):
    def setUpTestData(cls):
        create_dir(10,base_path)
        create_file(10,base_path)


    def test_creation(self, base_path='W:\Work\PythianTask\TestingDir'):
        startTime =time.time()
        testingDuplicates = Duplicates(base_path)
        testingDuplicates.createFileHashDict(base_path)
        endTime = time.time()
        data = list_subdir(base_path)
        # self.assertEqual(10,data['total_subdirs'] )



def create_dir(number_of_dir, base_path):
    access_rights = 0o755

    try:

        path_list = []
        for i in range(number_of_dir):
            final_path = os.path.join(base_path, '%s' % str(i))
            os.mkdir(final_path, access_rights)
            # create_file(number_of_dir,final_path)
            path_list.append(final_path)
        create_file(path_list)

    except OSError:
        print("Creation of the directory %s failed" % access_rights)
    else:
        print("Successfully created the directory %s" % access_rights)


def create_file(path):
    # for item in range(number_of_file):
    #     # path = os.path.join(path, str(item))
    #     with open("%s.txt" % path, "w") as f:
    #         f.write(str(item))
    #         f.close()

    for item in path:
        with open(item, "w") as f:
            f.write("This is my first line of code")

def list_subdir(base_path):
    base_path = 'W:\Work\PythianTask\Testing'
    data = dict()
    for entry in os.listdir(base_path):
        if os.path.isdir(os.path.join(base_path, entry)):
            print(entry)
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
    Total_subdirs = []
    Total_file = []
    for dirName, subdirs, fileList in os.walk(base_path):
        if len(subdirs) == 0:
            pass
        else:
            for subdirs in subdirs:
                Total_subdirs.append(subdirs)
        for file in fileList:
            Total_file.append(file)
    data['number_of_total_file'] = len(Total_file)
    data['number_of_total_subdirs'] = len(Total_subdirs)
    data['total_subdirs'] = Total_subdirs
    data['total_file'] = Total_file

    return data

# 3
#
# path = 'W:\Work\PythianTask\TestingDir\Test1File7'
# # create_dir(10)
# # create_file(10, path)
# list_subdir()
