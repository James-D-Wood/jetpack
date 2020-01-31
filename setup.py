from setuptools import setup

setup(
    name='bchoc',
    version='0.1',
    py_modules=['bchoc'],
    install_requires=[
        'Click',
    ],
    entry_points= {
        "console_scripts": ["bchoc = bchoc.cli:run"]
    }
)