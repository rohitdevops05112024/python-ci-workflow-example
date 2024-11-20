from setuptools import setup, find_packages

setup(
    name="python-ci-example",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "pytest",
        "flake8",
    ],
    entry_points={
        'console_scripts': [
            'app=src.app:main',
        ],
    },
)

