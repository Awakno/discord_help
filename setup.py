from setuptools import setup, find_packages

setup(
    name='discord_help',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'discord.py',
        
    ],
    author='Awakno',
    author_email='awaknocode@email.com',
    description='Discord_help it\'s a package to help developer of discord bot', 
    url='https://github.com/Awakno/discord_help',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)