# Pi Zero Sensors

A Python wrapper package for reading data from sensors attached to a Raspberry Pi Zero.

## Build

### Using the Makefile

This library uses `venv` and a `requirements.txt` file to isolate dependencies. Build requirements are stored in `build_requirements.txt`.

1. Initialise the virtual environment with `make init`. This creates a Python virtual environment in a `.venv/` directory in the project root.
2. Install dependencies with `make install`
3. Run tests with `make test`. Test must be run on a Raspberry Pi with the appropriate sensors attached.
4. Install build dependencies with `make build-install` and build with `make build`, which generates packages in the `dist/` directory.

### Using a custom virtual environment configuration or system Python installation

Configure your Python virtual environment how you like. To use the `Makefile`, edit the `PYTHON_INTERPRETER` variable to point to your virtual environment, and follow the above steps from step 2.

Otherwise, build following steps from this tutorial section: [Generating distribution archives](https://packaging.python.org/en/latest/tutorials/packaging-projects/#generating-distribution-archives) (last accessed 10/10/23).

## Distribution

This package is not currently uploaded to any package indexes. To use, build as above and host in your own repository (see for example [here](https://packaging.python.org/en/latest/guides/hosting-your-own-index/)).
