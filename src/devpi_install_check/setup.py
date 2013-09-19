from setuptools import setup


setup(
    name='devpi_install_check',
    py_modules=['devpi_install_check'],
    entry_points={
        'console_scripts': [
            'devpi-install-check=devpi_install_check:main']})
