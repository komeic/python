#!/usr/bin/env python
import sys
import os

class preprocess:
    """preprocessing a file"""

    def __init__(self, filename):
        """ read file contents into buffer """
        self.name = filename
        fp = open(filename, 'r')
        self.lines = fp.readlines()
        fp.close()

    def writeFile(self):
        """ write buffer into a file """
        fp = open(self.name, 'w')
        for line in self.lines:
            fp.write(line)
        fp.close()

    def replaceSpace(self):
        """replace space in file name with '_' """
        orig_name = self.name
        self.name = self.name.replace(' ', '_')
        os.rename(orig_name, self.name)

    def rmLine(self):
        """remove 1st line """
        self.lines = self.lines[1:]

    def printLines(self):
        """Helper func for debug.
           Print all lines"""
        for line in self.lines:
            print line

if __name__ == '__main__':
    args = sys.argv

    # if not given specific file name,
    #   apply to all files in './data/' directory.
    # if filename given, it should be relative path.
    # Caution: it will overwrite the file
    #          if want to save as other file, change arg to writeFile()

    dataDir = "./data/"

    if len(sys.argv)==1:
        for file in os.listdir(dataDir):
            obj = preprocess(dataDir+file)
            obj.replaceSpace()
            obj.rmLine()
            obj.writeFile()
    else:
        for file in args[1:]:
            obj = preprocess(file)
            obj.replaceSpace()
            obj.rmLine()
            obj.writeFile()
