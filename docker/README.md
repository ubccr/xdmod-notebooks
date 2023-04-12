# Instructions

This directory contains a configuration file to build a
Docker image containing Jupyter notebooks and the Python-based XDMoD
interface library.

Build the docker image as follows:
```sh
docker build -t xdmod-notebooks .
```

Run the container as follows:
```
docker run -p8888:8888 --name xdmod-notebooks xdmod-notebooks
```

It will print out the web URL to go to in a browser.

**No notebooks are loaded into this image.** You'll have to import the ones you
want to use.
