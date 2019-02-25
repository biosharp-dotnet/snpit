# snpit

Whole genome SNP based identification of members of the Mycobacterium tuberculosis complex. Based on code originally written by Samuel Lipworth and turned into a package by Philip Fowler.

SNP-IT allows rapid Mycobacterial speciation of VCF or FASTA files aligned to NC000962 (H37rV).

For more information please see the publication;

Lipworth S, Jajou R, de Neeling A, Bradley P, van der Hoek W, Maphalala G, et al. SNP-IT tool for identifying subspecies and associated lineages of Mycobacterium tuberculosis complex. Emerg Infect Dis. 2019 Mar. 
https://doi.org/10.3201/eid2503.180894

Please note we are now using version 2 libraries (slightly smaller than those in the paper). If you notice any problems please let us know.

Please email samuel.lipworth@medsci.ox.ac.uk with any queries.

If you are experience difficulties installing the package, please email for help or try https://github.com/samlipworth/SNP-IT (the original non-packaged version).

## How to install

### Conda

With an activated Bioconda channel:
```
conda config --add channels defaults
conda config --add channels bioconda
conda config --add channels conda-forge
```

Install SNP-IT (nb the bioconda recipe is called mtb-snp-it, with thanks to Peter van Heusden)
```
conda install mtb-snp-it
```
### From source

First clone the repository on your local machine

```   
> git clone https://github.com/philipwfowler/snpit.git
Cloning into 'snpit'...
remote: Counting objects: 140, done.
remote: Compressing objects: 100% (10/10), done.
remote: Total 140 (delta 7), reused 13 (delta 6), pack-reused 122
Receiving objects: 100% (140/140), 2.95 MiB | 3.58 MiB/s, done.
Resolving deltas: 100% (58/58), done.
```   
then enter the directory and install
```
> cd snpit
> python setup develop --user
```
The `--user` flag ensures that it is only installed for the user (avoiding the need to know the root/sudo password). To system-wide install simply omit the flag.

## Dependencies

The code requires the BioPython, Gzip and PyVCF Python packages. The above installation process will detect if they already installed in the local machine, and if not, download and install them.

## Usage

The code is Python3 and a `snpit` class is defined. To demonstrate simple usage, a python script that calls the package (`snpit-run.py`) which can be found in `bin/` folder is installed in your `$PATH` during installation. To see what it does, a single example VCF is provided in the `example/` folder

```
> cd example
> ls
example.vcf
```

To run simply
```
> snpit-run.py --input example.vcf 
example.vcf
     M. tuberculosis        Lineage 2                  97.7 %
```
Note that, as shown in the paper, sublineages are only available for Lineage 4, hence no sublineage is reported for this sample. To alter how the results are output, please see the `bin/snpit-run.py` script.

Or for bulk usage eg:

```
ls *.fasta.gz | parallel -j10 snpit-run.py {} > snpit_results.tsv
```

