from setuptools import setup, find_packages

setup(
    name="scp-sdk",
    version="1.0.0",
    description="Safe Context Protocol SDK for policy enforcement in AI and multi-agent systems",
    packages=find_packages(),
    python_requires=">=3.7",
    install_requires=[
        "pyyaml>=5.3.1"  # for YAML config parsing
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
