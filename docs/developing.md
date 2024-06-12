# Instructions for developers

## Contributing a Pull Request

1. If updating existing notebooks:
    1. Increment the notebook minor version number and date at the top of the notebook (e.g., 1.0 becomes 1.1).
    1. If applicable, update the version of the XDMoD Data Analytics Framework at the top and bottom of the notebook.
    1. If applicable, increment the copyright year of the notebook (e.g., 2023 becomes 2023–2024 becomes 2023–2025).
    1. Clear out output cells by running the following command, replacing `foo.ipynb` with the name of the notebook file (requires the `jupyter` command, which may be available through anaconda by running `conda activate` first):
        ```
        jupyter nbconvert --ClearOutputPreprocessor.enabled=True --inplace foo.ipynb
        ```
    1. Create a Pull Request.
    1. Update `CHANGELOG.md` in the Pull Request to add an item under `Main development branch` (create that section if it does not already exist) that has the title, number, and URL of the Pull Request.
    1. Once the Pull Request is approved, before merging it, update the release dates at the top of the notebooks you changed.

## Releasing a new version

1. Make a new branch of `xdmod-notebooks` and:
    1. For each notebook, including those in the `R` directory:
        1. Increment the document version at the top to the next major version (e.g., 1.1 becomes 2.0) and the expected release date.
        1. Make sure the XDMoD Data Analytics Framework version number is updated at the top and bottom of the document.
    1. Update `CHANGELOG.md` to change `Main development branch` to, e.g., `v1.0.1 (2024-06-XX)`.
    1. Run all notebooks and make sure they work.
    1. Create a Pull Request for the new version.
    1. Once the Pull Request is approved, before merging it, update the release dates in `CHANGELOG.md` and each of the notebooks.
1. Once the Pull Request is merged, go to [create a new release on GitHub](https://github.com/ubccr/xdmod-notebooks/releases/new) and:
    1. Click `Choose a tag`.
    1. Type in a tag similar to `v1.0.0` and choose `Create new tag`.
    1. Make the release title the same as the tag name (e.g., `v1.0.0`).
    1. Where it says `Describe this release`, paste in the contents of the release's section in `CHANGELOG.md`.
    1. Where it says `Attach binaries`, attach the built distribution that was uploaded to PyPI.
    1. Click `Publish release`.
