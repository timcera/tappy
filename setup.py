# -*- coding: utf-8 -*-

import os
import shlex
import subprocess
import sys

from setuptools import find_packages, setup

# temporarily redirect config directory to prevent matplotlib importing
# testing that for writeable directory which results in sandbox error in
# certain easy_install versions
os.environ["MPLCONFIGDIR"] = "."

pkg_name = "tappy"

version = open("VERSION").readline().strip()

scripts=['tappy.py']
packages=[
    'tappy_lib',
    ]

if sys.argv[-1] == "publish":
    subprocess.run(shlex.split("cleanpy ."))
    subprocess.run(shlex.split("python setup.py sdist"))
    subprocess.run(shlex.split(f"twine upload dist/{pkg_name}-{version}.tar.gz"))
    sys.exit()

README = open("README.rst").read()

install_requires = [
    # List your project dependencies here.
    # For more details, see:
    # http://packages.python.org/distribute/setuptools.html#declaring-dependencies
    "astronomia",
    "pyparsing",
]

extras_require = {
    "dev": [
        "black",
        "cleanpy",
        "twine",
        "pytest",
        "coverage[toml]",
        "flake8",
        "pytest-cov",
        "pytest-mpl",
        "pre-commit",
        "black-nbconvert",
        "blacken-docs",
        "velin",
        "isort",
        "pyroma",
        "pyupgrade",
        "commitizen",
    ]
}

setup(
    name=pkg_name,
    version=version,
    description="Tidal Analysis Program - Python",
    long_description=README,
    classifiers=[
        # Get strings from
        # http://pypi.python.org/pypi?%3Aaction=list_classifiers
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Science/Research",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Developers",
        "Environment :: Console",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Scientific/Engineering",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],  # strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords="time_series",
    author="Tim Cera, PE",
    author_email="tim@cerazone.net",
    url=f"http://timcera.bitbucket.io/{pkg_name}/docs/index.html",
    license="BSD",
    zip_safe=False,
    install_requires=install_requires,
    extras_require=extras_require,
    test_suite="tests",
    python_requires=">=3.7.1",
    scripts=scripts,
    packages=packages,
)
