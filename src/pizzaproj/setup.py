from setuptools import setup

package_name = 'pizzaproj'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='lordinator',
    maintainer_email='nath.kamps@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'talker = pizzaproj.MarkersPos:main',
            'turtle_tf2_listener = pizzaproj.MarkersPos:main',
        ],
    },
)
