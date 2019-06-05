# snpit

![GitHub release](https://img.shields.io/github/release/samlipworth/snpit.svg)
![GitHub license](https://img.shields.io/github/license/samlipworth/snpit.svg)

Whole genome SNP based identification of members of the Mycobacterium tuberculosis complex. Based on code originally written by Samuel Lipworth and turned into a package by Philip Fowler.

SNP-IT allows rapid Mycobacterial speciation of VCF or FASTA files aligned to NC000962 (H37rV).

For more information please see the publication:

> Lipworth S, Jajou R, de Neeling A, Bradley P, van der Hoek W, Maphalala G, et al. SNP-IT tool for identifying subspecies and associated lineages of Mycobacterium tuberculosis complex. Emerg Infect Dis. 2019 Mar.
> [DOI:10.3201/eid2503.180894](https://doi.org/10.3201/eid2503.180894)

_Please note we are now using version 2 libraries (slightly smaller than those in the paper). If you notice any problems please let us know._

Please email samuel.lipworth@medsci.ox.ac.uk with any queries.

If you are experience difficulties installing the package, please email for help or try [SNP-IT](https://github.com/samlipworth/SNP-IT) (the original non-packaged version).

## How to install

### From source

First clone the repository on your local machine

```sh
> git clone https://github.com/samlipworth/snpit.git
Cloning into 'snpit'...
```

then enter the directory and install

```sh
> cd snpit
> python setup develop --user
```

The `--user` flag ensures that it is only installed for the user (avoiding the need to know the root/sudo password). To system-wide install simply omit the flag.

### Using conda

**NB**: The bioconda recipe is called [mtb-snp-it](https://anaconda.org/bioconda/mtb-snp-it), with thanks to [@pvanheus](https://github.com/pvanheus). I have not tested yet so please let me know if there are any issues.

Install [Miniconda](https://conda.io/projects/conda/en/latest/user-guide/install/index.html) and setup bioconda channel:

```sh
conda config --add channels defaults
conda config --add channels bioconda
conda config --add channels conda-forge
```

Install SNP-IT

```sh
conda install mtb-snp-it
conda update mtb-snp-it
```

## Usage

The code is Python3 and a `snpit` class is defined. To demonstrate simple usage, a python script that calls the package (`snpit-run.py`) which can be found in `bin/` folder is installed in your `$PATH` during installation. To see what it does, a single example VCF is provided in the `example/` folder.

```sh
> cd example
> ls
example.vcf
```

To run simply

```sh
> snpit-run.py --input example.vcf
example.vcf
     M. tuberculosis        Lineage 2                  97.7 %
```

Note that, as shown in the paper, **sublineages are only available for Lineage 4**, hence no sublineage is reported for this sample. To alter how the results are output, please see the [`bin/snpit-run.py`](bin/snpit-run.py) script.

**Below is an example for bulk usage**:

```sh
ls *.fasta.gz | parallel -j10 snpit-run.py {} > snpit_results.tsv
```
