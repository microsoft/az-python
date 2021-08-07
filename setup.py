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

msft_ama_requires = read_requirements(".depends/msft.ama.requirements.txt")
msft_utils_requires = read_requirements(".depends/msft.utils.requirements.txt")

fclib_requires = read_requirements(".depends/re.fclib.requirements.txt")
reco_requires = read_requirements(".depends/msft.reco.requirements.txt")

energy_ca_requires = read_requirements(".depends/en.ca.requirements.txt")
energy_km_requires = read_requirements(".depends/en.km.requirements.txt")

gem_ent_requires = read_requirements(".depends/gem.ent.requirements.txt")
gem_reco_requires = read_requirements(".depends/gem.reco.requirements.txt")

retail_requires = read_requirements(".depends/re.retail.requirements.txt")

fsi_nlp_requires = read_requirements(".depends/fsi.nlp.requirements.txt")
fsi_risk_requires = read_requirements(".depends/fsi.risk.requirements.txt")

sc_ro_requires = read_requirements(".depends/sc.ro.requirements.txt")
sc_ip_requires = read_requirements(".depends/sc.ip.requirements.txt")
sc_ecr_requires = read_requirements(".depends/sc.ecr.requirements.txt")

cdm_requires = read_requirements(".depends/cdm.cdm.requirements.txt")
maro_requires = read_requirements(".depends/maro.maro.requirements.txt")

all = (
    core_requires
    + msft_ama_requires + msft_utils_requires
    + energy_ca_requires + energy_km_requires
    + fclib_requires
    + fsi_nlp_requires + fsi_risk_requires
    + gem_ent_requires + gem_reco_requires
    + retail_requires
    + sc_ecr_requires + sc_ro_requires + sc_ip_requires
    + cdm_requires
    + maro_requires    
)

extras = {
    "required": [],
    "all": all,
    "core": core_requires,
    "test": test_requires,
    "ama": msft_ama_requires,
    "fclib": fclib_requires,
    "reco": reco_requires,
    "msft-utils": msft_utils_requires,
    "retail": retail_requires,
    "energy": energy_ca_requires,
    "energy-ca": energy_ca_requires,
    "energy-km": energy_km_requires,
    "fsi": fsi_risk_requires + fsi_nlp_requires,
    "fsi-nlp": fsi_nlp_requires,
    "fsi-risk": fsi_risk_requires,
    "gem": gem_ent_requires + gem_reco_requires,
    "gem-ent": gem_ent_requires,
    "gem-reco": gem_reco_requires, 
    "sc": sc_ro_requires + sc_ip_requires + sc_ecr_requires,
    "sc-ecr": sc_ecr_requires,
    "sc-ip": sc_ip_requires,
    "sc-ro": sc_ro_requires,
    "cdm": cdm_requires,
    "maro": maro_requires,
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
