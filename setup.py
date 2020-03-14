"""The python wrapper for IQ Option API package setup."""
from setuptools import (setup, find_packages)

setup(
    name="iqoptionapi",
    version="5.2.1",
    packages=find_packages(),
    install_requires=["pylint","requests","websocket-client==0.56"],
    include_package_data = True,
    description="Best IQ Option API for python",
    long_description="Best IQ Option API for python",
    url="https://github.com/evecimar/iqoptionapi",
    author="Evecimar",
    author_email="silva.evecimar@gmail.com",
    zip_safe=False
)
