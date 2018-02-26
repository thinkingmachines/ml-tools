from setuptools import setup
from setuptools import find_packages

setup(name='tm-ml-tools',
      version='0.1.1',
      description='Tools for Thinking Machines ML Team',
      url='https://github.com/thinkingmachines/ml-tools',
      author='Thinking Machines',
      author_email='hello@thinkingmachin.es',
      license='MIT',
      install_requires=[
            'google_colab',
            'portpicker'
      ],
      dependency_links=[
          'git+https://github.com/googlecolab/colabtools.git#egg=google_colab',
      ],
      packages=find_packages(),
      zip_safe=False)
