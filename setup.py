import setuptools

with open("readme.md", "r") as file:
    long_description = file.read()

setuptools.setup(
    name = "tocamelcase",
    packages = ["tocamelcase"],
    version = "0.0.8",
    description = "Convert to CamelCase 🐫",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    include_package_data=True,
    license = "MIT",
    author = "Carlos Abraham",
    author_email = "abraham@abranhe.com",
    url = "https://p.abranhe.com/tocamelcase",
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
        'Issue Tracker': 'https://github.com/abranhe/tocamelcase/issues'
    },
)
