v15.0.0
=======

Removed cmp module.

``Popen_nonblocking`` now sets text mode.

v14.0.3
=======

Removed compatibility code.

v14.0.2
=======

Use PEP 420 for namespace package.

v14.0.1
=======

Refresh package metadata.

v14.0.0
=======

Require Python 3.6 or later.

13.0
====

Switch to `pkgutil namespace technique
<https://packaging.python.org/guides/packaging-namespace-packages/#pkgutil-style-namespace-packages>`_
for the ``jaraco`` namespace.

12.0
====

* Removed ``auth`` module. Use `grampg
  <https://pypi.org/project/grampg>`_ instead.

* Removed ``jaraco.lang`` package with ``jaraco.lang.python``.
  ``mf`` and ``obinfo`` were unused and ``callable`` returned
  to Python 3.

* Removed ``jaraco.util.exceptions.suppress_exception``. Use
  ``contextlib2.suppress`` instead.

* Removed ``jaraco.util.random``. Use ``os.urandom`` instead
  of ``random.bytes``.

* Moved ``jaraco.util.stream.Tee`` to `jaraco.stream
  <https://pypi.org/project/jaraco.stream>`_ (1.2).

* Removed PIPE attribute from ``jaraco.util.subprocess``.

11.0
====

* Removed deprecated modules and functions.

10.14
=====

* Deprecated ``jaraco.util.filesystem`` and ``jaraco.filesystem``.
  Functionality has been moved to the ``jaraco.path`` package.

10.13
=====

* Deprecated ``jaraco.util.bitutil``. Functionality has been
  moved to the ``jaraco.structures`` package.

10.12
=====

* Deprecated ``jaraco.util.cmdline``. Functionality has been
  moved to the ``jaraco.ui`` package.

10.11
=====

* Bump to ``jaraco.ui`` 1.1, avoiding setuptools_scm issue.

10.10
=====

* Deprecated ``jaraco.util.ui``, ``jaraco.util.editor``, and
  ``jaraco.util.input``. Functionality has been moved to the ``jaraco.ui``
  package.

10.9
====

* Deprecated ``jaraco.util.logging``. Functionality has been moved to the
  ``jaraco.logging`` package.
* Deprecated ``jaraco.util.meta`` and ``jaraco.util.classlib`` and
  ``jaraco.util.properties``. Functionality
  has been moved to the ``jaraco.classes`` package.
* Deprecated ``jaraco.util.classlib.ensure_sequence``. Use
  ``jaraco.itertools.always_iterable`` instead.
* Deprecated ``jaraco.util.context``. Functionality moved to
  ``jaraco.context``.
* Deprecated ``jaraco.util.dictlib`` and ``jaraco.util.collections``.
  Functionality has been moved to the ``jaraco.collections`` package.
* Deprecated ``jaraco.util.string``. Functionality moved to the ``jaraco.text``
  package.

10.8
====

* Deprecated ``jaraco.util.functools``. Functionality has been moved to the
  ``jaraco.functools`` package.
* Deprecated ``jaraco.tempora`` module. Functionality has been moved to the
  ``tempora`` package.
* Deprecated ``jaraco.util.numbers.ordinalth``. Use ``inflect`` package
  instead.
* Deprecated ``jaraco.itertools`` module. Functionality has been moved to the
  ``jaraco.itertools`` package.

10.7.1
======

* Fix ``tempora.calculate_prorate`` on Python 3.

10.7
====

* Added methods to ``jaraco.util.WordSet``.

10.6
====

* Added ``dictlib.Enumeration``.

10.5
====

* Moved functionality from words function to ``WordSet.parse``. ``words``
  retained for compatibility.

10.4
====

* WordSet and words results can now be readily sliced.

10.3
====

* Add classproperty to properties module.

10.2
====

* Moved jaraco.util.timing into its own package under jaraco.timing and
  deprecated the module in this package.

10.1
====

* Added ``meta.TagRegistered``.

10.0.2
======

* Restore ``itertools.one``, unintentionally removed in 10.0.

10.0.1
======

* Restore Python 2 compatibility.

10.0
====

* Removed several itertools recipes now obviated by `more-itertools
  <https://github.com/erikrose/more-itertools>`_ (recipes and more):

  - grouper -> recipes.grouper
  - grouper_nofill -> more.chunked (note parameters are switched)
  - chain -> itertools.chain.from_iterable

  The following can now be found in more_itertools.recipes:

  - pairwise
  - consume
  - roundrobin
  - unique_justseen
  - unique_everseen

* Add logging.setup_requests_logging, following the pattern document at
  `StackOverflow
  <http://stackoverflow.com/questions/10588644/how-can-i-see-the-entire-request-thats-being-sent-to-paypal-in-my-python-applic/16630836#16630836>`_.


9.0.1
=====

* Apply fix in 8.9.1 to 9.0.

9.0
===

* ``itertools.one()`` now always raises a ValueError and never a
  StopIteration.

8.9.1
=====

* Use six for callable in NonDataProperty, restoring Python 3.1 compatibility.

8.9
===

* Added ``KeyTransformingDict.matching_key_for``, allowing the original key
  to be returned.

8.8
===

* Added ``context.ExceptionTrap``.

8.7
===

* Removed dependency links for ``six``.

8.6
===

* Added ``collections`` module with an Everything collection.

8.5
===

* Added ``ui.countdown`` function.

8.4
===

* ``cmdline.Command`` now exposes an ``invoke`` class method to facilitate
  a common invocation.

8.2
===

* ``timing.Stopwatch`` context now returns self for convenience.

8.1
===

* Moved `jaraco.dateutil` to `jaraco.tempora` (but kept jaraco.dateutil for
  compatibility). Expect `jaraco.dateutil` to be removed in 9.0.

8.0
===

* Package no longer uses 2to3 for Python 3 support, but instead relies on a
  unified code base and compatibility routines (including six).
* Moved ``wallpaper`` module to ``jaraco.desktop`` project.

7.2
===

* ``dictlib.FrozenDict`` now supplies ``.copy``.
* Fixed issue in ``FrozenDict`` where ``.__eq__`` didn't work on other
  FrozenDict instances.

7.1
===

* Added ``dictlib.FrozenDict``.

7.0
===

* Moved `blowfish` module to jaraco.crypto.
* Moved `image` module to jaraco.imaging.

6.8
===

* Added `string.simple_html_strip`.

6.7
===

* Added `itertools.unique_everseen` from Python docs.

6.6
===

* Added `dateutil.parse_timedelta`.

6.5
===

* Added `itertools.remove_duplicates` and `itertools.every_other`.
* `functools.compose` now allows the innermost function to take arbitrary
  arguments.

6.4
===

* Added `dictlib.BijectiveMap`.

6.3
===

* Added cmdline module.

6.2
===

* Added IntervalGovernor to `timing` module. Allows one to decorate a
  function, causing that function to only be called once per interval, despite
  the number of calls attempted.
* Added `itertools.suppress_exceptions`. Use it to iterate over callables,
  suppressing exceptions.

6.1
===

* Added `context` module, with a null_context context manager. It is suitable
  for taking the place of a real context when no context is needed.

6.0
===

* `itertools.always_iterable` now returns an empty iterable when the input
  is None. This approach appears to work better for the majority of use-cases.

5.5
===

* Added `itertools.is_empty`.

5.4
===

* Added context manager support in `timing.Stopwatch`.

5.3.1
=====

* Fixed issue with `dictlib.RangeMap.get` so that it now works as one would
  expect.

5.3
===

* Added `string.words` for retrieving words from an identifier, even if
  it is camelCased.

5.2
===

* Added `string.indent`.

5.1
===

* Added `functools.once`, a rudimentary caching function to ensure an
  expensive or non-idempotent function is not expensive on subsequent calls
  and is idempotent.

5.0
===

* Renamed method in KeyTransformingDict from `key_transform` to
  `transform_key`.
* Fixed critical NameErrors in jaraco.util.logging.
* Enabled custom parameters in logging.setup.

4.4
===

* Extracted KeyTransformingDict from FoldedCaseKeyedDict with much more
  complete handling of key transformation.

4.3
===

* Added `jaraco.filesystem.recursive_glob`, which acts like a regular glob,
  but recurses into sub-directories.

4.2
===

* Added `dictlib.DictStack` for stacking dictionaries on one another.
* Added `string.global_format` and `string.namespace_format` for formatting
  a string with globals and with both globals and locals.

4.1
===

* Added jaraco.util.dictlib.IdentityOverrideMap
* Added jaraco.util.itertools.always_iterable
* All modules now use unicode literals, consistent with Python 3 syntax

4.0
===

The entire package was combed through for deprecated modules. Many of the
modules and functions were moved or renamed for clarity and to match
modern PEP-8 naming recommendations.

* Renamed `jaraco.util.iter_` to `jaraco.util.itertools`
* Renamed `jaraco.util.cmp_` to `jaraco.util.cmp`
* Moved PasswordGenerator to jaraco.util.auth
* Updated callable() to use technique that's good for all late Python versions
* Removed jaraco.util.odict (use py26compat.collections.OrderedDict for
  Python 2.6 and earlier).
* Renamed many functions and methods to conform more to the PEP-8 convention:

  - jaraco.util

    + Moved `make_rows`, `grouper`, `bisect`, `groupby_saved`, and
      `FetchingQueue` to `itertools` module. Renamed groupby_saved to
      GroubySaved.
    + Moved `trim` to `string` module.
    + Moved `Stopwatch` to new `timing` module.
    + Moved `splitter` to `string.Splitter`.
    + Removed replaceLists.
    + Moved `readChunks` to `filesystem.read_chunks`.
    + Moved `coerce_number` and `ordinalth` to new `numbers` module.
    + Moved `callable` to `jaraco.lang.python` module.
    + Moved `randbytes` to `random` module.

  - jaraco.dateutil

    + ConstructDatetime is now DatetimeConstructor.construct_datetime
    + DatetimeRound is now datetime_round
    + GetNearestYearForDay is now get_nearest_year_for_day
    + Removed getPeriodSeconds, getDateFormatString, and GregorianDate
      backward-compatibility aliases.

  - jaraco.filesystem

    + GetUniquePathname is now get_unique_pathname
    + GetUniqueFilename has been removed.

  - jaraco.logging

    + Removed deprecated add_options.
    + methods, attributes, and parameters on TimeStampFileHandler updated.

* Removed jaraco.filesystem.change (moved to jaraco.windows project).
* Added jaraco.util.filesystem.tempfile_context.
* Removed jaraco.util.excel (functionality moved to jaraco.office project).
* Removed jaraco.util.timers (functionality moved to jaraco.windows project).
* Removed jaraco.util.scratch (unused).
* Removed ``jaraco.util.xml_``.
* Added jaraco.util.exceptions.suppress_exception.
* Added jaraco.util.itertools.last.
* Moved `jaraco.util.dictlib.NonDataProperty` to `jaraco.util.properties`.

3.9.2
=====

* Another attempt to avoid SandboxViolation errors on some Python
  installations (Python 2 only).

3.9.1
=====

* Address attribute error for some older versions of distribute and
  setuptools.

3.9
===

* dictlib.RangeMap now uses PEP-8 naming. Use `sort_params` and
  `key_match_comparator` for
  the constructor and `undefined_value`, `last_item`, and `first_item` class
  attributes.
* Added `jaraco.util.bitutil.BitMask` metaclass.

3.8.1
=====

* jaraco namespace package now supports py2exe
* ItemsAsAttributes now works with dicts that customize `__getitem__`

3.8
===

* `jaraco.util.logging` now supports ArgumentParser with `add_arguments`
  and `setup`. `add_options` has been replaced with `add_arguments` for
  both OptionParser and ArgumentParser and is deprecated.
* Added `jaraco.util.exceptions` with a function for determining if a
  callable throws a specific exception.
* Added `is_decodable` and `is_binary` to `jaraco.util.string`.

3.7
===

* Added jaraco.util.dictlib.DictAdapter.
* Added jaraco.util.dictlib.ItemsAsAttributes.
* Added wallpaper script by Samuel Huckins with added support for Windows.
* Added stream.Tee (for outputting to multiple streams).
* Fix for NameErrors.
* Added cross-platform getch function.
* Added several new functions to `iter_`.
* Enhanced EditableFile with support for non-ascii text and capturing
  a diff after changes are made.


3.6
===

* Added jaraco.util.editor (with EditableFile for editing strings in a
  subprocess editor).

3.5.1
=====

* Removed apng from .image so the package now installs on Python 2.5
  with only one error.

3.5
===

* Added `jaraco.util.iter_.window` and `.nwise`
* Added `jaraco.util.filesystem.ensure_dir_exists` decorator
* Added `jaraco.util.iter_.Peekable` iterator wrapper
* Moved `jaraco.util.package` to `jaraco.develop` project

3.4
===

* Adding jaraco.util.concurrency

3.3
===

* Added prorating calculator and console script calc-prorate.
* Added `iter_.peek`
* Renamed QuickTimer to Stopwatch - modified to PEP8 specs
* Adding jaraco.filesystem.DirectoryStack
* Added `iter_.one` and `iter_.first`

3.2
===

* Removed release module and moved its function to the package module.

3.1
=====

* Added skip_first to `jaraco.util.iter_`
* Moved rss module to `jaraco.net` package.
* Bug fixes in `iter_.flatten`.
* Restored Python 2 compatibility and implemented 2to3 for deployment.
  `jaraco.util` is now easy_installable on Python 2 and Python 3.

3.0.1
=====

* More Python 3 changes.
* Fixes bug in `jaraco.util.meta.LeafClassesMeta`.
* Added jaraco.util.string.local_format

3.0
===

This version includes many backwards-incompatible changes.

* May require Python 2.6
* Removed powerball module
* Refactored RangeMap: RangeValueUndefined, RangeItem/First/Last moved into RangeMap class. RangeValueUndefined, RangeItemFirst, and RangeItemLast are now instances, not classes. Renamed to UndefinedValue, Item, FirstItem, LastItem.
* Renamed DictMap function to dict_map
* Renamed `iter_.evalAll` to `iter_.consume` and evalN to consume_n
* More Python 3 improvements
* Added rss feed handler (this perhaps this belongs in jaraco.net, and may be moved in the future)
* Renamed ciString to jaraco.util.string.FoldedCase and added support for sorting case-insensitive strings
* Added some useful iterator tools.
* Added bitutil, based on some functions in jaraco.input
* Added some rich comparison mixins in `jaraco.util.cmp_`
* Added PasswordGenerator from jaraco.site
* Added logging module for commonly-used logging patterns

2.3
===

* Minor fixes, primarily to deployment techniques
* Mostly Python 3 compatible.
* Final release before major refactoring.

2.2
===

* First release with documentation.

2.1
===

* Added package release script.
* Added RelativePath, a class for manipulating file system paths
* Added trim function

2.0
===

* First release with no dependencies.

1.0
===

* Initial release
