---
title: Download
subtitle: FEniCSx fenicsxversion
permalink: /download/
---

## Getting started

The latest stable release of FEniCSx is version {{ site.fenicsxversion }},
which was released in {{ site.fenicsxversiondate }}. The easiest way to start using FEniCSx
on MacOS and other systems is to install it using [conda](https://conda.io):

```shell
conda create -n fenicsx-env
conda activate fenicsx-env
conda install -c conda-forge fenics-dolfinx mpich pyvista
```

The easiest way to install FEniCSx on Debian or Ubuntu Linux
is via apt:

```shell
sudo add-apt-repository ppa:fenics-packages/fenics
sudo apt update
sudo apt install fenicsx
```

## Other installation options

The source code of all the components of FEniCSx can be found [on GitHub](https://github.com/FEniCS/):

- [<i class="fa-brands fa-github"></i> UFL](https://github.com/FEniCS/ufl)
- [<i class="fa-brands fa-github"></i> Basix](https://github.com/FEniCS/basix)
- [<i class="fa-brands fa-github"></i> FFCx](https://github.com/FEniCS/ffcx)
- [<i class="fa-brands fa-github"></i> DOLFINx](https://github.com/FEniCS/dolfinx)

Detailed instructions for installing FEniCSx from source, or using some binary distributions can be found
[in the installation page of the DOLFINx docs](https://github.com/FEniCS/dolfinx#installation).

## FEniCSx vs legacy FEniCS

FEniCSx is the latest iteration of FEniCS, and boasts a number of 
major improvements over the legacy library,
including support for a wide range of cell types and elements, memory
parallelisation, and complex number support. FEniCSx is comprised of
the libraries UFL, Basix, FFCx and DOLFINx. The latest version of
FEniCSx ({{ site.fenicsxversion }}) was released in
{{ site.fenicsxversiondate }}.
We recommend that new users use the latest release of FEniCSx.


Updates are now very rarely made to the legacy FEniCS library. We recommend that users consider
using FEniCSx instead of the legacy library. Lecacy FEniCS is comprised
of the libraries UFL legacy, FIAT, FFC and DOLFIN. The latest version of legacy
FEniCS ({{ site.fenicsversion }}) was released in
{{ site.fenicsversiondate }}.
Instructions for installing the legacy FEniCS (version {{
site.fenicsversion }}) can be found [here](archive.md).

## Complex number support

FEniCSx introduces complex number support.

On Debian/Ubuntu Linux this is provided via the python3-dolfinx-complex package:

```shell
sudo apt install python3-dolfinx-complex
```

Debian/Ubuntu packages manage dolfinx builds via the version of PETSc they are built against.
The Debian/Ubuntu standard installation uses the real number build. To access other
builds, set the environment variable PETSC_DIR to point at the required PETSc version
located under /usr/lib/petscdir. Likewise SLEPc support can be managed via SLEPC_DIR
(see /usr/lib/slepcdir).

So to access complex number support in dolfinx on Debian/Ubuntu, run scripts with:

```shell
PETSC_DIR=/usr/lib/petscdir/petsc-complex python3 demo_dolfinx.py
```

or, with SLEPc:

```shell
PETSC_DIR=/usr/lib/petscdir/petsc-complex SLEPC_DIR=/usr/lib/slepcdir/slepc-complex python3 demo_dolfinx.py
```
