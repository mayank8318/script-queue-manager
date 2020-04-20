import os
from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.readlines()

with open(os.path.join('.', 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='script_queue_manager',
    version='0.0.4',
    author='Mayank Vaidya',
    author_email='mayank8318@gmail.com',
    url='https://github.com/mayank8318/script-queue-manager',
    description='A CLI tool to manage script queue',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'sqm-pusher = script_queue_manager.pusher:pusher',
            'sqm-executor = script_queue_manager.executor:executor'
        ]
    },
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    keywords='script_queue_manager manage-tasks queue tasks python package mayank8318',
    install_requires=requirements,
    zip_safe=False,
    include_package_data=True
)
