# Set up a Jupyter Notebook

VS Code

## Setting up your environment
https://code.visualstudio.com/docs/python/jupyter-support#_setting-up-your-environment

Open a new terminal using `New Terminal`.
Conda way, too many packages that we dont need:
```
# conda create -n yourenvname python=x.x anaconda
conda create -n udacity_wine python=3.7 anaconda

# source activate yourenvname
source activate udacity_wine

# conda remove -n yourenvname -all
conda remove -n udacity_wine -all
```


Python3 way:
```
python3 -m venv ~/yourenvname
```
## Create Python Notebook

`<STRG + SHIFT + P>` or `<CMD + SHIFT + P>` and start typing "jupyter" until you find "Jupyter: Create New Blank Notebook"