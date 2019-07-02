from setuptools import setup


setup(name='guaiaca',
      version_format='{tag}.dev{commitcount}',
      setup_requires=['setuptools-git-version'],
      description='Simple integration with AWS S3',
      url='https://github.com/geislor/guaiaca',
      author='Geislor Crestani',
      author_email='geislor@gmail.com',
      license='MIT',
      packages=['guaiaca'],
      zip_safe=False)
