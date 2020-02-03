from setuptools import setup

setup(
    name='Jetpack',
    version='0.1',
    py_modules=['jetpack'],
    install_requires=[
        'Click',
    ],
    entry_points= {
        "console_scripts": ["jetpack = jetpack.cli:cli"]
    }
)