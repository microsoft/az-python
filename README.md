# AI Python by Microsoft

This is a library of Python packages scanned using various open source and internal tools to provide up-to-date, and secury dependencies.  

## Installation
Currently Python3.7 is supported.

### Ubuntu 18.04
The aiubuntu library is provided to simplify installation of required Ubuntu dependancies.

shell

add-apt-repository -y ppa:deadsnakes/ppa \
&& apt-get update \
&& apt-get install -y python3.7 python3.7-dev

curl -fSsLO https://bootstrap.pypa.io/get-pip.py \
&& /usr/bin/python3.7 get-pip.py 'pip==20.3.3'

add-apt-repository -y ppa:dciborow/ppa \
&& apt-get update \
&& apt-get install -y aiubuntu

# For Core Libaries (this will install nearly everything) 
python3.7 -m pip install ai-python[core]

# For Libraries needed for testing
python3.7 -m pip install ai-python[tests]

# For Libraries needed for a single package
python3.7 -m pip install ai-python[retail]

## Contributing

This project welcomes contributions and suggestions.  Most contributions require you to agree to a
Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us
the rights to use your contribution. For details, visit https://cla.opensource.microsoft.com.

When you submit a pull request, a CLA bot will automatically determine whether you need to provide
a CLA and decorate the PR appropriately (e.g., status check, comment). Simply follow the instructions
provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

## Trademarks

This project may contain trademarks or logos for projects, products, or services. Authorized use of Microsoft 
trademarks or logos is subject to and must follow 
[Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
Use of Microsoft trademarks or logos in modified versions of this project must not cause confusion or imply Microsoft sponsorship.
Any use of third-party trademarks or logos are subject to those third-party's policies.
