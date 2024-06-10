# Instructions for developers

## Clear out output cells
To clear out output cells in a notebook before sharing it or committing it to version control, run the following command, replacing `foo.ipynb` with the name of the notebook file (requires the `jupyter` command, which may be available through anaconda by running `conda activate` first):
```
jupyter nbconvert --ClearOutputPreprocessor.enabled=True --inplace foo.ipynb
```
## Releasing a new version
1. Make a new branch of `xdmod-notebooks` and:
    1. Make sure the version number is updated in each of the notebooks including in the `R` directory.
    1. Update `CHANGELOG.md` to change "Main development branch" to, e.g., `v1.0.1 (2024-06-XX)`.
    1. Run all notebooks and make sure they work.
    1. Create a Pull Request for the new version.

1. Once the Pull Request is merged, go to [create a new release on GitHub](https://github.com/ubccr/xdmod-notebooks/releases/new) and:
    1. Click `Choose a tag`.
    1. Type in a tag similar to `v1.0.0` and choose `Create new tag`.
    1. Make the release title the same as the tag name.
    1. Where it says `Describe this release` paste in the contents of `CHANGELOG.md`.
    1. Where it says `Attach binaries` attach the built distribution that was uploaded to PyPI.
    1. Click `Publish release`.
