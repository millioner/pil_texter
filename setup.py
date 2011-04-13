from distutils.core import setup, find_packages

install_requires = [
    'PIL',
]

setup(
    name="pil_texter",
    version=0.1,
    description="A small module for drawing text with PIL",
    long_description=open("README").read(),
    author="Millioner",
    author_email="millioner.bbb@gmail.com",
    url="https://github.com/millioner/pil_texter",
    license='BSD',
    packages=find_packages(),
    package_dir={"texter": "texter"},
    include_package_data=True,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Python Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python"
    ]
)