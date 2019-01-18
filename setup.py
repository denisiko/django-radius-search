from distutils.core import setup

setup(
    name='django-radius-search',
    version='0.1',
    description='Simple manager tool for finding nearby locations in Django',
    license='MIT',
    author='Denis Anuschewski',
    author_email='denis@anuschewski.com',
    url='https://github.com/denisiko/django-radius-search',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        "Operating System :: OS Independent",
        'Programming Language :: Python',
    ],
    requires=['django'],
    packages=['radius_search'],
)