Changes
=======

2.0.1 (unreleased)
------------------

- Sort the imports with ruff (one per line, ``from`` imports first, no
  sections) and format the code with ``ruff format`` (90 characters per line,
  single quotes).
  [rnix]

- Add import sorting (``I`` rules) and the formatter settings to the ruff
  configuration in ``pyproject.toml``.
  [rnix]


2.0.0 (2026-10-24)
------------------

- Require ``cone.app`` 2.0. ``treibstoff>1.99`` is required already, which
  only ``cone.app`` 2.0 is compatible with. Check out ``cone.app`` and
  ``treibstoff`` from their 2.0 branches in ``mx.ini``.
  [rnix]

- Modernise the code ruff flags as outdated: ``u''`` prefixes, ``.format()``
  over f-strings. Remove unused import. Behaviour unchanged.
  [rnix]

- Add ``qa.ruff`` domain to Makefile and pin the ruff rule selection in
  ``pyproject.toml``, ``make check`` runs ``ruff check``.
  [rnix]

- Pin ``setuptools<82.0.0`` in ``mx.ini``. ``pyramid`` 2.0.2 still imports
  ``pkg_resources``, which ``setuptools`` 82 removed.
  [rnix]


1.1.0 (2026-02-03)
------------------

- Refactor package layout to use ``pyproject.toml`` and implicit namespace packages.
  [rnix]

- Setup Makefile.
  [lenadax]

- Run tests with pytest.
  [lenadax]

- Initial work.
  [rnix, toalba, lenadax]
