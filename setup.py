from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='snpit',
    version='1.0.0',
    author='Samuel Lipworth',
    url='https://github.com/samlipworth/snpit',
    email='samuel.lipworth@medsci.ox.ac.uk',
    packages=['snpit'],
    install_requires=[
        "PyVCF >= 0.6.8",
        "biopython >= 1.70"
    ],
    scripts=["bin/snpit-run.py"],
    license='MIT',
    long_description=long_description,
    long_description_content_type="text/markdown",
)
