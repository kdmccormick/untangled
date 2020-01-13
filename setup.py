#!/usr/bin/env python3
"""
Configuration for Untangled Python package.
"""

import os
import sys

from setuptools import setup

VERSION = "0.1"

if sys.argv[-1] == "tag":
    print("Tagging the version on github:")
    os.system(u"git tag -a %s -m 'version %s'" % (VERSION, VERSION))
    os.system("git push --tags")
    sys.exit()

README = open(os.path.join(os.path.dirname(__file__), "README.md")).read()
CHANGELOG = open(os.path.join(os.path.dirname(__file__), "CHANGELOG.md")).read()

SETUP_INFO = dict(
    name="untangled",
    version=VERSION,
    author="Kyle D. McCormick",
    author_email="kdmc@pm.me",
    url="http://github.com/kdmccormick/untangled",
    include_package_data=True,
    packages=["untangled"],
    download_url="http://pypi.python.org/pypi/untangled",
    description="Untangle large Python projects by analyzing internal dependency relationships.",
    long_description=README + "\n\n" + CHANGELOG,
    license="Apache Software License 2.0",
    classifiers=[
        "Development Status :: 1 - Planning",
        "Environment :: MacOS X",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Testing",
        "Intended Audience :: Developers",
        "Natural Language :: English",
    ],
    zip_safe=True,
    install_requires=[],
)

setup(**SETUP_INFO)
