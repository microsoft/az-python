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

setuptools = "setuptools>=54.2.0,<=54.2.0"

def read_requirements(file_path):
    return io.open(file_path, encoding="utf-8").read()

core_requires = read_requirements("./requirements.txt")

ama_requires = read_requirements("./ai-python/msft/ama.requirements.txt")
maro_requires = read_requirements("./ai-python/maro/maro.requirements.txt")

fclib_requires = read_requirements("./ai-python/retail/fclib.requirements.txt")

fsi_risk_requires = read_requirements("./ai-python/fsi/risk.requirements.txt")

log_ro_requires = read_requirements("./ai-python/log/ro.requirements.txt")
log_ip_requires = read_requirements("./ai-python/log/ip.requirements.txt")
log_ecr_requires = read_requirements("./ai-python/log/ecr.requirements.txt")

test_requires = io.open("./test/requirements.txt", encoding="utf-8").read()

extras = {
    "required": [],
    "all": core_requires + fclib_requires + maro_requires + fsi_risk_requires + log_ro_requires + log_ip_requires + log_ecr_requires,
    "core": core_requires,
    "test": test_requires,
    "ama": ama_requires,
    "maro": maro_requires,
    "retai": fclib_requires,
    "fclib": fclib_requires,
    "fsi": fsi_risk_requires
    "fsi-risk": fsi_risk_requires,
    "log": log_ro_requires + log_ip_requires + log_ecr_requires,
    "log-ro": log_ro_requires,
    "log-ip": log_ip_requires,
    "log-ecr": log_ecr_requires,
}

SETUP_REQUIRES = [
    "jupyter-packaging==0.7.12",
    "numpy==1.19.5",
    "pip-tools==5.5.0",
    "scikit-build==0.11.1",
    "scipy==1.4.1",
]


setup(
    name="ai-python",
    version="0.1.8",
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
    setup_requires=SETUP_REQUIRES,
    extras_require=extras,
    packages=find_packages(exclude=["tests", "tests.*", "examples", "examples.*"]),
    include_package_data=True,
    zip_safe=False,
)
