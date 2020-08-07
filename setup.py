from setuptools import setup, find_namespace_packages
from setuptools_rust import Binding, RustExtension


setup(
    name='dummy',
    version="0",
    packages=find_namespace_packages(include=['dummy.*']),
    namespace_packages=['dummy'],
    rust_extensions=[RustExtension("dummy.hello", path="Cargo.toml", binding=Binding.PyO3, debug=False)],
)

