try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Exercise49',
    'author': 'adrianb',
    'url': 'None',
    'download_url': 'N/A',
    'author_email': '@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['exercise49'],
    'scripts': [],
    'name': 'Exercise 49'
}

setup(**config)
