import sys
import cmd
import argparse
import os
import os.path
import glob
import getopt


def main(argv):
    if len(argv) > 0: 
        if "-i" in argv:
            file = glob.glob(argv[2])
            print(file)
        else :
            print ("The path does not exist or is not found")
               
        if "-o" in argv:
          print("The path of the folder containing the website file is: ", argv[4])
          file = glob.glob(argv[4])
        else :
            print ("The path does not exist or is not found")

        parser = argparse.ArgumentParser(description=" Static site creation"    
        parser.add_argument("-i","--input-directory",
            default="chemin",
            action="append",
            help=" Corresponds to the sources' path file folder (containing the markdown files)",
        )
        args = parser.parse_args()

        parser.add_argument("-o","--output-directory",
            help="Corresponds to the path folder where the files are generated for the static website",
            required=False,
        )
        args = parser.parse_args()
        parser.add_argument("-t","--template-directory",
            help=" Corresponds to the folder containing templates of web pages to complete",
            required=False,
        )
        args = parser.parse_args()

    if len(argv):
        print ("Error, Missing arguments please refer to -h for any kind of help")
             


if __name__ == "__main__":
    main(sys.argv)
