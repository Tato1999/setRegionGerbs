from setuptools import setup, find_packages

setup(
    name="setRegionGerbs",  # Your package name
    version="0.1.0",  # Version of your package
    description="A module to download region flags (gerbs) based on ISO codes",  # Short description
    long_description=open("README.md").read(),  # Description from README file
    long_description_content_type="text/markdown",  # Specify Markdown format
    author="Tarieli Tabatadze",  # Your name
    author_email="tato.tabatadze.1999@gmail.com",  # Your email
    url="https://github.com/Tato1999",  # Your GitHub repository URL
    packages=find_packages(),  # Automatically discover submodules
    py_modules=["setRegionGerbs"],  # Include your Python script
    install_requires=[
        "requests",  # Dependencies required for your script
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",  # Minimum Python version
)
