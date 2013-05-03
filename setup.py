# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


setup(
    name='pydevcmd',
    version='1.0.0',
    description='Django PyDev Management Command',
    author='sammyrulez',
    url='https://github.com/sammyrulez/django_pydev_command',
    license='BSD',
    packages=find_packages(exclude=('tests')),
    package_dir = {'': 'src'},
    py_modules=['pydev'],
    install_requires=['django']
)