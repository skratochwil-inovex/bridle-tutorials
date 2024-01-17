# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

from datetime import date


# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Cytron Maker RP2040 Tutorials'
copyright = f'{date.today().year}, TiaC Systems'
author = 'TiaC Systems'

version = '0.1.0'
release = '0.1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.intersphinx',
    'sphinx.ext.ifconfig',
    'sphinx.ext.todo',
    'sphinx_immaterial',
]

templates_path = ['_templates']
exclude_patterns = []

language = 'de'

rst_prolog = '''
.. |copyright| replace:: {copyright}
.. |project| replace:: {project}
.. |author| replace:: {author}
'''.format(
    copyright = copyright,
    project = project,
    author = author,
)

# -- Options for PDF output --------------------------------------------------
# https://www.mos6581.org/rinohtype/master/quickstart.html#sphinx-quickstart

rinoh_documents = [dict(doc='index', target='bridle-tutorials')]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_title = project
html_favicon = '_static/images/bridle.ico'
html_logo = '_static/images/bridle.svg'

html_theme = 'sphinx_immaterial'
html_static_path = ['_static']
html_theme_options = {
    "icon": {
        "repo": "fontawesome/brands/github",
    },
    "repo_url": "https://github.com/tiacsys/bridle-tutorials/",
    "repo_name": "TiaCSys/Bridle-Tutorials",
    "globaltoc_collapse": True,
    "features": [
        "navigation.expand",
        # "navigation.tabs",
        # "toc.integrate",
        "navigation.sections",
        # "navigation.instant",
        # "header.autohide",
        "navigation.top",
        # "navigation.tracking",
        # "search.highlight",
        "search.share",
        "toc.follow",
        "toc.sticky",
        "content.tabs.link",
        "announce.dismiss",
    ],
    "palette": [
        {
            "media": "(prefers-color-scheme: light)",
            "scheme": "default",
            "primary": "indigo",
            "accent": "amber",
            "toggle": {
                "icon": "material/weather-sunny",
                "name": "In den dunklen Modus wechseln",
                # "name": "Switch to dark mode",
            },
        },
        {
            "media": "(prefers-color-scheme: dark)",
            "scheme": "slate",
            "primary": "indigo",
            "accent": "amber",
            "toggle": {
                "icon": "material/weather-night",
                "name": "In den hellen Modus wechseln",
                # "name": "Switch to light mode",
            },
        },
    ],
}

# -- Options for intersphinx extension ---------------------------------------
# https://www.sphinx-doc.org/en/master/usage/extensions/intersphinx.html#configuration

intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
}

# -- Options for todo extension ----------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/extensions/todo.html#configuration

todo_include_todos = True
