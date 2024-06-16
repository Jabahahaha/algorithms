from setuptools import setup, find_packages

setup(
    name='root_finding_project',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'matplotlib',
    ],
    entry_points={
        'console_scripts': [
            'root_finding=main:main',
        ],
    },
)
