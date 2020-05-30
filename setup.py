from setuptools import setup
with open("README.md", "r") as fh:
    long_description = fh.read()
setup(name='gill',
      version='0.0.1',
      author="Saikat Bhattacharjee",
      author_email="bhattacharjee.saikat3@hotmail.com",
      description="A sample PySpark application",
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="https://github.com/saikat-bh/python_wheel",
      packages=['python_wheel'],
      classifiers=[
          "Programming Language :: Python :: 3",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
      ],
      zip_safe=False)