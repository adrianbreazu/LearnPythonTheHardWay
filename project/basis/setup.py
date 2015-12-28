try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'adrianb',
    'url': 'None',
    'download_url': 'N/A',
    'author_email': '@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['main'],
    'scripts': [],
    'name': 'project'
}

setup(**config)
