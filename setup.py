from setuptools import setup, find_packages

setup(
    name="pd-database",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "pandas>=2.0.0"
    ]
)