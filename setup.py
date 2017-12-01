from setuptools import setup

setup(
    name="data-structures",
    description="Data structures.",
    py_modules=['dll', 'deque', 'bst'],
    install_requires=[],
    extras_require={'test': ['pytest', 'pytest-watch', 'tox']},
    package_dir={"": "src"}
)