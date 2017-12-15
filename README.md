[![Build Status](https://travis-ci.org/hcodydibble/data-structures.svg?branch=master)](https://travis-ci.org/hcodydibble/data-structures)[![Coverage Status](https://coveralls.io/repos/github/hcodydibble/data-structures/badge.svg?branch=master)](https://coveralls.io/github/hcodydibble/data-structures?branch=master)

# Data Structures

This repo is here to hold all the data structures I write, or at least attempt to write, in my never-ending
pursuit of knowledge in the world of development. Previous works were done with [Adrienne](https://github.com/adriennekarnoski)
and are thus pushed up on her [data-structures repo](https://github.com/adriennekarnoski/data-structures) and mine
will be starting with the Binary Search Tree (in Python, JavaScript started LinkedList).

## Author

The author is me, Cody! I'm working under the assumption that you are already on my [github](https://github.com/hcodydibble)
but linking things with Markdown is fun so there is another one. If you want to follow/watch/stalk me on anything else social
media related you can find me on [Linkedin](https://www.linkedin.com/in/codydibble/), [Twitter](https://twitter.com/hcodydibble),
or [Facebook](https://www.facebook.com/hcodydibble).
## Python
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



### Big O Notations

**Doubly Linked List**:

- `.push(val)` - O(1)
- `.append(val)` - O(1)
- `.pop()` - O(1)
- `.shift()` - O(1)
- `.size()` - O(1)
- `.remove(val)` - O(n)

**Deque**:

- `.append(val)` - O(1)
- `.appendleft(val)` - O(1)
- `.pop()` - O(1)
- `.popleft()` - O(1)
- `.peek()` - O(1)
- `.peekleft()` - O(1)
- `.size()` - O(1)

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

**Trie Tree**:

- `.insert(string)` - O(n)
- `.contains(string)` - O(n)
- `.size()` - O(1)
- `.remove(string)` - O(n)

**Hash Table**:

- `.set(key, val)` - O(n)
- `.get(key` - O(1)
- `._hash(key, style)` -O(n)


## Sorting Algorithms

We are now adding sorting algorithm happy fun times to this repo so under this section I will try and add a bit of info about the algorithm and what I feel the Big O notation of it is.

### Bubble Sort

This sorting algorithm will run through a given list of numbers and move a number down until it is no longer larger than the next number coming it. It will then continue to move down the list switching numbers until it comes to the end, where it will then proceed to the very beginning of the list and do it all over again until the entire list is sorted smallest to largest (it could easily switched to run largest to smallest as well).

- **Big O Notation**: The time complexity of a bubble sort at worst case is going to be O(n^2).

### Insertion Sort

This sorting algorithm will run through a list and check each new number it comes across against all the numbers it has already sorted to then decide where to insert it.

- **Big O Notation**: The time complexity of an insertion sort at worst case is going to be O(n^2)

### Merge Sort

This sorting algorithm will split a down until it has 1 to 2 items (only 1 according to [visualgo](https://visualgo.net/en)) and then will build itself back up from the bottom up.

- **Big O Notation**: The time complexity of a merge sort will always be O(n log n)

### Quick Sort

This sorting algorithm will choose a spot in a list to be the pivot point, it will then check the rest of the list and split it based on if the number is larger or smaller than the pivot number. It will continue to do this until it has two sorted lists of numbers smaller than the pivot and numbers larger than the pivot and then will smoosh them all back together.

- **Big O Notation**: The time complexity of a quick sort at worst case will be O(n^2)

### Radix Sort

This sorting algorithm takes a list of numbers and, starting with the right most number in each number of the list, will plop them in a container. After it does that it will rebuild the list and continue to do this for however long the largest number in the list is.

- **Big O Notation**: The time complexity of the radix sort at worst case is O(nk)


## JavaScript Data Structures

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