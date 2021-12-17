# Estimating PV Output from Solar Irradiance

## `R` Packages required for this project

This project requires:

```
bookdown
boot
knitr
rmarkdown
tidyverse
```

## Reproducing this project with the included components

This project can be reproduced using the included data files,
if you don't want to download and preprocess the data yourself.

Requires: `R`, `R` packages mentioned above

1. Knit both the paper and presentation with `knitr`

## Reproducing this project end-to-end

Requires: 
- `python3`
- `python` `venv` package (optional, may require further system packages)
- `R`
- `R` packages mentioned above

To install the necessary python packages:

1. Make a virtual environment: `python3 -m venv solarenv`
1. Activate the virtual environment: `source solarenv/bin/activate`
1. Install the required `python3` packages: `pip install -r requirements.txt`

To replicate the data download:

1. Get an NREL developer API key
1. Change directory to the data scraping directory: `cd data_scraping`
1. Copy the config template to a private config: `cp config_template.toml config.toml`
1. Fill the private config with your values, including the API key
1. Run the data scraping script: `python3 data_scraping.py`

To replicate data preprocessing:

1. Change directory to the processing directory: `cd data_preprocessing`
1. Run the data processing script: `python3 main.py`

To replicate the paper and presentation:

1. Knit both the paper and presentation with `knitr`.
