# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name="pyEddyTracker",
    version="3.0.0",
    description="Py-Eddy-Tracker libraries",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Scientific/Engineering :: Physics",
        "Programming Language :: Python",
    ],
    keywords="eddy science, eddy tracking, eddy tracker",
    author="emason",
    author_email="emason@imedea.uib-csic.es",
    packages=find_packages("src"),
    package_dir={"": "src"},
    scripts=[
        "src/scripts/GridFiltering",
        "src/scripts/EddyId",
        "src/scripts/EddySubSetter",
        "src/scripts/EddyTranslate",
        "src/scripts/EddyTracking",
        "src/scripts/EddyFinalTracking",
        "src/scripts/EddyMergeCorrespondances",
        "src/scripts/ZarrDump",
        "src/scripts/GUIEddy",
    ],
    zip_safe=False,
    entry_points=dict(
        console_scripts=["MergeEddies = py_eddy_tracker.appli:merge_eddies"]
    ),
    package_data={
        "py_eddy_tracker.featured_tracking": ["*.nc"],
        "py_eddy_tracker": ["data/*.nc"],
    },
    install_requires=[
        "matplotlib",
        "netCDF4>=1.1.0",
        "numba",
        "numpy>=1.14",
        "opencv-python",
        "pint",
        "polygon3",
        "pyproj",
        "pyyaml",
        "scipy>=0.15.1",
        "zarr",
    ],
)
