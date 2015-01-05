try:
	from setuptools import setuptool
except:
	from distutils.core import setup

config = {
	'description': 'My Project',
	'author': 'Nitin Venkatesh',
	'url': 'http://nitstorm.github.io/',
	'download_url': 'yet to be configured',
	'author_email': 'xyz@gmail.com',
	'version':'0.1',
	'install_requires': ['nose'],
	'packages': ['ex48'],
	'scripts': [],
	'name': 'ex48'
}

setup(**config)
