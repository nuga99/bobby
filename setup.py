import setuptools

with open("README.md" , "r") as fh:
	long_description = fh.read()

setuptools.setup(
	name='bobby',
	version='0.1',
	scripts=['bobby'],
	author="nux99",
	description="Bobby is a random python package",
	packages=setuptools.find_packages(),
)
