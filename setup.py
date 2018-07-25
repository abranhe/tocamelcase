import setuptools

with open("README.md", "r") as file:
    long_description = file.read()

setuptools.setup(
    name = "tocamelcase",
    packages = ["tocamelcase"],
    version = "0.0.7",
    description = "🐫 To Camel Case: self explanatory!",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    license = "MIT",
    author = "Carlos Abraham",
    author_email = "abraham@abranhe.com",
    url = "https://abranhe.com",
    classifiers=(
        "Programming Language :: Python",
        "Natural Language :: English",
        "Environment :: Plugins",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
    ),
    project_urls={
        'Source': 'https://github.com/abranhe/tocamelcase',
    },
)
