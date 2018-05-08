from setuptools import setup

setup(name='PyRadioLoc',
      version='0.1',
      description='Radio Localization for Python',
      url='http://github.com/timotrob/PyRadioLoc',
      author='Robson Dias Alves Timoteo',
      author_email='rdat@cin.ufpe.br',
      license='MIT',
      packages=['PyRadioLoc'],
      install_requires=[
          'numpy','geographiclib'
      ],
      zip_safe=False)

