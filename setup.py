#!/usr/bin/env python
from setuptools import setup, find_packages
import io

from CalendarFusion import __NAME__, __VERSION__


def required(sfx=""):
    with io.open(f"requirements{sfx}.txt", encoding="utf-8") as f:
        return f.read().splitlines()


setup(
    name=__NAME__,
    version=__VERSION__,
    description="A python module to generate fancy markdown table based calendar",
    author="Dipankar Pal",
    keywords="calendar markdown-table markdown calendar-to-table cli-app",
    author_email="dipankarpal5050@gmail.com",
    url="http://github.com/deep5050/CalendarFusion",
    download_url="https://github.com/deep5050/CalendarFusion/tarball/master",
    packages=find_packages(exclude=["test*"]),
    install_requires=required(),
    extras_require={"dev": required("-dev")},
    license="MIT",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Communications :: Email :: Filters",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content :: CGI Tools/Libraries",
        "Topic :: Internet :: WWW/HTTP :: Site Management",
        "Topic :: Software Development :: Documentation",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Text Processing :: Filters",
        "Topic :: Text Processing :: Markup :: HTML",
        "Topic :: Text Processing :: Markup :: Markdown",
    ],
)
