#setup.py looks for the constructor __init__.py and install all of them as local packages
import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__= "0.0.0"


REPO_NAME = "Text-Summerizar-Project"
AUTHOR_USER_NAME = "SachinM007"
SRC_REPO = "TextSummarizer"
AUTHOR_EMAIL = "bsachinmiryala@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for NLP app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")

)


