[![ORCID: Monks](https://img.shields.io/badge/Tom_Monks_ORCID-0000--0003--2631--4481-brightgreen)](https://orcid.org/0000-0003-2631-4481)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# A tutorial on time series (temporal) train-test split

🎓 This tutorial aims to support beginners to forecasting learn how to perform a basic temporal train test split of a time series.  By following the tutorial you will build:

* ✅ Practical experience of how to perform a basic train test split of a univariate time series;
* ✅ Understand why you might consider a more advanced train-validation-test split;
* ✅ Hands on experience of using both strategies to evaluate simple ARIMA models.
* ✅ Understand the limitations of basic train-test split strategies.
* 🎁 **Bonus**: Gained expertise in generating and plotting ARIMA prediction intervals.

## License

The materials have been made available under an [MIT license](LICENCE).  The materials are as-is with no liability for the author. Please provide credit if you reuse the code in your own work.

## Installation instructions

### Installing dependencies

All dependencies can be found in [`binder/environment.yml`]() and are pulled from conda-forge.  To run the code locally, we recommend installing [miniforge](https://github.com/conda-forge/miniforge);

> miniforge is Free and Open Source Software (FOSS) alternative to Anaconda and miniconda that uses conda-forge as the default channel for packages. It installs both conda and mamba (a drop in replacement for conda) package managers.  We recommend mamba for faster resolving of dependencies and installation of packages. 

navigating your terminal (or cmd prompt) to the directory containing the repo and issuing the following command:

```bash
mamba env create -f binder/environment.yml
```

Activate the mamba environment using the following command:

```bash
mamba activate ts
```

Run Jupyter-lab

```bash
jupyter-lab
```

## Repo overview

```
.
├── binder
│   └── environment.yml
├── CHANGELOG.md
├── CITATION.cff
├── LICENSE
├── ts_plotting.py
├── 01_ts_train_test_split.ipynb
└── README.md
```

* `binder/environment.yml` - contains the conda environment if you wish to work the models.
* `01_ts_train_test_split.ipynb` - A tutorial notebook describing strategies for time series train test split
* `ts_plotting.ipynb` - a supporting module that contains plotly and other utility code.
* `CHANGES.md` - changelog with record of notable changes to project between versions.
* `CITATION.cff` - citation information for the package.
* `LICENSE` - details of the MIT permissive license of this work.
