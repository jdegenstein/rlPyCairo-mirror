#!/usr/bin/env python
from setuptools import setup, find_packages
from rlPyCairo import __version__ as version

requires = [str(x).strip() for x in open('requirements.txt').readlines() if '-i' not in x]

setup_kwargs = {str('install_requires'): requires}


# on py3, all these are text strings
# on py2, they're all byte strings.
# ... and that's how setuptools likes it.
setup(
    name=str('rlPyCairo'),
    description=str('''Plugin backend renderer for reportlab.graphics.renderPM'''),
    version=version,
    author=str('Robin Becker'),
    author_email=str('andy@reportlab.com'),
    url=str('https://www.reportlab.com/pypi/rlPyCairo'),
    long_description=open('README.txt').read(),
    keywords=str('reportlab renderPM'),
    packages=find_packages(exclude=['test']),
    license="BSD license, Copyright (c) 2000-2021, ReportLab Inc.",

    include_package_data=True,
    classifiers=[
        str('Development Status :: 2 - Pre-Alpha'),
        str('Environment :: Web Environment'),
        str('Intended Audience :: Developers'),
        str('License :: OSI Approved :: BSD License'),
        str('Operating System :: OS Independent'),
        str('Programming Language :: Python'),
        str('Programming Language :: Python :: 3'),
        str('Programming Language :: Python :: 3.6'),
        str('Programming Language :: Python :: 3.7'),
        str('Programming Language :: Python :: 3.8'),
        str('Programming Language :: Python :: 3.9'),
        str('Topic :: Utilities'),
    ],
    python_requires='>=3.6,<4',
    install_requires=['pycairo>=1.20.0'],
    **setup_kwargs
    )
