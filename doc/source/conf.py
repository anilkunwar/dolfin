# -*- coding: utf-8 -*-
#
# DOLFIN documentation build configuration file, created by
# sphinx-quickstart on Fri Mar 18 10:11:41 2016.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.
import subprocess
import sys
import os

ONLY_SPHINX = os.environ.get('ONLY_SPHINX', False)
run_doxygen = not ONLY_SPHINX

if run_doxygen:
    # Doxygen handling in parent directory
    current_dir = os.getcwd()
    os.chdir("../")

    # Run doxygen on C++ sources, generates XML output for us to convert into Sphinx and SWIG formats.
    subprocess.call('doxygen', shell=True)
    
    # Convert doxygen XML output to *.rst files per subdirectory and make SWIG docstrings.i
    subprocess.call(["python", "./generate_api_rst.py"])

    os.chdir(current_dir)

# We can't compile the swig generated headers on RTD.  Instead, we generate the python part as usual,
# and then mock the cpp objects by importing a generated module full of stubs that looks enough like
# what the C++ SWIG modules will look like.
if os.path.isfile('../mock_cpp_modules.py'):
    sys.path.insert(0, '../')
    sys.path.insert(0, '../../site_packages')
    import mock_cpp_modules

# TODO: Copy site-packages/dolfin to tmp-dolfin/
# Run cmake/scripts/generate-generate-swig-interface.py with output to tmp-swig/
# Run swig in every directory tmp-swig/modules/*
# Copy generated tmp-swig/modules/*/*.py to tmp-dolfin/cpp/
# Now it should be possible to import dolfin and let Sphinx do its magic on the docstrings.

sys.path.append(os.getcwd())
import rstprocess

# Copy demo files into doc source tree and process with pylit
rstprocess.process()

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
# sys.path.insert(0, os.path.abspath('.'))


# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.todo',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'DOLFIN'
copyright = u'2016, FEniCS Project'
author = u'FEniCS Project'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = u'2017.1.0.dev0'
# The full version, including alpha/beta/rc tags.
release = u'2017.1.0.dev0'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = []

# The reST default role (used for this markup: `text`) to use for all
# documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
#keep_warnings = False

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#html_theme = 'alabaster'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
#html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = None

# The name of an image file (relative to this directory) to use as a favicon of
# the docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
#html_extra_path = []

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
#html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Language to be used for generating the HTML full-text search index.
# Sphinx supports the following languages:
#   'da', 'de', 'en', 'es', 'fi', 'fr', 'hu', 'it', 'ja'
#   'nl', 'no', 'pt', 'ro', 'ru', 'sv', 'tr'
#html_search_language = 'en'

# A dictionary with options for the search language support, empty by default.
# Now only 'ja' uses this config value
#html_search_options = {'type': 'default'}

# The name of a javascript file (relative to the configuration directory) that
# implements a search results scorer. If empty, the default will be used.
#html_search_scorer = 'scorer.js'

# Output file base name for HTML help builder.
htmlhelp_basename = 'DOLFINdoc'

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
#'papersize': 'letterpaper',

# The font size ('10pt', '11pt' or '12pt').
#'pointsize': '10pt',

# Additional stuff for the LaTeX preamble.
#'preamble': '',

# Latex figure (float) alignment
#'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'DOLFIN.tex', u'DOLFIN Documentation',
     u'FEniCS Project', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'dolfin', u'DOLFIN Documentation',
     [author], 1)
]

# If true, show URL addresses after external links.
#man_show_urls = False


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'DOLFIN', u'DOLFIN Documentation',
     author, 'DOLFIN', 'One line description of project.',
     'Miscellaneous'),
]

# Documents to append as an appendix to all manuals.
#texinfo_appendices = []

# If false, no module index is generated.
#texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#texinfo_show_urls = 'footnote'

# If true, do not generate a @detailmenu in the "Top" node's menu.
#texinfo_no_detailmenu = False


# -- Options for Epub output ----------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project
epub_author = author
epub_publisher = author
epub_copyright = copyright

# The basename for the epub file. It defaults to the project name.
#epub_basename = project

# The HTML theme for the epub output. Since the default themes are not
# optimized for small screen space, using the same theme for HTML and epub
# output is usually not wise. This defaults to 'epub', a theme designed to save
# visual space.
#epub_theme = 'epub'

# The language of the text. It defaults to the language option
# or 'en' if the language is not set.
#epub_language = ''

# The scheme of the identifier. Typical schemes are ISBN or URL.
#epub_scheme = ''

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#epub_identifier = ''

# A unique identification for the text.
#epub_uid = ''

# A tuple containing the cover image and cover page html template filenames.
#epub_cover = ()

# A sequence of (type, uri, title) tuples for the guide element of content.opf.
#epub_guide = ()

# HTML files that should be inserted before the pages created by sphinx.
# The format is a list of tuples containing the path and title.
#epub_pre_files = []

# HTML files that should be inserted after the pages created by sphinx.
# The format is a list of tuples containing the path and title.
#epub_post_files = []

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']

# The depth of the table of contents in toc.ncx.
#epub_tocdepth = 3

# Allow duplicate toc entries.
#epub_tocdup = True

# Choose between 'default' and 'includehidden'.
#epub_tocscope = 'default'

# Fix unsupported image types using the Pillow.
#epub_fix_images = False

# Scale large images.
#epub_max_image_width = 0

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#epub_show_urls = 'inline'

# If false, no index is generated.
#epub_use_index = True


# Hack to support avoid renaming download files with same names coming
# from different directories (CMakeLists.txt, Makefile etc)

# Fix add_file, see https://github.com/sphinx-doc/sphinx/issues/2720
from sphinx.util import FilenameUniqDict
from os import path
def add_file(self, docname, newfile):
    if newfile in self:
        self[newfile][0].add(docname)
        return self[newfile][1]
    uniquename = path.basename(newfile)
    i = 0
    while uniquename in self._existing:
        i += 1
        uniquename = path.join('subdir%s' % i, path.basename(newfile))
    self[newfile] = (set([docname]), uniquename)
    self._existing.add(uniquename)
    return uniquename
FilenameUniqDict.add_file = add_file

# Hack to support sub-directories within the _download directory
# see https://github.com/sphinx-doc/sphinx/issues/2720
from sphinx.builders.html import StandaloneHTMLBuilder, ensuredir, copyfile
from docutils.utils import relative_path
from sphinx.util.console import brown
def copy_download_files(self):
    def to_relpath(f):
        return relative_path(self.srcdir, f)
    # copy downloadable files
    if self.env.dlfiles:
        ensuredir(path.join(self.outdir, '_downloads'))
        for src in self.app.status_iterator(self.env.dlfiles,
                                            'copying downloadable files... ',
                                            brown, len(self.env.dlfiles),
                                            stringify_func=to_relpath):
            dest = self.env.dlfiles[src][1]
            subdirs, filename = os.path.split(dest)
            if subdirs:
                ensuredir(path.join(self.outdir, '_downloads', subdirs))
            try:
                copyfile(path.join(self.srcdir, src),
                         path.join(self.outdir, '_downloads', dest))
            except Exception as err:
                self.warn('cannot copy downloadable file %r: %s' %
                          (path.join(self.srcdir, src), err))
StandaloneHTMLBuilder.copy_download_files = copy_download_files

# Hack to support sub-directories within the _images directory
# see https://github.com/sphinx-doc/sphinx/issues/2720
def copy_image_files(self):
    # type: () -> None
    # copy image files
    if self.images:
        ensuredir(path.join(self.outdir, self.imagedir))
        for src in self.app.status_iterator(self.images, 'copying images... ',
                                            brown, len(self.images)):
            dest = self.images[src]
            subdirs, filename = os.path.split(dest)
            if subdirs:
                ensuredir(path.join(self.outdir, self.imagedir, subdirs))
            try:
                copyfile(path.join(self.srcdir, src),
                         path.join(self.outdir, self.imagedir, dest))
            except Exception as err:
                logger.warning('cannot copy image file %r: %s', path.join(self.srcdir, src), err)
StandaloneHTMLBuilder.copy_image_files = copy_image_files

