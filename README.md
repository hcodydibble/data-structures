[![Build Status](https://travis-ci.org/hcodydibble/data-structures.svg?branch=master)](https://travis-ci.org/hcodydibble/data-structures)[![Coverage Status](https://coveralls.io/repos/github/hcodydibble/data-structures/badge.svg?branch=master)](https://coveralls.io/github/hcodydibble/data-structures?branch=master)

# Python Data Structures

This repo is here to hold all the data structures I write, or at least attempt to write, in my never-ending
pursuit of knowledge in the world of development. Previous works were done with [Adrienne](https://github.com/adriennekarnoski)
and are thus pushed up on her [data-structures repo](https://github.com/adriennekarnoski/data-structures) and mine
will be starting with the Binary Search Tree.

**Installation**:

In case you feel like pulling this down and making the code better, writing more tests to attempt to disprove my
knowledge of these data structures or you just want to mess around in it there are just a few steps you need to follow.

- `$ git clone https://github.com/hcodydibble/data-structures.git`
- `$ cd data-structures/`
- `$ pip install -e .` (The -e is so any changes you make will immediately affect the package without needing to reinstall)

**Tests**:

To run the tests (and to see my amazing coverage and all those precious precious dots) is just as simple as the installation
(and one of these steps can be done above but writing things twice is fun).

- `$ pip install -e .[test]`
- `$ tox`

## Author

The author is me, Cody! I'm working under the assumption that you are already on my [github](https://github.com/hcodydibble)
but linking things with Markdown is fun so there is another one. If you want to follow/watch/stalk me on anything else social
media related you can find me on [Linkedin](https://www.linkedin.com/in/codydibble/), [Twitter](https://twitter.com/hcodydibble),
or [Facebook](https://www.facebook.com/hcodydibble).


## Big O Notations

**Binary Search Tree**

- `.insert(val)` - O(n)
- `.search(val)` - O(n)
- `.size()` - O(1)
- `.balance()` - O(1)
- `.depth()` - O(1)
- `.contains(val)` - O(n)
- `.in_order()` - O(n)
- `.pre_order()` - O(n)
- `.post_order()` - O(n)
- `.breadth_first()`- O(n)
- `.delete(val)` - O(n)

(It seems most of these will end up as O(log n) once the tree is balanced but for now I believe these are the big o notations.)

# JavaScript Data Structures

**Installation**:

Same as with my Python data structures, if you feel like pulling this down and playing around with it there's only a few things to do!

- `$ git clone https://github.com/hcodydibble/data-structures.git`
- `$ cd data-structures/js/`
- `$ npm install data-structures`

**Tests***:

This turned out to be waaaay easier than I thought. Since npm init gives you script commands you just need to type the following (and make sure you're still in the js/ directory)

`$ npm test`

And if you would like to see my actual coverage

`$ npm run covered_test`