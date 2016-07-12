#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

requirements = [
    'Click>=6.0',
]

setup(
    name='qwork',
    version='0.1',
    description="Queue up commands to run in parallel.",
    long_description=readme,
    author="Simon Mutch",
    author_email='smutch.astro@gmail.com',
    url='https://github.com/smutch/qwork',
    entry_points={
        'console_scripts': [
            'qwork=qwork:queue_work'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='qwork',
    classifiers=[
        'Development Status :: 3 - Alpha'
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
