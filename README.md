# xdmod-notebooks
This repository contains example Jupyter notebooks demonstrating how to use the XDMoD Data Analytics Framework via the [`xdmod-data` package](https://github.com/ubccr/xdmod-data).

## Download
This `xdmod-notebooks` repository can be downloaded from this GitHub page by clicking the "Code" button and choosing the method of download.

## Setup
Follow the instructions below to set up your system to run the notebooks in JupyterLab either through Anaconda or Docker.

### Anaconda
1. Install Anaconda following [these instructions](https://docs.anaconda.com/free/anaconda/install/index.html).
1. Open Anaconda Navigator following [these instructions](https://docs.anaconda.com/free/anaconda/install/verify-install/).
1. Launch JupyterLab.
1. Open a Terminal.
1. Install the packages needed to run the example notebooks using the command:
    ```
    python3 -m pip install --upgrade xdmod-data python-dotenv tabulate
    ```

### Docker
1. Install Docker following [these instructions](https://docs.docker.com/engine/install/).
1. Make sure you have downloaded this repository.
1. In a terminal / command prompt, change directories to your downloaded copy of `xdmod-notebooks` and then into the `docker` directory inside there.
1. Build a Docker image called `xdmod-notebooks` from the provided Dockerfile by running the command (make sure to include the dot):
    ```
    docker build -t xdmod-notebooks .
    ```
1. Run a new Docker container named `xdmod-notebooks` on port 8888 by running the command:
    ```
    docker run -p8888:8888 --name xdmod-notebooks xdmod-notebooks
    ```
1. Copy-paste the URL listed on your Terminal into a browser to take you to JupyterLab.

## Usage
1. Once you have JupyterLab open, you can upload and run the notebooks from your copy of this repository by clicking the Upload button (![Screenshot of upload button](docs/img/jupyter-upload.jpg)). If you are not familiar with Jupyter notebooks, the "Help" tab may provide useful information.

## Support
For support, please see [this page](https://open.xdmod.org/support.html). If you email for support, please include the following:
* `xdmod-data` version number, obtained by running the command in JupyterLab:
    ```
    python3 -m pip freeze | grep xdmod-data
    ```
* Operating system version.
* Anaconda or Docker version.
* JupyterLab version.
* Name of the notebook you are using.
* A description of the problem you are experiencing.
* Detailed steps to reproduce the problem.

## Reference
When referencing XDMoD, please cite the following publication:

> Jeffrey T. Palmer, Steven M. Gallo, Thomas R. Furlani, Matthew D. Jones, Robert L. DeLeon, Joseph P. White, Nikolay Simakov, Abani K. Patra, Jeanette Sperhac, Thomas Yearke, Ryan Rathsam, Martins Innus, Cynthia D. Cornelius, James C. Browne, William L. Barth, Richard T. Evans, "Open XDMoD: A Tool for the Comprehensive Management of High-Performance Computing Resources", *Computing in Science & Engineering*, Vol 17, Issue 4, 2015, pp. 52-62. DOI:10.1109/MCSE.2015.68
