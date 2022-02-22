""" 
gw4xxx-launcher - IoTmaxx Gateway Hardware Abstraction Layer
Copyright (C) 2021 IoTmaxx GmbH

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
from setuptools import setup, find_packages

version = {}
with open("iot_launcher/version.py") as fp:
    exec(fp.read(), version)

setup(
    name='gw4xxx_flask',
    version=version['__version__'],
    url='https://github.com/iotmaxx/gw4xxx-launcher',
    author='Ralf Glaser',
    author_email='glaser@iotmaxx.de',
    description='IoTmaxx gateway application launcher',
    packages=find_packages(),    
    install_requires=[],
)
