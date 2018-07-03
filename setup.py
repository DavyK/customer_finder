from setuptools import setup

package_locals = {}
version = '0.0.1'

setup(
    name='customer_finder',
    version=version,
    description='find customers near to a given location',
    author='David Kavanagh',
    author_email='davykavanagh@gmail.com',
    packages=['customer_finder'],
    install_requires=[
        'pytest',
    ],
    entry_points={
        'console_scripts': [
            'customers = customer_finder.main:cli',
        ]
    }
)
