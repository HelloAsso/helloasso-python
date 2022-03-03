from setuptools import setup, find_packages

with open("README.md") as f:
    readme = f.read()

setup(
    name="helloasso.apiv5",
    version="1.0.0",
    description="Python wrapper for Helloasso APIV5",
    long_description=readme,
    packages=find_packages(exclude=("tests", "docs")),
    install_requires=[
        "requests>=2.23.0",
        "oauthlib==3.1.0",
        "requests-oauthlib==1.3.0",
        "typing_extensions==3.7.4.2",
    ],
    python_requires=">=3.7",
)
