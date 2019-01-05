import sys
import cmd
import argparse
from math import *
import os
import os.path


def main(argv):
        parser.add_argument("-i","--input-directory",
            help="le chemin du dossier de fichiers source (contenant les fichiers markdown)",
        )
        args = parser.parse_args()

        parser.add_argument("-o","--output-directory",
            help="le chemin du dossier où seront mis les fichiers générés pour le site statique ",
            required=False,
        )
        args = parser.parse_args()
        parser.add_argument("-t","--template-directory",
            help="le dossier contenant des modèles de pages web à compléter",
            required=False,
        )
        args = parser.parse_args()


if __name__ == "__main__":
    main(sys.argv)
