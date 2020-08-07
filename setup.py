import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sevdeskapi",
    version="0.1.0",
    author="Stefan Eiermann, Sachs Media",
    author_email="support@sachs-media.com",
    description="Provides a Python (object-based) API for SevDesk",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Sachs-Media/sevdeskapi",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Office/Business",
        "Topic :: Utilities",
        "Topic :: Software Development :: Libraries"        
    ],
    python_requires='>=3.6',
)
