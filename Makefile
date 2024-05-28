# Annotator
# Quickly annotate images using JSON.
# Github: https://www.github.com/0x4248/Annotator
# Licence: GNU General Public License v3.0
# By: 0x4248

PYTHON = python3
PIP = pip3

ifeq (, $(shell which $(PYTHON)))
$(error "No $(PYTHON) in PATH, please install $(PYTHON) or set the PYTHON variable to the correct path")
endif

all: install_requirements build

build:
	$(PYTHON) setup.py sdist bdist_wheel

install_requirements:
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt
	$(PIP) install --user --upgrade setuptools

clean:
	@echo "RM\tbuild dist annotator.egg-info"
	@rm -rf build dist annotator.egg-info

help:
	@echo "Usage: make [target]"
	@echo "Targets:"
	@echo "  all:              Install requirements and build the package"
	@echo "  build:            Build the package"
	@echo "  install_requirements: Install requirements"
	@echo "  clean:            Remove build, dist and annotator.egg-info directories"

.PHONY: all build install_requirements clean