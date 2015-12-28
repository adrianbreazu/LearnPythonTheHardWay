try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'exercise 47 of book Learn Python The Hard Way',
    'author': 'adrianb',
    'url': 'None',
    'download_url': 'N/A',
    'author_email': '@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['exercise47'],
    'scripts': [],
    'name': 'exercise47'
}

setup(**config)
