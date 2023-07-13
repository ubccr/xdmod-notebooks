FROM jupyter/scipy-notebook:latest

RUN python3 -m pip install xdmod-data python-dotenv tabulate
