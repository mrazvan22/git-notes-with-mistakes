from setuptools import setup, find_packages

setup(
    name = "units",
    version = "0.1",
    packages = find_packages(exclude=['*test']),
    scripts = ['units/units.py', 'units/units.yaml']
)