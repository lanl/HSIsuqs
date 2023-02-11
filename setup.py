from setuptools import setup, find_packages
from Cython.Build import cythonize

setup(
    name="HSIsuqs",
    version="1.0.0",    
    packages=find_packages(),
    ext_modules=cythonize(["HSIsuqs/models/_slic.pyx"],
                       compiler_directives={'language_level' : "3"}),
    description='Code for doing hyperspectral image segmentation and uncertainty quantification.',
    long_description=README.md,
    long_description_content_type='text/markdown',
    url='https://github.com/lanl/HSIsuqs',
    author='Scout Cabe Jarman',
    author_email='scoutjarman@yahoo.com',
    license='GPLv3',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Education',
        'Topic :: Scientific/Engineering :: Image Processing',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Scientific/Engineering :: Visualization',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3' ,
        'Environment :: GPU :: NVIDIA CUDA',
        'Natural Language :: English',
        'Programming Language :: Cython',
        'Programming Language :: Python :: 3'],
    keywords='Hyperspectral Image Analysis Image Segmentation',
    python_requires='>=3',
    )