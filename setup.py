from setuptools import setup

setup(
    name="ServerBoiUtils",
    version="1.0",
    packages=["serverboi_utils"],
    install_requires=["python-a2s", "requests", "linode_api4"],
    include_package_data=True,
)