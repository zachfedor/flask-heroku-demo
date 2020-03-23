import setuptools

with open("README.md", "r") as f:
    long_description = f.read()


setuptools.setup(
    name="flaskherokudemo"
    version="0.0.1",
    author="Zach Fedor",
    author_email="zachfedor@gmail.com",
    url="https://github.com/zachfedor/flask-heroku-demo",
    description="Hello world app configured to be deployed to Heroku",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires=[],
    extras_require=[],
    tests_require=['pytest'],
    python_requires='>=3.6',
)

