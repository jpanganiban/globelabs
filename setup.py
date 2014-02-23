from setuptools import setup

__name__ = 'globelabs'
__version__ = '0.0.2'
__author__ = 'Jesse Panganiban'

install_requires = ['requests']


setup(name=__name__,
      version=__version__,
      author=__author__,
      url="http://developer.globelabs.com.ph",
      author_email="me@jpanganiban.com",
      install_requires=install_requires,
      py_modules=['globelabs'])
