from setuptools import setup
from setuptools_rust import Binding, RustExtension


setup(
    name='dummy',
    version="0",
    rust_extensions=[RustExtension("hello", path="Cargo.toml", binding=Binding.PyO3, debug=False)],
    install_requires=['numpy',
        "google-cloud-storage",
        "apache_beam",
        "jsonschema",
        "inflection",
                      'PyYAML',
                      'hdbscan'],
)

