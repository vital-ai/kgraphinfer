from setuptools import setup, find_packages

setup(
    name='kgraphinfer',
    version='0.0.1',
    author='Marc Hadfield',
    author_email='marc@vital.ai',
    description='Kgraph Infer',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/vital-ai/kgraphinfer',
    packages=find_packages(exclude=["test", "test_data"]),
    license='Apache License 2.0',
    install_requires=[

            'vital-ai-vitalsigns>=0.1.27',
            'vital-ai-domain>=0.1.7'

    ],
    extras_require={

    },
    classifiers=[
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.11',
)
