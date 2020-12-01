#!/usr/bin/python3

import os

from glob import glob
from shutil import copytree, rmtree

LICENSE = '''Copyright (c) 2018 The Python Packaging Authority

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

SETUP = '''
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='bontu-library',
    version='0.1.1',
    author="BontuTeam",
    author_email="carlos.anorve@alphacredit.mx",
    description="Layers for lambdas",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['boto3>=1.10.2', 'pandas>=0.25.2', 'peewee>=3.13.1', 'psycopg2>=2.8.4', 'requests>=2.22.0',
                      'firebase-admin>=3.2.1', 'tqdm', 'xlsxwriter>=1.2.8', 'qrcode==6.1', 'Pillow==6.2.1',
                      'pyOpenSSL==18.0.0', 'clabe==0.2.3', 'pydantic==1.4', 'sendgrid==6.2.2', 'img2pdf==0.3.6',
                      'xlrd==1.2.0', 'pdfkit==0.6.1', 'xmltodict==0.12.0', 'PyPDF2==1.26.0', 'fpdf==1.7.2', 
                      'lxml==4.5.0','unidecode==1.1.1', 'pdfrw', 'PyMuPDF>=1.17.7','uuid','pybase64'],
    python_requires='>=3.6',
)
'''

README = '''
# Example Package

This is a simple example package. You can use
[Github-flavored Markdown](https://guides.github.com/features/mastering-markdown/)
to write your content.

'''

paths = {folder: os.path.join('.', 'tmp', os.path.split(folder)[1]) for folder, sub_paths, files in
         os.walk('../src/layers') if len(files) > 1}

files = {
    '.' + os.sep + 'tmp' + os.sep + 'LICENSE': LICENSE,
    '.' + os.sep + 'tmp' + os.sep + 'README.md': README,
    '.' + os.sep + 'tmp' + os.sep + 'setup.py': SETUP
}
for e in paths:
    copytree(e, paths[e])

for file in files:
    with open(file, 'w') as ff:
        ff.write(files[file])
os.chdir('tmp')
os.system('pip install setuptools wheel')
os.system(r'python setup.py sdist bdist_wheel')
try:
    os.system('pip uninstall  bontu-library')
except Exception as details:
    print(details)
    raise Exception('Error')
os.system(r'pip install {}'.format(glob(os.path.join('.', 'dist', '*.whl'))[0]))
os.chdir('..')
rmtree('.' + os.sep + 'tmp')
