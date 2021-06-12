from setuptools import setup

setup(
    name="ServerBoiUtils",
    version="1.0",
    packages=["serverboi_utils"],
    install_requires=["python-a2s", "requests", "aws_enums", "linode_enums"],
    dependency_links=[
        "git+ssh://git@github.com/Awslring/AWS-Enums-Python.git#egg=aws_enums-0.1",
        "git+ssh://git@github.com/Awslring/Linode-Enums-Python.git#egg=linode_enums-0.1",
    ],
    include_package_data=True,
)