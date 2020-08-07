#!/bin/bash
set -xeuf -o pipefail

rm -rf venv

python3.6 -m venv venv
source venv/bin/activate
pip install setuptools==40.3.0 setuptools_rust==0.11.0 wheel pip --upgrade

python setup.py bdist_wheel
