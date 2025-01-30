# Instructions for developers

## Contributing a Pull Request

1. If updating existing notebooks:
    1. At the top of the notebook:
        1. Increment the notebook minor version number (e.g., 1.0 becomes 1.1)
           and date.
        1. If applicable, update the minimum and maximum compatible versions of
           the XDMoD Data Analytics Framework.
        1. If applicable, increment the copyright year (e.g., 2023 becomes
           2023–2024 becomes 2023–2025).
    1. Clear out output cells by running the following command, replacing
       `foo.ipynb` with the name of the notebook file (requires the `jupyter`
       command, which may be available through anaconda by running `conda
       activate` first):
        ```
        jupyter nbconvert --ClearOutputPreprocessor.enabled=True --inplace foo.ipynb
        ```
    1. Create a Pull Request.
    1. Update `CHANGELOG.md` in the Pull Request to add an item under `Main
       development branch` (create that section if it does not already exist)
       that has the title, number, and URL of the Pull Request.
    1. Once the Pull Request is approved, before merging it, update the release
       dates at the top of the notebooks you changed.

## Releasing a new version

1. Make a new branch of `xdmod-notebooks` and:
    1. In `README.md`:
        1. Under the main heading,
            1. In the sentence that begins, `This documentation is for ...`,
               replace the version number in bold, e.g.:
                ```
                This documentation is for **v1.0.2**.
                ```
            1. Add the following item to the list, replacing `1` with the major
               version number of the new release. The development branches
               should be listed in order of major version, ascending (`1.x.y`,
               `2.x.y`, etc.):
                ```
                - [v1.x.y (development branch)](https://github.com/ubccr/xdmod-notebooks/tree/v1.x.y?tab=readme-ov-file#xdmod-notebooks)
                ```
    1. For each notebook, including those in the `R` directory, if any changes
       were made to the notebook since the last version, increment the document
       version at the top to the next major version (e.g., 1.1 becomes 2.0) and
       the expected release date.
    1. Update `CHANGELOG.md` to:
        1. Change the `development branch` to, e.g., `v1.0.1 (2024-06-XX)`.
        1. Add a summary of the changes in the version.
    1. Run all notebooks and make sure they work.
    1. Create a Pull Request for the new version.
    1. Once the Pull Request is approved, before merging it, update the release
       dates in `CHANGELOG.md` and each of the notebooks.
1. Once the Pull Request is merged, go to
   [create a new release on GitHub](https://github.com/ubccr/xdmod-notebooks/releases/new)
   and:
    1. Click `Choose a tag`.
    1. Type in a tag similar to `v1.0.0` and choose `Create new tag`.
    1. Choose the correct target based on the major version you are developing.
    1. Make the release title the same as the tag name (e.g., `v1.0.0`).
    1. Where it says `Describe this release`, paste in the contents of the
       release's section in `CHANGELOG.md`. Note that single newlines are
       interpreted as line breaks, so you may need to reformat the description
       to break the lines where you want them to break. Use the `Preview` to
       make sure it looks right.
    1. Click `Publish release`.
    1. Go to the [GitHub milestones](https://github.com/ubccr/xdmod-notebooks/milestones)
       and close the milestone for the version.

## After release

1. For each major version branch, in a Pull Request,
    1. In `CHANGELOG.md`:
        1. Add a section at the top called `v1.x.y (development branch)`,
           replacing `1` with the major version under development (if it is
           also the main development branch, replace `development branch` with
           `main development branch`).
        1. Add the entry for the version that was just released, if it isn't
           already there.
    1. In `README.md`:
        1. Under the main heading, in the sentence that begins,
           `This documentation is for ...`, replace the version number in bold,
           e.g.:
            ```
            This documentation is for **v1.x.y (development branch)**.
            ```
        1. Add an item to the top of the bulleted list for
           the new version, making sure to replace the version number in
           the link text and in the URL.
        1. Remove the item from the bulleted list for the `v1.x.y (development
           branch)` (where `1` is the major version number).
    1. Get the Pull Request approved and merged.
1. Go to the [GitHub milestones](https://github.com/ubccr/xdmod-notebooks/milestones)
   and add a milestone for the version under development.
