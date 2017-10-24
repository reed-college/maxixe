from setuptools import setup
setup(
    name="maxixe",
    version="0.2",
    packages=[
        "maxixe",
    ],
    scripts=[
        "mockTango"
    ],
    install_requires=[
        'Flask>=0.12.2',
        'requests>=2.18.4',
    ],
    include_package_data=True,
)
