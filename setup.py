from setuptools import setup, find_packages

# Read the contents of your README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='discord_help',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'discord.py',
    ],
    author='Awakno',
    author_email='awaknocode@email.com',
    description='Discord_help is a package to help developers of discord bots',
    long_description=long_description,  # Add long_description
    long_description_content_type='text/markdown',  # Specify content type for long_description
    url='https://github.com/Awakno/discord_help',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Add minimum Python version requirement
)
