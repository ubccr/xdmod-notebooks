# xdmod-notebooks R example
This directory contains an example R Markdown file demonstrating how to use the
XDMoD Data Analytics Framework via the
[`xdmod-data`](https://pypi.org/project/xdmod-data/) package.

For examples using Python in Jupyter instead, see the main [README](../).

## Setup
Follow the instructions below to set up your system to run the R Markdown file
in RStudio Desktop using an Anaconda environment.

Install R and RStudio Desktop from
[here](https://posit.co/download/rstudio-desktop/).

Install the following R libraries in RStudio Desktop (`Tools` >
`Install Packages...`):

* `plotly`
* `rmarkdown`
* `reticulate`
* `tidyverse`

Install Anaconda following [these
instructions](https://docs.anaconda.com/free/anaconda/install/index.html).

Next an Anaconda environment for `xdmod-notebooks` should be created and the
latest version of the `xdmod-data` package should be installed. Command line
instructions for doing so are below. Note that the last two commands can also
be run to apply any minor or patch upgrades to the package.

```
conda activate
conda create -y -n xdmod-notebooks python
conda activate xdmod-notebooks
python3 -m pip install --upgrade 'xdmod-data>=1.0.0,<2.0.0'
```

### Obtain and store an API token
Follow [these
instructions](https://github.com/ubccr/xdmod-data#api-token-access) to obtain
an API token.

Create an environment file at `~/xdmod-data.env` with the following contents,
replacing `<TOKEN>` with your token.
```
XDMOD_API_TOKEN=<TOKEN>
```

## Usage
In RStudio Desktop, open and run the R Markdown file (`Intro.Rmd`). If you are
not familiar with running R Markdown files, the "Help" tab may provide useful
information.

## Feedback / Feature Requests, Support, Contributing, License, and Reference
See the main [README](../).
