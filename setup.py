from setuptools import setup, find_packages


setup(
    name='wagtail_comments_xtd',
    author='André Karlsson',
    license='GPLv3',
    author_email='andre.karlsson@protractus.se',
    version='0.3.0',
    url='https://github.com/joyider/wagtail_comments_xtd',
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        'Topic :: Internet :: WWW/HTTP',
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    packages=find_packages(),
    include_package_data=True,
    python_requires='>=3',
    install_requires=[
        "wagtail>2.16",
        "Django>=3.2",
        "wagtailfontawesome>=1.0.2",
        "django-comments-xtd>=2.9.9"
    ],
)
