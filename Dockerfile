# ubuntu bionic - v1.29
FROM ubuntu:18.04

## Azure Global AI Dev Environment Ubuntu 18.04 ##
LABEL maintainer="Azure Global AI <dciborow@microsoft.com>"

WORKDIR /tmp

# define variables for build
ENV DISTRIBUTION=ubuntu DISTRIBUTION_VERSION=18.04 \
    PY_VER=3.7 PY_VER_NODOT=37 PYPKG_VER=3.7.9-1+bionic \
    CVXOPT_BUILD_GLPK=1 \
    TZ=America/New_York

ARG DEBIAN_FRONTEND=noninteractive

# set env paths
ENV PATH="${PATH}:/root/.local/bin"

# -----------------------------------------------------------------#
#             Install Main Ubuntu Depedancies                      #
# -----------------------------------------------------------------#
RUN sed -i "s://archive\.ubuntu\.com/://azure.archive.ubuntu.com/:" /etc/apt/sources.list \
    && apt-get update \
    && apt-get install -y --no-install-recommends\
        apt-utils curl unzip zip bzip2 xz-utils git wget \
        libtool build-essential clang libssl-dev libffi-dev libbz2-dev zlib1g-dev libgmp-dev \
        libxrender-dev libsm6 libxml2 libxslt-dev libfreetype6-dev libpng-dev pkg-config libhdf5-dev rustc unixodbc-dev \
        libjpeg-dev libc6 jsonlint \
        python-h5py libnetcdf-dev libnetcdff-dev libpq-dev libgeos-dev python-numpy gdal-bin libgdal-dev \
        libblas-dev liblapack-dev libsuitesparse-dev libglpk-dev \        
    && apt install -y \
        software-properties-common \
    && add-apt-repository -y ppa:deadsnakes/ppa \
    && apt install -y --no-install-recommends\
        python3.7 python3.7-dev \
    && add-apt-repository -y ppa:ubuntugis/ppa \
    && apt install -y --no-install-recommends\
        gdal-bin libgdal-dev \
    && rm -rf /var/lib/apt/lists/*

ENV CPLUS_INCLUDE_PATH=/usr/include/gdal C_INCLUDE_PATH=/usr/include/gdal

RUN SC_VER=v0.7.0 \
    && curl -fSsLO https://github.com/koalaman/shellcheck/releases/download/${SC_VER}/shellcheck-${SC_VER}.linux.x86_64.tar.xz \
    && printf "84e06bee3c8b8c25f46906350fb32708f4b661636c04e55bd19cdd1071265112d84906055372149678d37f09a1667019488c62a0561b81fe6a6b45ad4fae4ac0 ./shellcheck-${SC_VER}.linux.x86_64.tar.xz\n" | sha512sum -c \
    && tar --xz -xpf shellcheck-${SC_VER}.linux.x86_64.tar.xz \
    && cp shellcheck-${SC_VER}/shellcheck /usr/local/bin/ \
    && rm -rf shellcheck-${SC_VER}* \
    && shellcheck --version

RUN CMAKE_VER_MAJOR_MINOR=3.15 CMAKE_VER_PATCH_LEVEL=4 \
    && CMAKE_VER="${CMAKE_VER_MAJOR_MINOR}.${CMAKE_VER_PATCH_LEVEL}" \
    && curl -fSsLO https://cmake.org/files/v${CMAKE_VER_MAJOR_MINOR}/cmake-${CMAKE_VER}-Linux-x86_64.tar.gz \
    && printf "7c2b17a9be605f523d71b99cc2e5b55b009d82cf9577efb50d4b23056dee1109 cmake-${CMAKE_VER}-Linux-x86_64.tar.gz\n" | sha256sum -c \
    && tar xzf cmake-${CMAKE_VER}-Linux-x86_64.tar.gz -C /opt \
    && ln -s /opt/cmake-${CMAKE_VER}-Linux-x86_64/bin/cmake /usr/bin/cmake \
    && cmake --version \
    && rm -f cmake-${CMAKE_VER}-Linux-x86_64.tar.gz

# -----------------------------------------------------------------#
# INSTALL JDK 15 General-Availability Release
# -----------------------------------------------------------------#
ENV JAVA_HOME /opt/jdk/jdk-15

RUN wget "https://download.java.net/java/GA/jdk15/779bf45e88a44cbd9ea6621d33e33db1/36/GPL/openjdk-15_linux-x64_bin.tar.gz" \
    && rm -rf /opt/jdk \
    && mkdir /opt/jdk \
    && tar -zxf openjdk-15_linux-x64_bin.tar.gz -C /opt/jdk \
    && update-alternatives --install /usr/bin/java java /opt/jdk/jdk-15/bin/java 100 \
    && update-alternatives --install /usr/bin/javac javac /opt/jdk/jdk-15/bin/javac 100 \
    && update-alternatives --install /usr/bin/jar jar /opt/jdk/jdk-15/bin/jar 100 \
    && rm -f openjdk-15_linux-x64_bin.tar.gz

# -----------------------------------------------------------------#
# Prepare Python Environment
# -----------------------------------------------------------------#
COPY virtualenv.txt /tmp/

RUN curl -fSsLO https://bootstrap.pypa.io/get-pip.py \
    && /usr/bin/python${PY_VER} get-pip.py 'pip==21.1.3' \
    && pip3 install --require-hashes --upgrade -r /tmp/virtualenv.txt

RUN mkdir -p /source/packages/pywheel \
    && python3.7 -m pip install \
        cython==0.29.23 setuptools-rust flit \
    && python3.7 -m pip install \
        numpy \
    && virtualenv --extra-search-dir "/source/packages/pywheel" --no-download --python="python3.7" "/devopsVirtualEnv"

# Python Packages which must be downloaded as Binary (the default is src)
ENV BINARY="amply,azureml-automl-core,azureml-contrib-reinforcementlearning,azureml-contrib-automl-pipeline-steps,azureml-core,azureml-dataprep,azureml-dataprep-native,azureml-dataprep-rslex,azureml-dataset-runtime,azureml-defaults,azureml-model-management-sdk,azureml-pipeline,azureml-pipeline-core,azureml-pipeline-steps,azureml-telemetry,azureml-train,azureml-train-automl-client,azureml-train-core,azureml-train-restclients-hyperdrive,backports.entry-points-selectable,black,blis,colorama,commondatamodel-objectmodel,cornac,coverage,cryptography,dm-tree,dotnetcore2,fairlearn,fiona,flatbuffers,flit,flit-core,h5py,importlib-metadata,iniconfig,interpret,interpret-core,ipykernel,ipyleaflet,isort,jsonpickle,jsonschema,jupyterlab-widgets,keras-nightly,lazy-object-proxy,lightgbm,llvmlite,opencensus-context,opencensus-ext-azure,opencv-python,opencv-python-headless,ortools,pastel,pkgconfig,pluggy,py-spy,pyarrow,pydocumentdb,pykrige,pylint,pyproj,pytest,pytest-runner,python-dateutil,pymanopt,pymaro,ray,scikit-learn,scipy,sentencepiece,statsmodels,spacy,tenacity,tensorboard,tensorflow-hub,tensorboard-plugin-wit,tensorflow-estimator,tensorflow,tensorboard-data-server,testpath,tokenizers,torch,torchvision,thinc,tqdm,virtualenv,xarray,zipp"

# -----------------------------------------------------------------#
# Download and Install PIP Tools
# -----------------------------------------------------------------#
COPY piptools.txt /tmp/requirements/

RUN python3.7 -m pip download \
        -d "/source/packages/pywheel" \
        -r "/tmp/requirements/piptools.txt" \
    && /devopsVirtualEnv/bin/python -m pip install \
        --find-links "/source/packages/pywheel" \
        --upgrade \
        pip setuptools cython flit pytoml\
    && /devopsVirtualEnv/bin/python -m pip install \
        --find-links "/source/packages/pywheel" \
        --upgrade \
        -r "/tmp/requirements/piptools.txt"

# -----------------------------------------------------------------#
# Download and Install Test Dependancies
# -----------------------------------------------------------------#
COPY test/requirements.txt /tmp/requirements/test/

RUN python3.7 -m pip download \
        -d "/source/packages/pywheel" \
        -r "/tmp/requirements/test/requirements.txt" \
    && /devopsVirtualEnv/bin/python -m pip install \
        --use-deprecated=legacy-resolver \
        --find-links "/source/packages/pywheel" \
        --upgrade \
        -r "/tmp/requirements/test/requirements.txt"

# -----------------------------------------------------------------#
# Download and Install Runtime Dependancies
# -----------------------------------------------------------------#
COPY requirements.txt /tmp/requirements/

RUN python3.7 -m pip download \
        -d "/source/packages/pywheel" \
        -r "/tmp/requirements/requirements.txt" \
    && /devopsVirtualEnv/bin/python -m pip install \
        --find-links "/source/packages/pywheel" \
        --upgrade \
        -r "/tmp/requirements/requirements.txt"
