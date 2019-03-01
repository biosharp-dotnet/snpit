#! /usr/bin/env python

import argparse

from snpit import snpit

# programme to report the lineage/subspecies of a TB sample alligned to NC000962
# usage: python SNP-IT.py [guuid] [name of outfile]
# or for lots of samples: cat [list of samples] | parallel -j[no. of threads] python fasta_typer9.py {} {}.out
# Output1: is to file containing absolute and % hits for all subspecies
# Output2: only the top call, is to standard out - redirect to file if you want eg 1>calls.log


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--threshold", default=10, type=int,
                        help="the percentage of snps above which a sample is considered to belong to a lineage")
    parser.add_argument("--input", required=True,
                        help="the path to the VCF or FASTA file to read and classify (either can be bzip2ed/gzipped)")
    parser.add_argument('--version', action='version',
                        version='%(prog)s v1.1')
    options = parser.parse_args()

    # try opening the specified input file
    try:
        input_file = open(options.input, 'r')
    except OSError as e:
        raise OSError(
            "--input {} does not exist!\n{}".format(options.input, e))
    else:
        input_file.close()
        # create an instance (this loads all the lineages)
        tb = snpit(threshold=options.threshold, input_file=options.input)
        if tb.percentage is not None:
            print("%s\t%s\t%s\t%s%.1f %%" % (
                options.input, tb.species, tb.lineage, tb.sublineage, tb.percentage))
        else:
            print("%s\t%s" % (options.input, "none identified"))
