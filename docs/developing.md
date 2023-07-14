# Developing instructions

## Clear out output cells
To clear out output cells in a notebook before sharing it or committing it to version control, run the following command, replacing `foo.ipynb` with the name of the notebook file (requires the `jupyter` command, which may be available through anaconda by running `conda activate` first):
```
jupyter nbconvert --ClearOutputPreprocessor.enabled=True --inplace foo.ipynb
```
