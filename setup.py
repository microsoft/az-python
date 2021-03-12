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

setup(
    name="microsoft-ai-python",
    version="0.0.0",
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
    keywords=[
        "ai",
    ],
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
    setup_requires=[
        "jupyter-packaging==0.7.11",
        "numpy==1.19.5",
        "pip-tools==5.5.0",
        "scikit-build==0.11.1",
        "scipy==1.4.1",
    ],
    install_requires=[      
        "holidays==0.10.3",
        "pyaml==20.4.0",
        "redis==3.5.3",
        "pyzmq==19.0.2",
        "requests==2.24.0",
        "psutil==5.7.2",
        "deepdiff==5.0.2",
        "azure-storage-blob<13.0.0,>=12.6.0",
        "azure-storage-common==2.1.0",
        "geopy==2.1.0",
        "pandas==0.25.3",
        "PyYAML==5.3.1",
        "paramiko==2.7.2"
    ],
    entry_points={
    },
    packages=find_packages(exclude=["tests", "tests.*", "examples", "examples.*"]),
    include_package_data=True,
    package_data={
    },
    zip_safe=False,
    ext_modules=extensions,
)
