try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Exercise 48 details',
    'author': 'adrianb',
    'url': 'None',
    'download_url': 'N/A',
    'author_email': '@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['exercise48'],
    'scripts': [],
    'name': 'exercise48'
}

setup(**config)
