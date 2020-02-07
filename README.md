# ccxstuff
Some scripts that is usable when running CalculiX and salome

## intended work flow

- Mesh in salome. I have only tried the Netgen-1-2-3 mesher... 
- Export the mesh as unv.
- Convert to inp-file

        unv2ccx Mesh.unv

- Strip of all non 3d meshes (if preferred)

        only3d Mesh.inp mesh3d.inp

- make jobfile.inp
- run simulation
- extract the nodes, nodesets and results into csv-files

        nodExtract mesh3d.inp
        resultExtract jobfile.frd

Now you easily can import into python (or other) for easy processing
ald plotting

### unv2ccx

A fantastic tool witten by Ihor Mirzov. Thanks Ihor!

Note! unv2ccx is a GPL-v3 licensed code. The source code can be found at:


    https://github.com/imirzov/unv2ccx.git


unv2ccx converts unv-files to inp-files for calculix.

### only3d

Removes 1D and 2D elements from the input file. Netgen uses these
when constructing the solid mesh.



### resultExtract

Extracts the results in the frd-file to csv-files. Convenient when
post-processing in python.

### nodExtract

Writes the node info and nodsets to csv-files

