from setuptools import setup, find_packages

setup(
        name="pthat",
        version="0.1",
        description="An driver for an 8 channel pressure/temperature sensing hat",
        author="xdylanm",
        url="https://github.com/xdylanm/pthat",
        packages=find_packages(include=['pthat','pthat.*']),
        install_requires=[
            'spilite',
            'spidev',
            'gpiozero',
        ]
)

