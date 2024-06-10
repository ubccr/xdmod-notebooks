# Developing instructions

## Clear out output cells
To clear out output cells in a notebook before sharing it or committing it to version control, run the following command, replacing `foo.ipynb` with the name of the notebook file (requires the `jupyter` command, which may be available through anaconda by running `conda activate` first):
```
jupyter nbconvert --ClearOutputPreprocessor.enabled=True --inplace foo.ipynb
```
## Preparing a new version for release
1. Make sure the version number is updated in each of the notebooks including in the `R` directory.
1. Update `CHANGELOG.md` to change "Main development branch" to, e.g., `v1.0.1 (2024-06-XX)`.
1. Run all notebooks and make sure they work.
1. Create a Pull Request for the new version.
