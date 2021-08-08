# -*- coding: utf-8 -*-
from setuptools import setup

setup(
   name='ResNova',
   version='0.1.0',
   author='Nahuel Ferreiro',
   author_email='ferreiro@mpp.mpg.de',
   packages=['ResNova'],
   license='LICENSE.txt',
   description='Cryogenic detectors for neutrino detection',
   long_description='For now no long description',
   #long_description=open('README.txt').read(),
   install_requires=[
       "numpy>=1.19.2",
       "scipy>=1.5.2",
       "pandas",
       "matplotlib"
   ],
)
