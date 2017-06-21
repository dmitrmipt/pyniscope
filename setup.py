from setuptools import setup
setup(name='pyniscope',
      version='0.3',
      packages=['niscope'],
      install_requires=['numpy'],
      author="Bernardo Kyotoku, John Vishnefske",
      author_email="jvdude.developer@mailnull.com",
      description="Python wrapper for NI Oscilloscopes",
      url="https://github.com/bernardokyotoku/pyniscope",
      long_description=open("README.md").read(),
      classifiers=[
        "Programming Language :: Python",
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Natural Language :: English",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: Microsoft :: Windows :: Windows 7",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 2.7"
        "Topic :: Scientific/Engineering",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Intended Audience :: Science/Research"
    ],

    )
