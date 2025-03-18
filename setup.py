from setuptools import find_packages
from setuptools import setup
import os


def read_file(name):
    with open(os.path.join(os.path.dirname(__file__), name)) as f:
        return f.read()


version = '0.1.dev0'
shortdesc = 'Chart.js integration into cone'
longdesc = '\n\n'.join([read_file(name) for name in [
    'README.rst',
    'CHANGES.rst',
    'LICENSE.rst'
]])



setup(
    name='cone.charts',
    version=version,
    description=shortdesc,
    long_description=longdesc,
    classifiers=[
        'Environment :: Web Environment',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    keywords='node pyramid cone web',
    author='Cone Contributors',
    author_email='dev@conestack.org',
    url='http://github.com/conestack/cone.charts',
    license='MIT',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    namespace_packages=['cone'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'cone.app[lxml]>=1.0.3',
        'yafowil.yaml'
    ],
    extras_require=dict(
        test=[
            'zope.pytestlayer',
            'pytest',
        ],
        docs=[
            'Jinja2<3.0',
            'markupsafe<2.1.0',
            'Sphinx',
            'sphinx-conestack-theme',
            'sphinx-js'
        ]
    )
)
