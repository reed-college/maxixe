from setuptools import setup
setup(
    name="maxixe",
    version="0.1",
    packages=[
        "maxixe",
    ],
    scripts=[
        "mockTango"
    ],
    install_requires=[
        'Flask>=0.12.2'
    ],
)
