from setuptools import setup, find_packages
import os.path

def read(name):
    mydir = os.path.abspath(os.path.dirname(__file__))
    return open(os.path.join(mydir, name)).read()

with open("README.md", "r") as f:
    long_description = f.read()

with open('VERSION', 'r') as f:
    __version__ = f.read().strip()

setup(
    name="mkdocs_puml_file",
    version=__version__,
    description="A MkDocs plugin that allows to embed PlantUML files.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords="mkdocs plantuml publishing documentation uml sequence diagram",
    url="https://github.com/TomMeHo/mkdocs_puml_file",
    author="Thomas Meder",
    license="MIT",
    #python_requires=">=3.10",
    install_requires=["mkdocs"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
    ],
    packages=find_packages(
        exclude=["*.tests", "*.tests.*", "tests.*", "tests", "example"]
    ),
    entry_points={
        "mkdocs.plugins": [ "puml_file = mkdocs_puml_file:PlantUmlFilePlugin", ] },
        #"mkdocs.plugins": [ "puml_file = PlantUmlFilePlugin", ] },
)