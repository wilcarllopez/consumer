from setuptools import  setup

setup(name='consumer',
      version='0.1.0',
      description="A consumer module for use with the created application in ''listdir'' repository, branch ''write-to-queue''",
      url='https://github.com/wilcarllopez/consumer',
      author='Wilcarl D. Lopez',
      author_email='wilcarl_lopez@trendmicro.com',
      license='MIT',
      classifiers=[
            'Development Status :: Alpha',
            'Intended Audience :: Sir Anwar Sumawang',
            'Programming Language :: 3',
            'Programming Language :: 3.7'
      ],
      data_files=None,
      include_package_data = True,
      # scripts= ,
      entry_points={
            'console_scripts': [
                  'consumer=consumer.consumer:main'
            ]
      },
      packages=['consumer'], install_requires=['pika'])
