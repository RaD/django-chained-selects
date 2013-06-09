from setuptools import setup, find_packages

setup(
    name='django-chained-select',
    version='0.1',
    description="A django app to link two select fields together",
    author='Ruslan Popov',
    author_email='ruslan.popov@gmail.com',
    url="http://github.com/RaD/django-chained-select",
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities'],
)
