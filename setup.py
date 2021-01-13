from pathlib import Path

import setuptools

file_path = Path(__file__)
with open(file_path.parent / 'README.md', 'r') as fh:
    LONG_DESCRIPTION = fh.read()

setuptools.setup(
    name='caktin',
    version=0.1.0,
    author='Lionel Gulich',
    author_email='lgulich@ethz.ch',
    url='https://github.com/lgulich/caktin',
    description='A tool for compiling cakti.',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    install_requires=[],
    classifiers=[
        'Programming Language :: Python :: 3 :: Only',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: POSIX :: Linux',
        'Natural Language :: English',
    ],
    license='Closed',
    scripts=[
        'scripts/caktin',
    ],
    python_requires='>=3.6',
)
