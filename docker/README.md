# Instructions

This directory contains a configuration file to build a
docker image containing Jupyter notebooks and the python-based XDMoD
interface library.

Build the docker image as follows:
```sh
docker build -t xdmodnotebooks .
```

Setup authentication by creating a file called `secrets` and add the username and password
for your XDMoD local login. **SSO logins are not supported yet**. Since this file
will contain your password, make sure the file
permissions are set to owner read/write only:

```sh
touch secrets
chmod 600 secrets
```

The file contents should contain the following (with the text in brackets
replace appropriately)::
```
XDMOD_USER=[your username]
XDMOD_PASS=[your password]
```

Run the container as follows:
```
docker run -p8888:8888 --env-file=secrets xdmodnotebooks
```

it will then print out the web url to go to in the browser.

** No notebooks are loaded into this image ** You'll have to import the ones you want to use.
