import setuptools
import re

with open('__init__.py', 'rt', encoding='utf8') as f:
    version = re.search(r'__version__ = \'(.*?)\'', f.read()).group(1)

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="example-pkg-mehdinemo",
    version=version,
    author="mehdinemo",
    author_email="mehdin6990@gmail.com",
    description="A small example package",
    long_description=long_description,
    url="https://github.com/pypa/sampleproject",

    # install_requires=['tensorflow==2.1.0', 'datetime'],
    packages=setuptools.find_packages(),

    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    include_package_data=True,
    zip_safe=False
)
