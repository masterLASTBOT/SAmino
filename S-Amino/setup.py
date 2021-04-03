import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="samino",
    version="1.0.7",
    description="A libarry to create Amino bots",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/SirLez",
    author="SirLez",
    author_email="mailto:SirLezDV@gmail.com",
    license="MIT",
    keywords=[
        'capture',
        'captureS'
        'capture-bot',
        'capture-chat',
        'capture-lib',
        'cptr',
        'cptr.co',
        'api',
        'python',
        'python3',
        'python3.x',
        'SirLez',
        'sirlez',
        'Amino',
        'Amino.py',
        'Amino py',
        'samino',
        'samino py'
        'S-Amino',
        'samino',
        'samino',
        'samino-bot',
        'samino-bots',
        'samino-bot',
        'ndc',
        'narvii.apps'
    ],
    include_package_data=True,
    install_requires=[
        'requests',
    ],
    setup_requires=[
        'wheel'
    ],
    packages=find_packages(),
)