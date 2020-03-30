from os import system, path
from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="BitSightAPI",
    version="0.3.2",
    author="InfosecSapper",
    author_email="contact@infosecsapper.com",
    description="A Python wrapper for the BitSight API.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/infosecsapper/BitSightAPI",
    license='GPLv3',
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
    python_requires='>=3.7',
)