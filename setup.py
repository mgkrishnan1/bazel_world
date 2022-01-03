import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bazel_world",
    version="0.0.1",
    author="Cedd Burge",
    author_email="ceddlyburge@gmail.com",
    description="A function that returns 'world'",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mgkrishnan1/bazel_world/bazel_world/coverage-6.2-cp37-cp37m-win_amd64.whl",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
