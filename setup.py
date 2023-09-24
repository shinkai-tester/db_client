from setuptools import setup

REQUIRES = [
    'records>=0.5.3',
    'structlog>=23.1.0'
]

setup(
    name='db_client',
    version='0.0.1',
    packages=['db_client'],
    url='https://github.com/shinkai-tester/db_client.git',
    license='MIT',
    author='Aleksandra Klimantova',
    author_email='',
    install_requires=REQUIRES,
    description='DB client with logger'
)
