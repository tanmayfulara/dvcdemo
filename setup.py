from setuptools import setup, find_packages

setup(
    name="wine_q",  # It's good practice to specify the name of the package
    version="0.0.1",
    description="wine Q",
    author="tanmayfulara",
    packages=find_packages(),  # find packages in the "src" directory
      # tell setuptools to look in "src" for the packages
    license="MIT"
)
