from setuptools import setup

setup(
    name='app',
    packages=['app'],
    include_package_data=True,
    install_requires=[
        'flask',
        'dataset',
        'requests',
        'bs4',
        'flask_cors',
        'flask-mysql',
    ],
)