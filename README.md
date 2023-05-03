# PyPackage
An example for creating a deployable Python package.

This shows one way to create a Python package, that can be installed from
a local directory, a local Git repo, or a remote repo. It also
shows how to make the package executable from the command line.

It's very easy, once you know a few tricks.

## What you need

Perhaps you don't need all of these, but they are pretty standard.

1. *pyproject.toml*: contains the package specifications. Add dependent
   package names, and they are magically installed.
1. *LICENSE*
1. *README.md*
1. *\_\_init\_\_.py*: Updates the path so that python can find modules.
1. *\_\_main\_\_.py*: If you want to have a default way to run the package.
1. Source: Your source code, in a subdirectory.

"requests" was specified just as an example dependency in `pyproject.toml`.
You can also specify versionrequirements for the dependencies.

## Directory structure

```sh
TOPDIR/
    | pyproject.toml
    | LICENSE
    | README.md
    | PyPackage/         # (matches the package name)
        | __init__.py
        | __main__.py
        | PyPackage.py   # (matches the package name)
        | source1.py
        | ...
        | sourceN.py
```

## Package installation

- From a local directory:
```sh
pip3 install <path to the local directory>
```

- From a local repository:
```sh
pip3 install git+file://<path to the local repository>
```
Don't get confused when your current changes don't seem to be getting
installed using this method. You need to commit them first!

- From GitHub:
```sh
pip3 install git+https://github.com/<github repo>
```

Just look in your python `lib/site-packages/PyPackage/` directory
if you need to verify what is being installed.

## Running

```sh
python3 -m PyPackage        # Runs PyPackage.py
python3 -m PyPackage.script # Runs script.py
```

## Caveats

- The python paths can get very confused if you are trying to run the installed
  module, but your working directory is where the source code is located. 
  Change to a neutral directory first.
