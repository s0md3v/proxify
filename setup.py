from setuptools import setup, find_packages

setup(
    name="proxify",
    author="Somdev Sangwan",
    author_email="s0md3v@gmail.com",
    version="1.0.0",
    description="Python module to dump usable proxies.",
    url="https://github.com/UltimateHackers/proxify",
    download_url="https://github.com/UltimateHackers/proxify/tarball/master",
    license='GNU General Public License v3 (GPLv3)',
    classifiers=[
        'Development Status :: 5 - Production/Stable',

        'Intended Audience :: Developers',

        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ],
    keywords='proxify',
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    install_requires=['requests'],
    python_requires='>=2, <=2.8',
    

)
