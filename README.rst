

.. image:: https://badge.fury.io/py/ordered-set-minghu6.svg
   :target: https://badge.fury.io/py/ordered-set-minghu6

.. image:: https://travis-ci.org/minghu6/ordered-set.svg
   :target: https://travis-ci.org/minghu6/ordered-set

.. image:: https://landscape.io/github/minghu6/ordered-set/master/landscape.svg?style=flat
   :target: https://landscape.io/github/minghu6/ordered-set/master
   :alt: Code Health

An OrderedSet is a custom MutableSet that remembers its order, so that every
entry has an index that can be looked up.

Based on a recipe originally posted to ActiveState Recipes by Raymond Hettiger,
and released under the MIT license:

    http://code.activestate.com/recipes/576694-orderedset/

Rob Speer's changes are as follows:

    - changed the content from a doubly-linked list to a regular Python list.
      Seriously, who wants O(1) deletes but O(N) lookups by index?
    - add() returns the index of the added item
    - index() just returns the index of an item
    - added a __getstate__ and __setstate__ so it can be pickled
    - added __getitem__
    - __getitem__ and index() can be passed lists or arrays, looking up all
      the elements in them to perform NumPy-like "fancy indexing"

minghu6's changes are as follow:

    - restrict the OrderedSet operation object: only themselves.
      Because OrderededSet's element consists of its index and value,
      Python set's element only consists of its value, however.
      I have written a new class OrderedSetAdapter to adapt Python set.
    - writtern a new class OrderedSetAdapter
    - rewrittern some contradictory method from collections.MutableSet





Tested on Python 2.7, 3.3, 3.4, 3.5, 3.6, PyPy, and PyPy3.