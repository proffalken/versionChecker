# Symantec versioning check

This code checks a given version and checks that it is above version 1.1.

## Installation instructions

The code relies on the (https://pypi.python.org/pypi/semver)[semver] Python
module, and therefore should be run within a virtualenvironment.

You can do this by installing the `virtualenv` package for your distribution,
and then running `pip install -r requirements.txt` from this directory.

## Running the code

Once the requirements have been installed, you can run the code in one of two
ways:

### Using the default examples

Open up a command prompt and execute `python runChecks.py`, this will output
the results for versions 1.1, 1.2, 1.1.1, and 1.0

### Using the library in other code

Import the checkVersion function, and pass the version you wish to check as
follows:

```python

from checkVersion import checkVersion

my_version = "3.2"
result = checkVersion(my_version)
print(result)

```

## Issues

If you find an issue with this code, please fork the repository and submit a
pull request.

## Copyright

This code is copyright Matthew Macdonald-Wallace/Mockingbird Consulting Ltd.
and is released under the MIT license as documented in the LICENSE file.
