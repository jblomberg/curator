import os
from setuptools import setup

# Utility function to read from file.
def fread(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

def get_version():
    VERSION = fread("VERSION").strip()
    build_number = os.environ.get('BUILD_NUMBER', None)
    if build_number:
        return VERSION + "b{}".format(build_number)
    return VERSION

setup(
    name = "elasticsearch-curator",
    version = "1.0.0-dev",
    author = "Aaron Mildenstein",
    author_email = "aaron@mildensteins.com",
    description = "Tending your time-series indices in Elasticsearch",
    long_description=str(fread('README.md')),
    url = "http://github.com/jblomberg/curator",
    download_url = "https://github.com/jblomberg/curator/tarball/v1.0.0-dev",
    license = "Apache License, Version 2.0",
    install_requires = [
        'elasticsearch>=1.0.0,<2.0.0'
    ],
    keywords = "elasticsearch time-series indexed index-expiry",
    packages = ["curator"],
    include_package_data=True,
    entry_points = {
        "console_scripts" : ["curator = curator.curator:main"]
    },
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: Apache Software License",
    ],
    test_suite = "test_curator.run_tests.run_all",
    tests_require = ["mock", "nose", "coverage", "nosexcover"]
)
