# -*- coding: utf-8 -*-
"""Installer for the collective.js.rgraph package."""

from setuptools import find_packages
from setuptools import setup

long_description = (
    open('README.rst').read()
    + '\n' +
    'Contributors\n'
    '============\n'
    + '\n' +
    open('CONTRIBUTORS.rst').read()
    + '\n' +
    open('CHANGES.rst').read()
    + '\n')


setup(
    name='collective.js.rgraph',
    version='1.0',
    description="Rgraph library for Plone",
    long_description=long_description,
    # Get more from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
    	"Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: 4.2.3",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
    ],
    keywords='javascript, charts, Plone',
    author='Cédric Messiant',
    author_email='cedricmessiant@ecreall.com',
    url='http://pypi.python.org/pypi/collective.js.rgraph',
    license='GPL',
    packages=find_packages('src', exclude=['ez_setup']),
    namespace_packages=['collective', 'collective.js'],
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'five.grok',
        'plone.api',
        'setuptools',
    ],
    extras_require={
        'test': [
            'plone.app.testing',
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)