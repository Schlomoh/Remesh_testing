# PyMeshLab remesh testing

### Structure

#### Files

There's one `Main.py` file which is extended with modules which apply one filter onto one file.

This program may be extended to run trough multiple selected files making batch processing possible.

#### Parameters

Currently there's only single file processing. The way to parse arguments to the main `MeshLab` class is not optimal since it only takes the `args` object which is created by the argsparse module. Wasnt too important tho.

### Usage

#### CLI

##### This script is currently only tested on a windows x64 machine

###### Before first execution run:
```
pip install -r requirements.txt
```
This installs all dependencies needed to run the script successfully.

###### For CLI help run:
```
python Main.py -h
```
The `Main.py` requires two arguments:  
- `input_file`
- `action`  
``` 
python Main.py 'input_file' 'action' [-d decimation_percentage] [-o output_dir] [-h]
```

When setting `action` to `'remesh'`, the default percentage for remesh simplification is **50%**.  

**note:** *when setting the -d parameter to 40 the output .obj will be made up of only 40% of the original amount of vertices*

###### For remeshing .obj by certain percentage run:
```
python Main.py input/objects.obj remesh 30 
```

