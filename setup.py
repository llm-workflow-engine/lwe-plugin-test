from setuptools import find_packages, setup
import re
from os import path

FILE_DIR = path.dirname(path.abspath(path.realpath(__file__)))

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open('requirements.txt') as f:
    install_requirement = f.readlines()

with open(path.join(FILE_DIR, 'lwe_plugin_test', 'version.py')) as f:
    version = re.match(r'^__version__ = "([\w\.]+)"$', f.read().strip())[1]

setup(
    name="lwe-plugin-test-2",
    version=version,
    author="Chad Phillips",
    author_email="chad@apartmentlines.com",
    description="A test plugin for ChatGPT Wrapper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mmabrouk/chatgpt-wrapper",
    packages=find_packages(),
    install_requires=install_requirement,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    entry_points={
        "lwe_plugins": [
            "lwe_plugin_test = lwe_plugin_test.plugin:Test"
        ]
    },
)
