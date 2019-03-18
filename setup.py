from setuptools import setup, find_packages

setup(
    name='recursion_sort',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='Njabulo Magudulela recursion_sort python package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/Njabulo961/recursion_sort',
    author='Njabulo Magudulela',
    author_email='njabulo.magd@gmail.com'
)