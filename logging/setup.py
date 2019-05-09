import sys
# Remove current dir from sys.path, otherwise setuptools will peek up our
# module instead of system's.
sys.path.pop(0)
from setuptools import setup
sys.path.append("..")
import sdist_upip

setup(name='micropython-logging',
      version='0.5.2',
      description='logging module for MicroPython',
      long_description=open('README.rst').read(),
      url='https://github.com/pfalcon/micropython-lib',
      author='Stefan Lehmann',
      author_email='micropython-lib@googlegroups.com',
      maintainer='Paul Sokolovsky',
      maintainer_email='micropython-lib@googlegroups.com',
      license='MIT',
      cmdclass={'sdist': sdist_upip.sdist},
      packages=['logging'],
      install_requires=['micropython-os'])
