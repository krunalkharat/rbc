import os
import sys
sys.path.insert(0, os.path.abspath('../'))
import docutils

extensions = [
    'sphinx.ext.intersphinx',
    'sphinx.ext.doctest',
    'sphinx.ext.extlinks',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.coverage',
    'sphinx.ext.napoleon'
]

napoleon_google_docstring = False
napoleon_numpy_docstring = True
autosummary_generate = True
autosummary_imported_members = True

autodoc_default_options = {
    'inherited-members': None,
}

source_suffix = '.rst'
master_doc = 'index'
project = 'rbc'
copyright = '2019, Xnd-Project'
version = 'v0.1.0'
release = 'v0.1.0'
exclude_patterns = ['doc', '_build']
pygments_style = 'sphinx'

html_static_path = ['_static']
templates_path = ['_templates']

primary_domain = 'py'
add_function_parentheses = False

html_theme = "sphinx_rtd_theme"
html_theme_path = ["_themes", ]

html_theme_options = {
    'canonical_url': 'https://xnd.io/',
    'analytics_id': '',
    'logo_only': True,
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    # Toc options
    'collapse_navigation': True,
    'sticky_navigation': True,
    'navigation_depth': 4,
}

html_context = {
    "display_github": False,
    # Add 'Edit on Github' link instead of 'View page source'
    "last_updated": True,
    "commit": False,
}

html_show_sourcelink = False

extlinks = {
    'issue': ('https://github.com/xnd-project/rbc/issues/%s', 'GH#'),
    'pr': ('https://github.com/xnd-project/rbc/pull/%s', 'GH#')
}

html_logo = "images/xndlogo.png"


def setup(app):
    app.add_crossref_type(
        'topic', 'topic', 'single: %s', docutils.nodes.strong
    )
    app.add_javascript("copybutton.js")
