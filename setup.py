from setuptools import setup, find_packages
import codecs
import os.path


def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path), 'r') as fp:
        return fp.read()


def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith('__version__'):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")


def get_requires():
    reqs = []
    for line in open("requirements.txt", "r").readlines():
        reqs.append(line)
    return reqs


setup(
    name="RBbot_inference",
    version=get_version("RBbot_inference/__init__.py"),
    description="Running inference for RBbot",
    url="https://github.com/nabeelre/RBbot-inference",
    author="Nabeel Rehemtulla",
    author_email="nabeelr@u.northwestern.edu",
    license="MIT",
    packages=find_packages(),
    classifiers=[
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Astronomy",
        "Programming Language :: Python :: 3.12",
    ],
    keywords="Astronomy Computer Vision Deep Learning",
    install_requires=get_requires(),
)
