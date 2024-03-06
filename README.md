# rais-doc-code

This repository contains code for Reproducible AI Software (RAIS). `rais-doc-code` aims to extract code from repository documentation
and analyze it for reproducibility.

## Getting Started
Clone the repository:
```bash
git clone https://github.com/vamsi10010/rais-doc-code.git
```
Set up the python environment:
```bash
cd rais-doc-code
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```
Or if you are using conda:
```bash
cd rais-doc-code
conda env create -f rais.yml
conda activate rais
```
Good to go!

## Overview
The repository contains the following files:
- `src/` contains the source code for the project.
- `collection_test.ipynb` and `repo_test.ipynb` demonstrate how to use the code.
