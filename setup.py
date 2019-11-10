import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="BitSightAPI",
    version="0.2.0",
    author="InfosecSapper",
    author_email="contact@infosecsapper.com",
    description="A Python wrapper for the BitSight API.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/infosecsapper/BitSightAPI",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GPL-3.0",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)