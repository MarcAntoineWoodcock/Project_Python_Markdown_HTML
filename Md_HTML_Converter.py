import sys
import cmd
import argparse
from math import *
import os
import os.path
import glob
import getopt
import markdown
import markdown2


def main():
    from markdown2 import Markdown

    file = glob.glob(
        "/home/marc-antoine/Documents/workspace_python/Md_HTML/source/*.txt"
    )
    file_converti = glob.glob(
        "/home/marc-antoine/Documents/workspace_python/Md_HTML/site_statique/*.txt"
    )
    
    path = file[0]
    
    file_html = file_converti[0]
    with open(path, "r") as fichiermarkdown:
        #  Lecture du fichier qui contient le code markdown
        lignes = fichiermarkdown.readlines()
        with open(file_html, "w") as file_converti:
            #  Ecriture dans le fichier qui va contenir la conversion en html
            for ligne in lignes:
                ligne = markdown2.markdown(ligne)
                #  Conversion en html de la ligne pointé
                file_converti.write(ligne)
                file_converti.write("\n")
                #  Ecriture dans le fichier de la conversion effectue
                #  En y ajoutant un retour à la ligne


if __name__ == "__main__":
    main()
