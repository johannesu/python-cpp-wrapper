from distutils.core import setup
from Cython.Build import cythonize
from setuptools import Extension
from os import path

import numpy as np

ext_package = 'boilerplate'
cython = [Extension('utils',
                    [path.join(ext_package, 'utils.pyx')],
                    include_dirs=[np.get_include()])
]

setup(
    name='boilerplate',
    packages=['boilerplate'],
    version='0.0.1',
    description="Python boilerplate project",
    license=open('LICENSE.rst').read(),
    # Setuptools 18.0 properly handles Cython extensions.
    setup_requires=[
        'setuptools>=18.0',
        'cython',
    ],
    author='Johannes Ulén',
    url='https://github.com/johannesu/cython-wrapper-boilerplate',
    keywords=['boilerplate'],
    long_description=open('README.rst').read(),
    ext_package=ext_package,
    ext_modules=cythonize(cython),
)
