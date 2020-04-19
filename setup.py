from typing import IO, Sequence
from setuptools import setup as __compose_package, find_packages as __find_packages
from scooter import __author__, __email__, __version__, __package_name__


def __description() -> str:
    """Returns project description."""
    with open("README.md", "r") as readme:  # type: IO
        return readme.read()


def __requirements() -> Sequence[str]:
    """Returns requirements sequence."""
    with open("requirements.txt", "r") as requirements:  # type: IO
        return tuple(map(str.strip, requirements.readlines()))


if __name__ == "__main__":
    __compose_package(
        name=__package_name__,
        version=__version__,
        author=__author__,
        author_email=__email__,
        description="A command line application for renting electro-scooters. Just try it, it is fun :)",
        long_description=__description(),
        long_description_content_type="text/markdown",
        url="https://github.com/vyahello/rent-electro-scooter",
        packages=__find_packages(exclude=("*.tests", "*.tests.*", "tests.*", "tests")),
        include_package_data=True,
        install_requires=__requirements(),
        classifiers=(
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
            "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
            "Operating System :: OS Independent",
        ),
        python_requires=">=3.6",
        entry_points={"console_scripts": ("scooter-rental = scooter.__main__:launch_scooter_rental",)},
    )
