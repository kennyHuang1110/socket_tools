import logging

def setup_logging():
    logging.basicConfig(level=logging.INFO)
    return logging.getLogger(__name__)

from setuptools import setup, find_packages

setup(
    name="socket_tools",
    version="1.0.0",
    description="A network testing toolkit with fragmentation, tunneling, and spoofing features.",
    author="Your Name",
    packages=find_packages(),
    install_requires=[
        "scapy==2.5.0"
    ],
    entry_points={
        "console_scripts": [
            "socket-tools=socket_tools:main",
        ],
    },
)
