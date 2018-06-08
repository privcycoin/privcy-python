from setuptools import setup, find_packages
setup(
    name='privcy-python',
    version='0.1.3',
    description='Friendly privcy JSON-RPC API binding for PRiVCY',
    long_description='This package allows performing commands such as listing the current balance'
    ' and sending coins to the Satoshi (original) client from Python. The communication with the'
    ' client happens over JSON-RPC.',
    maintainer='PRiVCY',
    maintainer_email='info@privcy.io',
    url='http://github.com/privcy-python/doc/',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'License :: OSI Approved :: MIT License',
        'Topic :: Office/Business :: Financial'
    ],
    packages=find_packages("src"),
    install_requires=['simplejson'],
    package_dir={'': 'src'}
)
