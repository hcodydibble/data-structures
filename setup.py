from setuptools import setup

MODULES = ['bst',
'bubble_sort',
'deque',
'dll',
'hashtable',
'insertion_sort',
'linked_list',
'merge_sort',
'priorityq',
'que_',
'quick_sort',
'radix_sort',
'trie']

setup(
    name="data-structures",
    description="Data structures.",
    py_modules=MODULES,
    install_requires=[],
    extras_require={'test': ['pytest', 'pytest-watch', 'tox']},
    package_dir={"": "src"}
)