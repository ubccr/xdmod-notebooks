# xdmod-notebooks

This repository contains example Jupyter notebooks demonstrating how to use the
XDMoD Data Analytics Framework via the [`xdmod-data`
package](https://pypi.org/project/xdmod-data/).

This documentation is for **v1.x.y (development branch)**. For documentation of other versions:

- [v1.0.3](https://github.com/ubccr/xdmod-notebooks/tree/v1.0.3?tab=readme-ov-file#xdmod-notebooks)
- [v1.0.2](https://github.com/ubccr/xdmod-notebooks/tree/v1.0.2?tab=readme-ov-file#xdmod-notebooks)
- [v1.0.1](https://github.com/ubccr/xdmod-notebooks/tree/v1.0.1?tab=readme-ov-file#xdmod-notebooks)
- [v1.0.0](https://github.com/ubccr/xdmod-notebooks/tree/v1.0.0?tab=readme-ov-file#xdmod-notebooks)
- [v2.x.y (main development branch)](https://github.com/ubccr/xdmod-notebooks/tree/main?tab=readme-ov-file#xdmod-notebooks)

## Download

The latest version of this `xdmod-notebooks` repository can be downloaded from
the [releases page](https://github.com/ubccr/xdmod-notebooks/releases) — under
"Assets," click one of the "Source code" links.

## Setup

Follow the instructions below to set up your system to run the notebooks in
JupyterLab either through Anaconda or Docker.

### Anaconda

1. Install Anaconda following [these instructions](https://docs.anaconda.com/free/anaconda/install/index.html).
1. Open Anaconda Navigator following [these instructions](https://docs.anaconda.com/free/anaconda/install/verify-install/).
1. Launch JupyterLab (NOT Jupyter Notebook).

### Docker

1. Install Docker following [these instructions](https://docs.docker.com/engine/install/).
1. Run a new Docker container named `xdmod-notebooks` on port `8888` based on
   Jupyter's latest SciPy Docker image by running this command:
    ```
    docker run -p8888:8888 --name xdmod-notebooks jupyter/scipy-notebook:latest
    ```
1. Copy-paste the URL listed on your terminal / command prompt that starts with
   `http://127.0.0.1` into a web browser to take you to JupyterLab.
1. Note: Subsequent runs of the Docker container should use this command
   instead of `docker run`:
    ```
    docker start -i xdmod-notebooks
    ```

## Usage

* Once you have JupyterLab open, you can upload and run the notebooks from your
  copy of the `examples` directory in this repository by clicking the Upload
  button (![Screenshot of upload button](docs/img/jupyter-upload.jpg)). If you
  are not familiar with Jupyter notebooks, the "Help" tab may provide useful
  information.
* The notebooks can be run independently and in any order; however, you may
  find this order to be the most helpful when starting out:
    1. Intro.ipynb
    1. Raw-Data.ipynb
    1. Machine-Learning.ipynb

### R example

An example R Markdown file is available [examples/R](examples/R) directory.

## Feedback / Feature Requests

We welcome your feedback and feature requests for the XDMoD Data Analytics
Framework via email: ccr-xdmod-help@buffalo.edu.

## Support

For support, please see [this page](https://open.xdmod.org/support.html). If
you email for support, please include the following:
* `xdmod-data` version number, obtained by running this code in a Jupyter cell:
    ```
    from xdmod_data import __version__
    print(__version__)
    ```
* Operating system version.
* Anaconda or Docker version.
* JupyterLab version.
* Name of the notebook you are using.
* Version number of the notebook listed at the top and bottom of the notebook.
* A description of the problem you are experiencing.
* Detailed steps to reproduce the problem.

## Contributing

We welcome your contributions of new notebooks or edits to existing notebooks
that can be shared with others to demonstrate use of the XDMoD Data Analytics
Framework. Contributions can be made via GitHub Pull Requests to this
repository.

## License

The notebooks in this repository are released under the GNU Lesser General
Public License ("LGPL") Version 3.0. See the [LICENSE](LICENSE) file for
details.

## References

When referencing the Data Analytics Framework for XDMoD, please cite the
following publication:

> Weeden, A., White, J.P., DeLeon, R.L., Rathsam, R., Simakov, N.A., Saeli, C.,
> and Furlani, T.R. The Data Analytics Framework for XDMoD. _SN COMPUT. SCI._
> 5, 462 (2024). https://doi.org/10.1007/s42979-024-02789-2

When referencing XDMoD, please cite the following publication:

> Jeffrey T. Palmer, Steven M. Gallo, Thomas R. Furlani, Matthew D. Jones,
> Robert L. DeLeon, Joseph P. White, Nikolay Simakov, Abani K. Patra, Jeanette
> Sperhac, Thomas Yearke, Ryan Rathsam, Martins Innus, Cynthia D. Cornelius,
> James C. Browne, William L. Barth, Richard T. Evans, "Open XDMoD: A Tool for
> the Comprehensive Management of High-Performance Computing Resources",
> *Computing in Science & Engineering*, Vol 17, Issue 4, 2015, pp. 52-62.
> DOI:[10.1109/MCSE.2015.68](https://doi.org/10.1109/MCSE.2015.68)
