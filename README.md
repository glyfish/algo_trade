## Required Packages

OS X

```
brew install pyenv
brew install pyenv-virtualenv
brew install graphviz
```

Ubuntu

```
curl -L https://raw.githubusercontent.com/pyenv/pyenv-installer/master/bin/pyenv-installer | bash
sudo apt-get install python-dev graphviz libgraphviz-dev pkg-config
```

## Initialize pyenv and pyenv-virtualenv

Add the following to .zshrc
```
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```
Reinitialize shell,

```
source .zshrc
```

## Install python

```
pyenv install 3.6.1
```

## Install Xcode Command Line Tools

If the python build fails because of missing libraries install Xcode command line tools and try again.

```
xcode-select --install
```

## Create Virtual Environment in Project Directory

```
pyenv virtualenv 3.6.1 gly.fish
pyenv local 3.6.1
```

## Activate Virtual Environment

```
pyenv activate gly.fish
```

## Install Packages

```
cat packages.txt | xargs pip install
```
or

```
pip install -r requirements.txt
```

## Use

[atom](https://atom.io) and [hydrogen](https://atom.io/packages/hydrogen) are required to run the notebooks. Start ```atom``` from the command line in the project directory so that the virtual environment is recognized.
