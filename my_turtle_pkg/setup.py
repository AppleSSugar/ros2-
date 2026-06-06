from setuptools import setup
from glob import glob
import os

package_name = 'my_turtle_pkg'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        (
            'share/ament_index/resource_index/packages',
            ['resource/' + package_name]
        ),
        (
            'share/' + package_name,
            ['package.xml']
        ),
        (
            os.path.join('share', package_name, 'launch'),
            glob('launch/*.py')
        ),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='sugar',
    maintainer_email='sugar@example.com',
    description='Turtle figure-8 demo',
    license='Apache License 2.0',
    entry_points={
        'console_scripts': [
            'turtle_figure8 = my_turtle_pkg.turtle_figure8:main',
        ],
    },
)
