#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Braindecode documentation build configuration file, created by
# sphinx-quickstart on Sat Jul  1 01:51:38 2017.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

import os
import sys

import matplotlib
matplotlib.use('agg')

import sphinx_gallery  # noqa
from numpydoc import numpydoc, docscrape  # noqa

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

curdir = os.path.dirname(__file__)
sys.path.append(os.path.abspath(os.path.join(curdir, 'sphinxext')))

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.doctest',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    'sphinx.ext.linkcode',
    'sphinx.ext.ifconfig',
    'sphinx.ext.intersphinx',
    'sphinx.ext.githubpages',
    'sphinx_gallery.gen_gallery',
    'numpydoc',
    'gh_substitutions',
]


def linkcode_resolve(domain, info):
    """Determine the URL corresponding to a Python object.

    Parameters
    ----------
    domain : str
        Only useful when 'py'.
    info : dict
        With keys "module" and "fullname".

    Returns
    -------
    url : str
        The code URL.

    Notes
    -----
    This has been adapted to deal with our "verbose" decorator.

    Adapted from SciPy (doc/source/conf.py).
    """
    import mne
    if domain != 'py':
        return None

    modname = info['module']
    fullname = info['fullname']

    submod = sys.modules.get(modname)
    if submod is None:
        return None

    obj = submod
    for part in fullname.split('.'):
        try:
            obj = getattr(obj, part)
        except Exception:
            return None
    # deal with our decorators properly
    while hasattr(obj, '__wrapped__'):
        obj = obj.__wrapped__

    try:
        fn = inspect.getsourcefile(obj)
    except Exception:
        fn = None
    if not fn:
        try:
            fn = inspect.getsourcefile(sys.modules[obj.__module__])
        except Exception:
            fn = None
    if not fn:
        return None
    fn = op.relpath(fn, start=op.dirname(mne.__file__))
    fn = '/'.join(op.normpath(fn).split(os.sep))  # in case on Windows

    try:
        source, lineno = inspect.getsourcelines(obj)
    except Exception:
        lineno = None

    if lineno:
        linespec = "#L%d-L%d" % (lineno, lineno + len(source) - 1)
    else:
        linespec = ""

    if 'dev' in braindecode.__version__:
        kind = 'master'
    else:
        kind = 'maint/%s' % ('.'.join(mne.__version__.split('.')[:2]))
    return "http://github.com/braindecode/braindecode/blob/%s/braindecode/%s%s" % (  # noqa
       kind, fn, linespec)


autosummary_generate = True
autodoc_default_options = {'inherited-members': False}

numpydoc_show_class_members = False

exclude_patterns = ['_build', '_templates']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'Braindecode'
copyright = '2018-2021, Braindecode developers'
author = 'Braindecode developers'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
import braindecode
version = braindecode.__version__
# The full version, including alpha/beta/rc tags.
release = version

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True


# Sphinx-gallery configuration

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {
    'python': ('https://docs.python.org/{.major}'.format(sys.version_info), None),
    'numpy': ('https://docs.scipy.org/doc/numpy/', None),
    'scipy': ('https://docs.scipy.org/doc/scipy/reference', None),
    'matplotlib': ('https://matplotlib.org/', None),
    'sklearn': ('http://scikit-learn.org/stable', None),
    'mne': ('http://mne.tools/stable', None),
}

sphinx_gallery_conf = {
    'examples_dirs': ['../examples'],
    'gallery_dirs': ['auto_examples'],
    'doc_module': ('braindecode', 'mne'),
    'backreferences_dir': 'generated',
    'show_memory': True,
    'reference_url': dict(braindecode=None),
}

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = 'alabaster'

import sphinx_rtd_theme
html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'Braindecodedoc'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'Braindecode.tex', 'Braindecode Documentation',
     'Robin Tibor Schirrmeister', 'manual'),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'braindecode', 'Braindecode Documentation',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'Braindecode', 'Braindecode Documentation',
     author, 'Braindecode', 'One line description of project.',
     'Miscellaneous'),
]
