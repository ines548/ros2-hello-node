from setuptools import setup

package_name = 'mon_package'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ines',
    maintainer_email='ines@todo.todo',
    description='My first ROS2 node',
    license='TODO',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'hello_node = mon_package.hello_node:main',
        ],
    },
)
