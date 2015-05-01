from setuptools import setup, find_packages
setup(
    name = "RecapGreen",
    version = "0.1",
    packages = find_packages(exclude=['*test']), # dependencies
    scripts = ['recapgreen/recapgreen.py'],

    install_requires = ['numpy','geopy','pypng'],

    # metadata for upload to PyPI
    author = "Raz",
    author_email = "no_email@gmail.com",
    description = "Measure level of greenery from Google Maps",
    license = "MIT",
    keywords = "Environment, geocoding",
    url = "http://development.rc.ucl.ac.uk", # project home page, if any
)
