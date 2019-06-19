import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
        name='bobby',
		python_requires='>3',
        packages=setuptools.find_packages(),
        include_package_data=True,
        version='0.2.3',
        author="nux99",
        author_email="nugamuhammad@gmail.com",
        url="https://github.com/nuga99/bobby",
        description="Bobby is a package to get prime factor of numbers\
		currently supported for (*nix)",
)
