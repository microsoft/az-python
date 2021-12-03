# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.

import io
import os

# NOTE: DO NOT change the import order, as sometimes there is a conflict between setuptools and distutils,
# it will cause following error:
# error: each element of 'ext_modules' option must be an Extension instance or 2-tuple
from setuptools import find_packages
from distutils.core import setup

readme = io.open("./README.md", encoding="utf-8").read()

version = io.open("./VERSION", encoding="utf-8").read()

setuptools = "setuptools>=54.2.0,<=54.2.0"


def read_requirements(file_path):
    return io.open(file_path, encoding="utf-8").read()


core_requires = read_requirements(".depends/requirements.txt")
test_requires = read_requirements(".depends/test.requirements.txt")

energy_km_requires = read_requirements(".depends/en.km.requirements.txt")


all = (
    core_requires
    + energy_km_requires
)

extras = {
    "required": [],
    "all": all,
    "core": core_requires,
    "test": test_requires,
    "energy-km": energy_km_requires,
}


setup(
    name="ai-python",
    version=version,
    description="Microsoft AI Python Package",
    long_description=readme,
    long_description_content_type="text/x-rst",
    author="Daniel Ciborowski",
    author_email="dciborow@microsoft.com",
    url="https://github.com/microsoft/ai-python",
    project_urls={
        "Code": "https://github.com/microsoft/ai-python",
        "Issues": "https://github.com/microsoft/ai-python/issues",
        "Documents": "https://github.com/microsoft/ai-python"
    },
    license="MIT License",
    platforms=["Windows", "Linux", "macOS"],
    keywords=["ai"],
    classifiers=[
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: MacOS',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Topic :: Scientific/Engineering :: Artificial Intelligence"],
    python_requires=">=3.7,<3.8",
    extras_require=extras,
    packages=find_packages(exclude=["tests", "tests.*", "examples", "examples.*"]),
    include_package_data=True,
    zip_safe=False,
)
