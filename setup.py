try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'TF2 Outpost Autobumper',
    'author': 'Sal Olivares',
    'url': '',
    'download_url': '',
    'author_email': '',
    'version': '0.1',
    'install_requires': [
        "selenium==2.48.0",
        "splinter==0.7.3",
        "wheel==0.24.0"
    ],
    'packages': ['outpostAutoBump'],
    'scripts': [],
    'name': 'outpostAutoBump'
}

setup(**config)
