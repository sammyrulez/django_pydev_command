# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


setup(
    name='pydevcmd',
    version='1.0.0',
    description='Django PyDev Management Command',
    author='sammyrulez',
    url='https://github.com/sammyrulez/django_pydev_command',
    license='BSD',
	packages = ['pydev','pydev.management','pydev.management.commands','pydev.management.commands.resources'],
	package_dir = {'': 'src'},  
    install_requires=['Django>=1.4']
)