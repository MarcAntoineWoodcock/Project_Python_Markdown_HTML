# Project_Python_Markdown_HTML

This tool converts any markdown file into HTML to do a static site builder.

What is a static website ?
A static website is a site only composed of files in a folder:

- HTML files,
- CSS files,
- JavaScript files,
- pictures,
- videos,

This is opposed to dynamic websites, where some of these files are generated on the air by software, for example from data in a database.


# Host a static site
Hosting a dynamic site is more complex than for a static site, it is indeed necessary to install the software that will generate the files on the air. But on the other hand, hosting a static site is relatively simple, you just have a small web server that provides the folder containing static files.

# Github
Github provides free static site hosting. Just create a git repository with Github, and commit to a specific branch.


# Project
I will make a tool that converts a folder of markdown files and pictures into another folder containing the files of a static site. HTML will be generated from the markdown, and this HTML will be mixed with templates of web pages to generate pages all conform to the same model (for example with the same logo, the same summary of website, the same referenced CSS file ... ).



# Realization of a command line interface
I will build a command line tool to generate the static site files. It will take at least as parameters:

- i ./a_folder or --input-directory ./un_folder: the path of the source file folder (containing the markdown files)
- o ./one_other_folder or --output-directory ./one_other_folder: the path of the folder where the files generated for the static site will be put
  - if the file already exists, you are free to either erase it or write it in for updates (this will be explained in the manual of your tool)
  - you can choose the naming convention you like for the generated files, for example you can use as prefix the name of the corresponding markdown file (this will also be explained)
  
-t ./other_folder or --template-directory ./other_folder: possibly the folder containing templates of web pages to be completed
-h or --help: to display help to explain command parameters





#Converting markdown to HTML
I'm going at least convert the following syntaxes:

#, a level 1 title in <h1>
##, a level 2 title in <h2>
###, a level 3 title in <h3>
Convert unordered lists to <ul> and <li>
Convert URLs (http://something.com) to <a href="http://something.com"> http://something.com </a>
* a text *, an important text in <em> a text </ em>
You can do these conversions using any of the following:

the basic functions of Python for strings
regular expressions (https://docs.python.org/en/3/library/re.html)
a community package
https://github.com/Python-Markdown/markdown
https://github.com/trentm/python-markdown2

# Code quality
I will make sure to respect:

PEP 8: https://www.python.org/dev/peps/pep-0008/ (you can help with https://github.com/ambv/black and https://github.com/hhatto/ autopep8)
PEP 20: https://www.python.org/dev/peps/pep-0020/





