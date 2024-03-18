# Developing instructions

## Clear out output cells
To clear out output cells in a notebook before sharing it or committing it to version control, run the following command, replacing `foo.ipynb` with the name of the notebook file (requires the `jupyter` command, which may be available through anaconda by running `conda activate` first):
```
jupyter nbconvert --ClearOutputPreprocessor.enabled=True --inplace foo.ipynb
```

## Conda Packages for R and Python

Using https://github.com/jupyter/docker-stacks images:
* base-notebook
* minimal-notebook
* scipy-notebook
* r-tidyverse

```bash
conda create -n xdmod-notebooks -y python=3.11 r=4.3
conda activate xdmod-notebooks
# base-notebook
conda install -y 'jupyterlab' \
    'notebook' \
    'jupyterhub' \
    'nbclassic'
# scipy-notebook
conda install -y  'altair' \
    'beautifulsoup4' \
    'bokeh' \
    'bottleneck' \
    'cloudpickle' \
    'conda-forge::blas=*=openblas' \
    'cython' \
    'dask' \
    'dill' \
    'h5py' \
    'ipympl'\
    'ipywidgets' \
    'jupyterlab-git' \
    'matplotlib-base' \
    'numba' \
    'numexpr' \
    'openpyxl' \
    'pandas' \
    'patsy' \
    'protobuf' \
    'pytables' \
    'scikit-image' \
    'scikit-learn' \
    'scipy' \
    'seaborn' \
    'sqlalchemy' \
    'statsmodels' \
    'sympy' \
    'widgetsnbextension'\
    'xlrd'
# r-notebook
conda install -y     'r-base' \
    'r-caret' \
    'r-crayon' \
    'r-devtools' \
    'r-e1071' \
    'r-forecast' \
    'r-hexbin' \
    'r-htmltools' \
    'r-htmlwidgets' \
    'r-irkernel' \
    'r-nycflights13' \
    'r-randomforest' \
    'r-rcurl' \
    'r-rmarkdown' \
    'r-rodbc' \
    'r-rsqlite' \
    'r-shiny' \
    'r-tidymodels' \
    'r-tidyverse' \
    'unixodbc'
# Other
conda install -y 'pymysql' \
    'r-plotly' 'r-repr' 'r-irdisplay' 'r-pbdzmq' 'r-reticulate' 'r-cowplot' 'r-rjson' 'r-dotenv' 'requests'
    
# qgrid2 extra installation
#conda install -y 'qgrid'
#jupyter labextension install @jupyter-widgets/jupyterlab-manager
#jupyter labextension install qgrid2

# Install rstudio server
 wget -q "https://download2.rstudio.org/server/jammy/amd64/rstudio-server-2023.12.1-402-amd64.deb" \
  && dpkg -i rstudio-server-*-amd64.deb \
  && rm rstudio-server-*-amd64.deb
#

echo "rsession-which-r=$(which R)" | sudo tee -a /etc/rstudio/rserver.conf

 
sudo /usr/lib/rstudio-server/bin/rserver

```
