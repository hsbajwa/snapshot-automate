from setuptools import setup
setup(
    name = 'shotty',
    version = '0.1',
    author = 'Harry Bajwa',
    author_email = 'harrybajwa0628@gmail.com',
    description = 'Practice project for AWS',
    packages = ['shotty'],
    url = "https://github.com/hsbajwa/meteorite-project",
    install_requires=[
        'click',
        'boto3'
    ],
    entry_points='''
        [console_scripts]
        shotty=shotty.shotty:cli
    ''',
)
