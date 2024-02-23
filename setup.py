from setuptools import setup, find_packages

# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="pyfortianalyzer",
    version="2.0.0",
    description="Python API client library for Fortinet's FortiAnalyzer.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="Apache2",
    author="Rasmus Thing",
    author_email="rasmus.thing@bestseller.com",
    url="https://github.com/BESTSELLER/pyfortianalyzer",
    python_requires=">=3.8, <4",
    install_requires=[
        "requests>=2.20.0,<3.0"
    ],
    zip_safe=False,
    keywords=[
        "fortinet",
        "fortianalyzer"
    ],
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12"
    ]
)