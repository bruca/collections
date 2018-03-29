import re
import os.path
from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__), 'collection', '__init__.py')) as v_file:
    package_version = re.compile(r".*__version__ = '(.?)'", re.S).match(v_file.read()).group(1)

setup(
    name='collections',
    version=package_version,
    desctiption='Collection utils',
    url='',
    author='Bruca Lock',
    license='GPLv3',
    keywords='collection collections vector list',
    classifiers=[
        'Development Status :: 1 - Prototype',
        'Environment :: Any',
        'Intended Audience :: Developpers',
        'Operating System :: Linux',
        'Operating System :: MAC',
        'Programming Language :: Python :: 3 :: Only'
    ],
    packages=find_packages(),
    include_package_data=False,
    zip_safe=False
)
