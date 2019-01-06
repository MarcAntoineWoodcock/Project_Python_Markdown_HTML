import sys
import cmd
import os
import os.path
import glob
import markdown2


def main():
    file = glob.glob(
        "/home/marc-antoine/Documents/workspace_python/Md_HTML/source/*.txt"
    )
    file_converti = glob.glob(
        "/home/marc-antoine/Documents/workspace_python/Md_HTML/site_statique/*.txt"
    )
    path = file[0]
    file_html = file_converti[0]
    with open(path, "r") as fichiermarkdown:
        #  Reading the markdown file
        lines = fichiermarkdown.readlines()
        with open(file_html, "w") as file_converti:
            #  Writing in the file 
            for line in lines:
                line = markdown2.markdown(line)
                #  Conversion in HMTL
                file_converti.write(line)
                file_converti.write("\n")
                #  Writing in the conversion file
                
if __name__ == "__main__":
    main()
