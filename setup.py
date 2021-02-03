from distutils.core import setup
import sys

if sys.version_info[0] < 3:
    with open('README.md') as f:
        long_description = f.read()
else:
    with open('README.md', encoding='utf-8') as f:
        long_description = f.read()

setup(name='FireflyAlgorithm',
      description='Firefly algorithm implementation',
      long_description=long_description,
      long_description_content_type="text/markdown",
      author='firefly-cpp',
      version='0.0.4',
      license='MIT',
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Developers',
          'Intended Audience :: Science/Research',
          'Operating System :: OS Independent',
          'Topic :: Scientific/Engineering',
          'Topic :: Software Development',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Programming Language :: Python :: 3.9',
          'Programming Language :: Python :: 3.10'
      ],
      url='https://github.com/firefly-cpp/FireflyAlgorithm',
      py_modules=['FireflyAlgorithm']
      )
