# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

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

html_theme = 'sphinx_immaterial'
html_static_path = ['_static']

# -- Options for intersphinx extension ---------------------------------------
# https://www.sphinx-doc.org/en/master/usage/extensions/intersphinx.html#configuration

intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
}

# -- Options for todo extension ----------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/extensions/todo.html#configuration

todo_include_todos = True
