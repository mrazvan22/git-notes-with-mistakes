from setuptools import setup, find_packages

setup(
    name = "units",
    version = "0.1",
    packages = find_packages(exclude=['*test']),
    scripts = ['scripts/units'],
    package_data={'units': ['units.yaml']},
    include_package_data=True,
    data_files = [('units', ['units/units.yaml'])]
)
