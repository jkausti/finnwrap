#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

#with open('HISTORY.rst') as history_file:
#    history = history_file.read()

requirements = ['spacy>=2.0.16', 'pytest>=3.8.2']

setup_requirements = [ ]

test_requirements = ['spacy>=2.0.16', 'pytest>=3.8.2']

setup(
    author="John Kaustinen",
    author_email='jokausti@gmail.com',
    python_requires='>=3.5, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Operating System :: Linux'
    ],
    description="A Python wrapper for FinnPos, a morphological tagging and lemmatization toolkit.",
    #entry_points={
    #    'console_scripts': [
    #        'finnwrap=finnwrap.cli:main',
    #    ],
    #},
    py_modules=["finnwrap", "finnpos"],
    install_requires=requirements,
    license="GNU General Public License v3",
    long_description=readme,
    include_package_data=True,
    package_data={
        '': ['finnpos/*']
    },
    keywords='finnwrap',
    name='finnwrap',
    packages=find_packages(include=['src', 'finnwrap', 'finnwrap.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/jkausti/finnwrap',
    version='0.1.0',
    zip_safe=False,
)
