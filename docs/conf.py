from datetime import datetime


extensions = []
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'

project = u'Allabaster'
year = datetime.now().year
copyright = u'%d Alexander Artemenko' % year

exclude_patterns = ['_build']

html_theme = 'alabaster'
html_sidebars = {
    '**': [
        'about.html',
        'navigation.html',
        'relations.html',
        'searchbox.html',
        'donate.html',
    ]
}
html_theme_options = {
    'description': "An embeddable Sphinx theme, based on Alabaster",
    'github_user': 'AllMyChanges',
    'github_repo': 'allabaster',
    'fixed_sidebar': True,
}

extensions.append('releases')
releases_github_path = 'AllMyChanges/allabaster'
# Our pre-0.x releases are unstable / mix bugs+features
releases_unstable_prehistory = True
