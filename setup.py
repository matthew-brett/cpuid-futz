import platform

if platform.processor() not in ('i386', 'x86_64'):
    raise RuntimeError('x86cpu only builds on x86 CPUs')

from os.path import join as pjoin
from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

ext_modules = [Extension("x86cpu.cpuinfo",
                         [pjoin(*parts) for parts in (
                             ['x86cpu', 'cpuinfo.pyx'],
                             ['src', 'cpuid.c'],
                             ['src', 'os_restores_ymm.c'])],
                         include_dirs = ['src'])]

setup(
    name = 'x86cpu',
    cmdclass = {'build_ext': build_ext},
    ext_modules = ext_modules,
    packages     = ['x86cpu',
                    'x86cpu.tests']
)
