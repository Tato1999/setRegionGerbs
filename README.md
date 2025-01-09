# setRegionGerbs

A Python module for downloading region-specific flags (gerbs) from the Flag CDN and saving them to a local directory.

## Installation

To install this module, you can use `pip`:

### Using `pip`:

If you're not using Poetry, you can install the module from PyPI using `pip`:

```bash
pip install setRegionGerbs

Install from source:

If you want to install directly from source, clone the repository and run:

git clone https://github.com/Tato1999/setRegionGerbs.git
cd setRegionGerbs
python3 setup.py install


from setRegionGerbs import setRegionGerbs

# Create an instance of the setRegionGerbs class
gerbs = setRegionGerbs()

# Call the makeDir method to create the necessary directory and start the download process
gerbs.makeDir()

# The flags for the specified regions will be downloaded and saved in the 'gerb_folder' directory.


gerbs.regIso = ['us', 'de', 'fr']  # ISO country codes
gerbs.formatType = 'png'           # Format type for the flags (e.g., 'png', 'jpg')
gerbs.makeDir()                    # Start the process
