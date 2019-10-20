import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
  name = 'DataChaser',
  version = '1.0.1',
  author = 'SuulCoder',
  author_email = 'saulcontreras@acm.org',
  description = 'This packages autocompletes the information that is lost in a CSV using AI',
  long_description=long_description,
  long_description_content_type="text/markdown",
  url = 'https://github.com//suulcoder/Chasers-of-the-Lost-Data', # use the URL to the github repo
  packages=setuptools.find_packages(),
  classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
  ],
  python_requires=">=3.4"
)